# OS: CentOS6
# python: 2.6.6
# Create: 2016/12/31

import subprocess
import re

def pingtest(dst, times):
    cmd = ['ping', '-q', '-c', times, dst]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    pattern = re.compile("rtt min/avg/max/mdev = (?P<min>[0-9]+\.[0-9]+)/(?P<avg>[0-9]+\.[0-9]+)/(?P<max>[0-9]+\.[0-9]+).+")
    result = pattern.match(proc.stdout.readlines()[-1])
    if result:
        return result.groupdict()
    else:
        return False

if __name__ == "__main__":
    pingresult = pingtest("www.hinet.net", "10")
    print(pingresult)
