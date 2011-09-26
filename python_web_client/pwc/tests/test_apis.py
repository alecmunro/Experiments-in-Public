'''
Created on 2011-09-22

@author: Alec
'''
import unittest

from pyramid import testing

from pwc.tests.echo_server import EchoServer, DEFAULT_ADDRESS
from pwc import views as mut

SAMPLE_URL = "http://{0}:{1}/anything".format(*DEFAULT_ADDRESS)
SAMPLE_STATUS = 302
SAMPLE_HEADERS = {"heya": "hoya"}
SAMPLE_BODY = "Jimmy Hoffa's"

class APITests(unittest.TestCase):
    
    def setUp(self):
        self.config = testing.setUp()
        self.test_server = EchoServer(DEFAULT_ADDRESS)
        self.test_server.set_echo(SAMPLE_STATUS, SAMPLE_HEADERS, SAMPLE_BODY)
        self.test_server.threaded_serve()
        
        
    def tearDown(self):
        """ Clear out the application registry """
        testing.tearDown()
        self.test_server.threaded_shutdown()
        

    def test_something(self):
        """Do it!"""
        request = testing.DummyRequest(params={"url": SAMPLE_URL})
        
        status, headers = mut.make_request(request)
        self.assertEquals(SAMPLE_STATUS, status)
        for key, value in SAMPLE_HEADERS.items():
            self.assert_(key in headers)
            self.assertEquals(value, headers[key])