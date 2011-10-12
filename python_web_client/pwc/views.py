'''
Created on 2011-09-20

@author: Alec
'''
import time
import json

import requests

URL_KEY = "url"
METHOD_KEY = "method"
PARAMETERS_KEY = "parameters"
CONTENT_TYPE_HEADER = "content-type"
CHARSET_KEY = "charset="
HEADERS_KEY = "headers"
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
    
    If the request has a 'params' parameter, it will be treated as a 
    json-encoded dictionary and used as the parameters for the new request.
    
    If the request has a 'headers' parameter, it will be treated as a 
    json-encoded dictionary and used as the headers for the new request.
    
    Returns the status code, headers and body from the response, as a 
    dictionary."""
    method_args = {"url": request.params[URL_KEY]}
    if PARAMETERS_KEY in request.params:
        method_args["params"] = json.loads(request.params[PARAMETERS_KEY])
    if HEADERS_KEY in request.params:
        method_args["headers"] = json.loads(request.params[HEADERS_KEY])
    method = request.params.get(METHOD_KEY, DEFAULT_METHOD)
    if not method in VALID_METHODS:
        raise KeyError(INVALID_METHOD)
    response = getattr(requests, method.lower())(**method_args)
    try:
        charset = response.headers[CONTENT_TYPE_HEADER].split(CHARSET_KEY)[1]
        body = response.content.decode(charset)
    except (KeyError, IndexError, AttributeError) as e:
        body = response.content
    time.sleep(SECURITY_SLEEP)
    #I could also write a json convertor for Response objects?
    return {"status": response.status_code, "headers": response.headers,
            "body": body}