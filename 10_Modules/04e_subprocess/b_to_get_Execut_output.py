import subprocess

myprocess = subprocess.Popen(
    "ps", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
)
output, error = myprocess.communicate()
# print(type(output))  # <class 'bytes'>

output = output.decode("utf-8")
error = error.decode("utf-8")


if output:
    pids = list(map(lambda x: x.split()[0], output.splitlines()[1:]))
    print(f"{pids = }")
else:
    print(error)
