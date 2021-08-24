from datetime import datetime
import subprocess

if __name__ == "__main__":
    command = "ffmpeg -h"
    proc = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE)

    output_pipe = proc.stdout

    while (res := output_pipe.read(2048)):
        print(res.decode("utf-8"))

    while 0:
        print("no loop")

    print(datetime.now())
