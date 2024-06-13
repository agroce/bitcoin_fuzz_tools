import glob
import os
import signal
import subprocess
import sys
import time

dir = sys.argv[1]
timeout = int(sys.argv[2])
corpus_dir = sys.argv[3]

def silent_run_with_timeout(cmd, timeout):
    start_P = time.time()
    try:
        with open("cmd_out.txt", 'w') as cmd_out:
            P = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid,
                                 stdout=cmd_out, stderr=cmd_out)
            while (P.poll() is None) and ((time.time() - start_P) < timeout):
                time.sleep(min(0.5, timeout / 10.0)) # Allow for small timeouts
            if P.poll() is None:
                os.killpg(os.getpgid(P.pid), signal.SIGTERM)
        with open("cmd_out.txt", 'r') as cmd_out:
            try:
                cmd_out = cmd_out.read()
            except:
                cmd_out = "ERROR READING OUTPUT"
    finally:
        if P.poll() is None:
            print("KILLING SUBPROCESS DUE TO TIMEOUT")
            os.killpg(os.getpgid(P.pid), signal.SIGTERM)

    return (cmd_out, P.returncode)


for f in glob.glob(dir + "/killed_*"):
    start = time.time()
    (output, r) = silent_run_with_timeout(f + " " + corpus_dir + "/*", timeout)
    finish = time.time()
    print("CHECKED", f, "IN", round(finish - start, 2), "SECONDS")
    executed = 0
    for line in output.split("\n"):
        if "Executed" in line:
            executed += 1
    print("EXECUTED", executed, "INPUTS")
    
                                                   
