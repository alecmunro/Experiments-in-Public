'''
Created on 2011-10-02

@author: Alec
'''
import time, subprocess

def run_server(ini):
    subprocess.Popen("paster serve {0} --pid-file=my.pid".format(ini))
    time.sleep(1)#Waiting for PID
    app_pid = open("my.pid").read()
    return app_pid
    
def kill_server(pid):
    #I would really like a better way to handle this.
    subprocess.Popen("taskkill /F /PID {0}".format(pid))
