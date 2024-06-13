import glob
import os
import shutil
import signal
import subprocess
import sys
import time
from contextlib import contextmanager


class TimeoutException(Exception):
    """"Exception thrown when timeouts occur"""


@contextmanager
def time_limit(seconds):
    """Method to define a time limit before throwing exception"""

    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

def silent_run_with_timeout(cmd, timeout, verbose):
    # Allow functions instead of commands, for use as a library from a script
    if verbose:
        print("*" * 30)
    if callable(cmd):
        try:
            if verbose:
                print("CALLING FUNCTION", cmd)
            with time_limit(timeout):
                return cmd()
        except TimeoutException:
            print("ABORTED WITH TIMEOUT")
            return 1 # non-zero return code may be interpreted as failure/crash/timeout
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

copied = 0
skipped = 0
for f in files:
    start = time.time()
    r = silent_run_with_timeout(fuzz_cmd + " " + f, timeout, False)
    finish = time.time()
    print("ANALYZED", f, "IN", round(finish - start, 2), "SECONDS")
    if r == 0:
        shutil.copyfile(f, os.path.join(new_corpus_dir, os.path.basename(f)))
        copied += 1
    else:
        print(f, "DETECTS THE MUTANT!")
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
