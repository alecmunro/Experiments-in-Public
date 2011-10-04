from pwc.tests.echo_server import EchoServer, DEFAULT_ADDRESS

SAMPLE_URL = "http://{0}:{1}/anything".format(*DEFAULT_ADDRESS)
SAMPLE_STATUS = 302
SAMPLE_HEADERS = {"heya": "hoya"}
SAMPLE_BODY = "Jimmy Hoffa's"

def setUp(self):
    """Create an echo server, used by API and UI tests."""
    self.test_server = EchoServer(DEFAULT_ADDRESS)
    self.test_server.set_echo(SAMPLE_STATUS, SAMPLE_HEADERS, SAMPLE_BODY)
    self.test_server.threaded_serve()
    
def tearDown(self):
    """Shutdown the echo server."""
    self.test_server.threaded_shutdown()