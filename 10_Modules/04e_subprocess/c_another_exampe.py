import subprocess


def get_execution_result(cmd):
    p = subprocess.Popen(
        cmd.split(),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    output, error = p.communicate()
    output = output.decode("utf-8")
    error = error.decode("utf-8")

    if output:
        print(output)
    else:
        print(error)


get_execution_result("ls /usr/bin/python3")
get_execution_result("ls -la")
