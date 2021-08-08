import requests
import json
import sys

try:
	_user_search = input(" Search YTS (YIFI) Movie : ")
	_api = (f"https://yts.mx/api/v2/list_movies.json?limit=50&query_term={_user_input}")
	_search_data = requests.get(_api).json()

	_movie_count = _data['data']['movie_count']
	_count = 0
	_index_ = 1
	print("\n ------------------------------------------------------------------------------------------ ")

	if _movie_count == 0:
		print("                  : 0 YIFY Movies Found! :( Try Using Different Keywords :")
		print(" ------------------------------------------------------------------------------------------ ")
		sys.exit()

	else:
		for mx in range(_movie_count):
			_index_ = str(_index_)
			_index_ = _index_.zfill(2)
			print(f" : {_index_} : " + _data['data']['movies'][_count]['title_long'])
			print(" ------------------------------------------------------------------------------------------ ")
			_count+=1
			_index_ = int(_index_)
			_index_+=1

		_movie_number = int(input("\n Enter Movie Number : "))
		_movie_id = (_movie_number - 1)
		print(_data['data']['movies'][_movie_id]['url'])

except requests.exceptions.ConnectionError as _network_failure:
	print("\n ConnectionError...")

