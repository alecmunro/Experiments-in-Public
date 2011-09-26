'''
Created on 2011-09-22

@author: Alec
'''
from unittest import TestCase

import mock

from pwc.tests import echo_server as mut

SAMPLE_STATUS = 302
SAMPLE_HEADERS = {"Why?": "Not!"}
SAMPLE_BODY = "Abracadabra"

class TestEchoServer(TestCase):
    
    
    def test_default_echo(self):
        """Confirm the behaviour of the default echo."""
        server = mut.EchoServer(mut.DEFAULT_ADDRESS)
        
        m_handler_instance = mock.Mock(spec=server.RequestHandlerClass)
        m_handler_instance.wfile = mock.Mock()
        
        server.RequestHandlerClass.do_GET(m_handler_instance)
        m_handler_instance.send_response.assert_called_once_with(
                                                             mut.DEFAULT_STATUS)
        for key, value in mut.DEFAULT_HEADERS.items():
            m_handler_instance.send_header.assert_called_once_with(key, value)
        m_handler_instance.end_headers.assert_called_once_with()
        m_handler_instance.wfile.write.assert_called_once_with(mut.DEFAULT_BODY)
    
    
    def test_set_echo(self):
        """Set the echo details for the server."""
        server = mut.EchoServer(mut.DEFAULT_ADDRESS)
        server.set_echo(SAMPLE_STATUS, SAMPLE_HEADERS, SAMPLE_BODY)
        
        m_handler_instance = mock.Mock(spec=server.RequestHandlerClass)
        m_handler_instance.wfile = mock.Mock()
        
        server.RequestHandlerClass.do_GET(m_handler_instance)
        m_handler_instance.send_response.assert_called_once_with(SAMPLE_STATUS)
        for key, value in SAMPLE_HEADERS.items():
            m_handler_instance.send_header.assert_called_once_with(key, value)
        m_handler_instance.end_headers.assert_called_once_with()
        m_handler_instance.wfile.write.assert_called_once_with(SAMPLE_BODY)