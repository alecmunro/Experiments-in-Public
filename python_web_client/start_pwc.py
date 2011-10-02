'''
Created on 2011-10-02

@author: Alec
'''
import webbrowser

from pwc.tests.run_server import run_server, kill_server

INI_FILE = "development.ini"

if __name__ == "__main__":
    print("Starting PWC.")
    app_pid = run_server(INI_FILE)
    port = open(INI_FILE).read().split("port = ")[1].split()[0]
    url = "http://localhost:{0}/".format(port)
    print("Opening browser to {0}".format(url))
    webbrowser.open(url)
    raw_input("Press enter to stop PWC\n.")
    kill_server(app_pid)