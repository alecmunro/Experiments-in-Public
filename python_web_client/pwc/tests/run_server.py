'''
Created on 2011-10-02

@author: Alec
'''
import time, subprocess, os, signal

def run_server(ini):
    subprocess.Popen(["paster", "serve", ini, "--pid-file=my.pid"])
    time.sleep(1)#Waiting for PID
    app_pid = open("my.pid").read()
    return app_pid
    
def kill_server(pid):
    try:
        os.kill(int(pid), signal.SIGTERM)
    except AttributeError:
        #I would really like a better way to handle this. Py2.7 maybe?
        subprocess.Popen(["taskkill", "/F", "/PID", pid])
