#!/usr/bin/env python3

# (c) 2021 Backstop Solutions Group, LLC. 
# Licensed under the MIT license: https://opensource.org/licenses/mit-license.php

import argparse
import requests

API_MIME_TYPE = 'application/vnd.api+json'

####

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True, help='Backstop URL')
parser.add_argument('-n', '--username', required=True, help='Backstop username')
parser.add_argument('-t', '--token', required=True, help='Backstop API token')

args = parser.parse_args()

url = args.url
username = args.username
api_token = args.token

response = requests.get(url,
                         auth=(username, api_token),
                         headers={
                             'token': 'true',
                             'Content-Type': API_MIME_TYPE,
                             'Accept': API_MIME_TYPE
                         })

print(response.text)
