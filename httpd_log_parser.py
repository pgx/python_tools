import re
import datetime
import time

def cacu(size):
    return size/1048576

def line_parse(line):
    pattern = r"^(?P<ip>(\d{2,3}\.?){4}) - - (?P<time>(\[.+\])) (?P<method>\".+\") (?P<return>\d{3}) (?P<size>.+)"
    m = re.match(pattern, line)
    if m:
        return m.groupdict()
    else:
        return False

def ts_to_date():
    ts = time.time()
    timestamp = ts- 43200
    return datetime.datetime.fromtimestamp(timestamp).strftime("%d/%b/%Y")

if __name__ == "__main__":
    result = dict()
    log = "/var/log/httpd/usd1000.log"
    fp = open(log, "r")
    for line in fp:
        m = line_parse(line)
        if m:
            if m['ip'] not in result:
                try:
                    result[m['ip']] = int(m['size'])
                    print(m['time'][1:11])
                except:
                    pass
            else:
                try:
                    result[m['ip']] += int(m['size'])
                except:
                    pass
        else:
            pass
    print(result)
