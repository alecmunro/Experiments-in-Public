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

class TestViews(TestCase):
    
    @mock.patch("pwc.views.requests")
    def test_make_request(self, m_requests):
        request = testing.DummyRequest({mut.URL_KEY: SAMPLE_URL})
        m_response = mock.Mock
        m_requests.get.return_value = m_response
        m_response.status_code = SAMPLE_STATUS
        m_response.headers = SAMPLE_HEADERS
        self.assertEqual((SAMPLE_STATUS, SAMPLE_HEADERS), 
                         mut.make_request(request))
        m_requests.get.assert_called_with(SAMPLE_URL)