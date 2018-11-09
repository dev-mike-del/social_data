#!/usr/bin/env python
import requests
from requests_oauthlib import OAuth1

import keys_and_tokens

consumer_key = keys_and_tokens.consumer_key
consumer_secret = keys_and_tokens.consumer_secret
access_token = keys_and_tokens.access_token
access_token_secret = keys_and_tokens.access_token_secret

verify_credentials_url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

auth = OAuth1(consumer_key, consumer_secret,
	access_token, access_token_secret)

requests.get(verify_credentials_url, auth=auth)