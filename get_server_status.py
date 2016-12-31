# python version: 2.7.9
# last update: 2016/12/30
# features:
#     2016/12/30: get_cpu_temperature with linux command sensors

import subprocess
import re
import time
import mysql.connector

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

def get_server_connections():
    cmd = ["lsof", "-i"]
    r = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    lines = r.stdout.readlines()
    return len(lines)

def count_processes():
    cmd = ["ps", "aux"]
    r = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    lines = r.stdout.readlines()
    return len(lines)-1

#def get_hdd_df():
#    cmd = ['df', '-h']
#    r = subprocess.Popen(cmd, stdout=subprocess.PIPE)
#    result = r.stdout.read()
#    return result

if __name__ == "__main__":
    cpu_temp = get_cpu_temperature()
    conns = get_server_connections()
    procs = count_processes()
    #hdd_df = get_hdd_df()
    dbc = mysql.connector.connect(user='', password='',host='',database='')
    cursor = dbc.cursor()

    add_server_info = ("INSERT INTO basic "
                       "(cpu_temperature, connections, processes, btime) "
                       "VALUES (%s,%s,%s,NOW())")
    data_server_info = (float(cpu_temp), int(conns), int(procs))
    cursor.execute(add_server_info, data_server_info)
    sid = cursor.lastrowid

    #print("Server status: ")
    #if cpu_temp:
    #    print("\tCPU Temperature: {0}".format(cpu_temp))

    #if conns:
    #    print("\tServer Connections: {0}".format(conns))

#    if hdd_df:
#        print(hdd_df)
#        fp.write(hdd_df)
    dbc.commit()
    cursor.close()
    dbc.close()
