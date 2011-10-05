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

CHARSET = "Gracelandish"
CHARSET_HEADERS = {mut.CONTENT_TYPE_HEADER: "{0}{1}".format(mut.CHARSET_KEY, 
                                                            CHARSET)}

class TestViews(TestCase):
    
    @mock.patch("pwc.views.requests")
    def test_make_request(self, m_requests):
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
        
        
    @mock.patch("pwc.views.requests")
    def test_make_request_charset(self, m_requests):
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