'''
Created on 2011-09-20

@author: Alec
'''
import requests

URL_KEY = "url"

def make_request(request):
    response = requests.get(request.params[URL_KEY])
    return (response.status_code, response.headers)