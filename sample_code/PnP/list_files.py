#!/usr/bin/env python

import requests
import sys
import json
import os.path, sys
#change path to allow import from parent directory
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from apic import get_auth_token, create_url

def list_files(namespace):
    token = get_auth_token()

    url = create_url(path="file/namespace/%s" % namespace)
    print "Getting %s" % url
    headers= { 'x-auth-token': token['token']}
    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException  as cerror:
        print "Error processing request", cerror
        sys.exit(1)
    return response.json()

if __name__ == "__main__":
    file_response = list_files("config")
    print '{0:30}:{1:15} {2:10}'.format('name','fileFormat','fileSize')
    for project in file_response['response']:
        #print json.dumps(project, indent=2)
        print '{0:30}:{1:15} {2:10}'.format(project['name'], project['fileFormat'], project['fileSize'])