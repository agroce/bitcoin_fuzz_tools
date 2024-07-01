import glob
import os
import shutil
import subprocess
import sys
import time

mutant_dir = sys.argv[1]
if len(sys.argv) > 2:
    extra_args = sys.argv[2]
else:
    extra_args = ""

modes = ["", "-use_value_profile=1"]

data = {}
for mode in modes:
    data[mode] = []

mutants = glob.glob(mutant_dir + "/killed_*")
mutants.extend(glob.glob(mutant_dir + "/survived_*"))

for m in mutants:
    dir = os.path.basename(m) + "_pruned"
    if not os.path.exists(dir):
        print("PRUNING FOR", dir)
        os.mkdir(dir)
        subprocess.call(["python3 ../bitcoin_fuzz_tools/libfuzzer_prune.py " + m + " 700 ../qa-assets/fuzz_seed_corpus/process_messages " + dir + " 1 1000"],
                            shell=True)

print("DONE PRUNING!")
print()

RUNS = 10

for r in range(RUNS):
    for m in mutants:
        for mode in modes:
            print("RUNNING", m, mode)
            try:
                shutil.rmtree("this_corpus")
            except FileNotFoundError:
                pass
            shutil.copytree(os.path.basename(m) + "_pruned", "this_corpus")
            start = time.time()        
            subprocess.call([m + " " + mode + " " + extra_args + " this_corpus"], shell=True)
            finish = time.time()
            print("FINISHED IN", round(finish-start, 2))
            data[mode].append((m, finish-start))
            print("RESULTS SO FAR:")
            for fm in data:
                print(fm, data[fm])
        
for mode in modes:
    print(mode, data[mode])
