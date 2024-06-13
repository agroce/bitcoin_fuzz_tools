import glob
import os
import shutil
import signal
import subprocess
import sys
import time


class TimeoutException(Exception):
    """"Exception thrown when timeouts occur"""


def silent_run_with_timeout(cmd, timeout, verbose):
    dnull = open(os.devnull, 'w')
    if verbose:
        print("EXECUTING", cmd)
    start_P = time.time()
    try:
        with open("cmd_errors.txt", 'w') as cmd_errors:
            P = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid,
                                 stdout=dnull, stderr=cmd_errors)
            while (P.poll() is None) and ((time.time() - start_P) < timeout):
                time.sleep(min(0.5, timeout / 10.0)) # Allow for small timeouts
            if P.poll() is None:
                os.killpg(os.getpgid(P.pid), signal.SIGTERM)
        with open("cmd_errors.txt", 'r') as cmd_errors:
            try:
                cmd_errors_out = cmd_errors.read()
            except:
                cmd_errors_out = "ERROR READING OUTPUT"
        if verbose and len(cmd_errors_out) > 0:
            print("OUTPUT (TRUNCATED TO LAST 20 LINES):")
            print("\n".join(cmd_errors_out.split("\n")[-20:]))
    finally:
        if P.poll() is None:
            print("KILLING SUBPROCESS DUE TO TIMEOUT")
            os.killpg(os.getpgid(P.pid), signal.SIGTERM)
    if verbose:
        print("COMPLETE IN", round(time.time() - start_P, 2), "SECONDS")
        print("*" * 30)

    return P.returncode


def files_ok(fuzz_cmd, timeout, files, new_corpus_dir):
    start = time.time()
    # Returns True only if the tests pass for this whole set; restores directory to clean state
    for f in files:
        shutil.copyfile(f, os.path.join(new_corpus_dir, os.path.basename(f)))
    r = silent_run_with_timeout(fuzz_cmd + " " + new_corpus_dir + "/*", timeout)
    for f in files:
        os.remove(os.path.join(new_corpus_dir, os.path.basename(f)))
    finish = time.time()
    print("ANALYZED", len(files), "IN", round(finish - start, 2), "SECONDS")
    return (r == 0)


def make_splits(files, N):
    splits = []
    start = 0
    size = int(len(files) / N)
    for i in range(N):
        if i < N - 1:
            splits.append(files[start:start + size])
        else:
            splits.append(files[start:])
        start += size
    return splits


fuzz_cmd = sys.argv[1] # Assume appending filename to the end of this will fuzz the right input
timeout = int(sys.argv[2])
corpus_dir = sys.argv[3]
new_corpus_dir = sys.argv[4]
min_skipped = sys.argv[5]
min_new_corpus_size = sys.argv[6]

files = glob.glob(corpus_dir + "/*")
print("SUBSETTING CORPUS WITH", len(files), "FILES...")
sys.stdout.flush()

if not os.path.exists(new_corpus_dir):
    os.mkdir(new_corpus_dir)

ok_files = []
bad_files = []
unknown = files

SPLIT_SIZE = 4 # Initially let's just quarter the corpus

copied = 0
skipped = 0
while len(unknown) > 0:
    unknown = []
    splits = make_splits(unknown, SPLIT_SIZE)
    for s in splits:
        ok = files_ok(fuzz_cmd, timeout, s, new_corpus_dir)
        if ok:
            copied += len(s)
        else:
            if len(s) > 1:
                unknown.extend(s)
            else:
                skipped += 1
    sys.stdout.flush()

print("THERE WERE", skipped, "DETECTING INPUTS")
print("FINISHED, NEW CORPUS HAS", copied, "FILES")

if skipped < min_skipped:
    print("TOO FEW DETECTING INPUTS!")
    sys.exit(1)
if copied < min_new_corpus_size:
    print("NEW CORPUS IS TOO SMALL!")
    sys.exit(2)

sys.exit(0)
