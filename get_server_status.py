# python version: 2.7.9
# last update: 2016/12/30
# features:
#     2016/12/30: get_cpu_temperature with linux command sensors

import subprocess
import re

def get_cpu_temperature():
    cmd = ['sensors']
    r = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    lines = r.stdout.readlines()
    pattern = re.compile("temp1:\s+\+([0-9]{2,3}\.[0-9]).+")
    result = pattern.match(lines[-3]).group(1)
    if result:
        return result
    else:
        return False

if __name__ == "__main__":
    cpu_temp = get_cpu_temperature()
    if cpu_temp:
        print(cpu_temp)
