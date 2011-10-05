'''
Created on 2011-09-22

@author: Alec
'''
import unittest

from pyramid import testing

from pwc import views as mut

from . import SAMPLE_URL, SAMPLE_STATUS, SAMPLE_HEADERS, SAMPLE_BODY

class APITests(unittest.TestCase):
    
    def setUp(self):
        self.config = testing.setUp()
        
        
    def tearDown(self):
        """ Clear out the application registry """
        testing.tearDown()
        

    def test_make_request(self):
        """Do it!"""
        request = testing.DummyRequest(params={"url": SAMPLE_URL})
        
        response = mut.make_request(request)
        status = response["status"]
        headers = response["headers"]
        body = response["body"]
        self.assertEquals(SAMPLE_STATUS, status)
        self.assertEquals(SAMPLE_BODY, body)
        for key, value in SAMPLE_HEADERS.items():
            self.assert_(key in headers)
            self.assertEquals(value, headers[key])