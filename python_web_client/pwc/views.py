'''
Created on 2011-09-20

@author: Alec
'''
import time

import requests

URL_KEY = "url"
METHOD_KEY = "method"
CONTENT_TYPE_HEADER = "content-type"
CHARSET_KEY = "charset="

#Errors
INVALID_METHOD = "You have specified an invalid method." 

DEFAULT_METHOD = "GET"

VALID_METHODS = (DEFAULT_METHOD, "POST", "PUT", "PATCH", "DELETE")

SECURITY_SLEEP = 0.5

def index(request):
    return {'project':'Python Web Client', 'methods': VALID_METHODS}

def make_request(request):
    """Accepts a request object, which is expected to have a 'url' parameter.
    If the request has a 'method' parameter, and that parameter matches a known
    http method type, it will make that type of request to the 'url'. If 
    'method' is not provided, GET will be used to make the request.
    It will  return the status code and headers from the response."""
    method = request.params.get(METHOD_KEY, DEFAULT_METHOD)
    if not method in VALID_METHODS:
        raise KeyError(INVALID_METHOD)
    response = getattr(requests, method.lower())(request.params[URL_KEY])
    try:
        charset = response.headers[CONTENT_TYPE_HEADER].split(CHARSET_KEY)[1]
        body = response.content.decode(charset)
    except (KeyError, IndexError, AttributeError) as e:
        body = response.content
    time.sleep(SECURITY_SLEEP)
    #I could also write a json convertor for Response objects?
    return {"status": response.status_code, "headers": response.headers,
            "body": body}