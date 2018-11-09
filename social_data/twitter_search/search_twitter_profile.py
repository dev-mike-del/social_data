#!/usr/bin/env python

import json
import requests

from twitter_api_verification import auth

def search_twitter_profile(screen_name=False):
	if screen_name:
		search_url = (
			'https://api.twitter.com/1.1/users/show.json?screen_name={}'.format(
				screen_name
				)
			)

		results = requests.get(search_url, auth=auth).json()

		try:
			if results["errors"]:
				print('''
Twitter Handle: {}
Twitter API Response: {}

***The Twitter API responded with an error for {}.
***Check the spelling to ensure accuracy.
***Do not include an "@" at the begining of the Twitter handle
'''.format(screen_name, results["errors"][0]["message"],screen_name))
		except Exception:
			raise Exception
		finally:
			return results
	else:
		print("You did not enter a Twitter handle. Please try again.")


if __name__ == "__main__":
	search_twitter_profile("dev_mike_del")

