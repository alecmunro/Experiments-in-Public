'''
Created on 2011-09-20

@author: Alec
'''
from unittest import TestCase

from pyramid import testing
import mock

from pwc import views as mut

SAMPLE_URL = "http://dont.goh.ere/service"
SAMPLE_STATUS = 200
SAMPLE_HEADERS = {"a": 1, "b": 2}
SAMPLE_BODY = "Elvis'"

SAMPLE_METHOD = "POST"
INVALID_METHOD = "GHOST"

CHARSET = "Gracelandish"
CHARSET_HEADERS = {mut.CONTENT_TYPE_HEADER: "{0}{1}".format(mut.CHARSET_KEY, 
                                                            CHARSET)}

class TestViews(TestCase):
    
    @mock.patch("pwc.views.time.sleep")
    @mock.patch("pwc.views.requests")
    def test_make_request(self, m_requests, m_sleep):
        """Make a simple request."""
        request = testing.DummyRequest({mut.URL_KEY: SAMPLE_URL})
        m_response = mock.Mock()
        m_requests.get.return_value = m_response
        m_response.status_code = SAMPLE_STATUS
        m_response.headers = SAMPLE_HEADERS
        m_response.content = SAMPLE_BODY
        self.assertEqual({"status": SAMPLE_STATUS, "headers": SAMPLE_HEADERS,
                          "body": SAMPLE_BODY}, 
                         mut.make_request(request))
        m_requests.get.assert_called_with(SAMPLE_URL)
        m_sleep.assert_called_with(mut.SECURITY_SLEEP)
        
        
    @mock.patch("pwc.views.time.sleep")
    @mock.patch("pwc.views.requests")
    def test_make_request_charset(self, m_requests, m_sleep):
        """Make a request with a specific character set in the response."""
        request = testing.DummyRequest({mut.URL_KEY: SAMPLE_URL})
        m_response = mock.Mock()
        m_requests.get.return_value = m_response
        m_response.status_code = SAMPLE_STATUS
        m_response.headers = CHARSET_HEADERS
        m_response.content = mock.Mock()
        m_response.content.decode.return_value = SAMPLE_BODY
        self.assertEqual({"status": SAMPLE_STATUS, "headers": CHARSET_HEADERS,
                          "body": SAMPLE_BODY}, 
                         mut.make_request(request))
        m_requests.get.assert_called_with(SAMPLE_URL)
        m_response.content.decode.assert_called_with(CHARSET)
        m_sleep.assert_called_with(mut.SECURITY_SLEEP)
        
        
    @mock.patch("pwc.views.time.sleep")
    @mock.patch("pwc.views.requests")
    def test_make_request_method(self, m_requests, m_sleep):
        """Make a request using an alternate http method."""
        request = testing.DummyRequest({mut.URL_KEY: SAMPLE_URL, 
                                        mut.METHOD_KEY: SAMPLE_METHOD})
        m_response = mock.Mock()
        m_requests.post.return_value = m_response
        m_response.status_code = SAMPLE_STATUS
        m_response.headers = SAMPLE_HEADERS
        m_response.content = SAMPLE_BODY
        self.assertEqual({"status": SAMPLE_STATUS, "headers": SAMPLE_HEADERS,
                          "body": SAMPLE_BODY}, 
                         mut.make_request(request))
        m_requests.post.assert_called_with(SAMPLE_URL)
        m_sleep.assert_called_with(mut.SECURITY_SLEEP)
        
        
    @mock.patch("pwc.views.time.sleep")
    @mock.patch("pwc.views.requests")
    def test_make_request_invalid_method(self, m_requests, m_sleep):
        """Make a request using an invalid http method."""
        request = testing.DummyRequest({mut.URL_KEY: SAMPLE_URL, 
                                        mut.METHOD_KEY: INVALID_METHOD})
        try:
            mut.make_request(request)
            self.fail("Should have raised KeyError.")
        except KeyError as e:
            self.assertEquals(mut.INVALID_METHOD, e.args[0])
