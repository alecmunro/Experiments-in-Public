'''
Created on 2011-09-20

@author: Alec
'''
import requests

URL_KEY = "url"

def index(request):
    return {'project':'Python Web Client'}

def make_request(request):
    response = requests.get(request.params[URL_KEY])
    #I could also write a json convertor for Response objects?
    return {"status": response.status_code, "headers": response.headers}