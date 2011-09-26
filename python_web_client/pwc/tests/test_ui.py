'''
Created on 2011-09-23

@author: Alec
'''
import time
from unittest import TestCase
import subprocess

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pwc import main
from pwc.tests.echo_server import EchoServer, DEFAULT_ADDRESS

SAMPLE_STATUS = 302
SAMPLE_HEADERS = {"heya": "hoya"}
SAMPLE_BODY = "Jimmy Hoffa's"

class UITests(TestCase):
    
    def setUp(self):
        self.app = subprocess.Popen("paster serve ..\..\development.ini --pid-file=my.pid")
        time.sleep(1)#Waiting for PID
        self.app_pid = open("my.pid").read()
        self.test_server = EchoServer(DEFAULT_ADDRESS)
        self.test_server.set_echo(SAMPLE_STATUS, SAMPLE_HEADERS, SAMPLE_BODY)
        self.test_server.threaded_serve()

    def test_something(self):
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:6543")
        try:
            WebDriverWait(driver, 10).until(
                        lambda driver: "Python Web Client" in driver.title)
            self.assertEquals(u'Welcome to the Python Web Client!', 
                              driver.title)
            url_box = driver.find_element_by_id("url")
            url_box.send_keys("http://{0}:{1}/".format(*DEFAULT_ADDRESS))
            submit = driver.find_element_by_id("submit_request")
            submit.click()
            time.sleep(1)
            self.assertEqual(SAMPLE_STATUS, 
                         int(driver.find_element_by_class_name("status").text))
            for name, value in SAMPLE_HEADERS.items():
                self.assertEqual(value, driver.find_element_by_name(name).text)
        finally:
            driver.quit()
        
        
    def tearDown(self):
        #I would really like a better way to handle this.
        subprocess.Popen("taskkill /F /PID {0}".format(self.app_pid))
        self.test_server.threaded_shutdown()
