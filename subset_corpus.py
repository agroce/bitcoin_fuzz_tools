import glob
import os
import shutil
import sys

from muttfuzz.fuzzutil import silent_run_with_timeout

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
    r = silent_run_with_timeout(fuzz_cmd + " " + f, timeout, False)
    if r == 0:
        shutil.copyfile(f, os.path.join(new_corpus_dir, os.path.basename(f)))
        copied += 1
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
