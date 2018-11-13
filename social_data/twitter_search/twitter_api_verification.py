#!/usr/bin/env python

import requests
from requests_oauthlib import OAuth1

from .keys_and_tokens import (
	consumer_key,consumer_secret,access_token,access_token_secret,
)

consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret

verify_credentials_url = '''
https://api.twitter.com/1.1/account/verify_credentials.json'''

auth = OAuth1(consumer_key, consumer_secret,
	access_token, access_token_secret)

requests.get(verify_credentials_url, auth=auth)
