'''
Created on 2011-09-20

@author: Alec
'''
import time

import requests

URL_KEY = "url"

def index(request):
    return {'project':'Python Web Client'}

def make_request(request):
    """Accepts a request object, which is expected to have a 'url' parameter.
    It will make a GET request to that URL, and return the status code and 
    headers from the response."""
    response = requests.get(request.params[URL_KEY])
    time.sleep(0.5)
    #I could also write a json convertor for Response objects?
    return {"status": response.status_code, "headers": response.headers}