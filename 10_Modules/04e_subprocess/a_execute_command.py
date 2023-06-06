import os
import subprocess


def run_a_command(cmd):
    result = os.system(cmd)
    print(f"{result =}")

    result2 = subprocess.call(cmd)
    print(f"{result2 =}")


# run_a_command("pst")
run_a_command("ps")
