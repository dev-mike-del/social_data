#!/usr/bin/env python

import requests

from .twitter_api_verification import auth

def search_twitter_profile_followers(screen_name=False):
	if screen_name is not False:
		cursor = "-1"
		id_results = {}
		while cursor:
			id_search_url = (
				'https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name={}&count=5000&cursor={}'.format(
					screen_name,
					cursor,
					)
				)
			id_results_set = requests.get(id_search_url, auth=auth).json()

			id_results.update(id_results_set)

			try:
				if id_results_set["next_cursor"]:
					cursor = id_results_set["next_cursor_str"]
			except KeyError:
				cursor = False
		print(id_results)

		try:
			if id_results["errors"]:
				print('''
Twitter Handle: {}
Twitter API Response: {}
***The Twitter API responded with an error for {}.
***Check the spelling to ensure accuracy.
***Do not include an "@" at the begining of the Twitter handle
'''.format(screen_name, id_results["errors"][0]["message"],screen_name))
				return id_results
		except KeyError:
			ids = id_results["ids"]
			number_of_ids = len(ids)
			user_lookup_results = []

			while number_of_ids >= 1:
				set_of_ids = ids[:100]
				del ids[:100]
				number_of_ids = number_of_ids - 100
				user_lookup_search_url = (
				'https://api.twitter.com/1.1/users/lookup.json?user_id={}'.format(
					"".join(str(set_of_ids))[1:-1],
					)
				)

				user_lookup_results += requests.get(user_lookup_search_url,auth=auth).json()

	else:
		pass


if __name__ == "__main__":
	search_twitter_profile_followers("dev_mike_del")

