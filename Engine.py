import re
import os
import sys
import time
import json
import requests
from bs4 import BeautifulSoup
from msvcrt import getch as _pause_

while True:
	while True:
		try:
			_user_search = input("\n Search YTS (YIFI) Movie : ")
			if _user_search == "":
				print("\n Invalid Input...")
				time.sleep(1)
				sys.exit()
			_api = # Source Code is Available Separately
			_search_data = requests.get(_api).json()
			
			_movie_count = _search_data['data']['movie_count']
			_count = 0
			_index_ = 1

			if _movie_count >= 51:
				_api_2 = # Source Code is Available Separately
				_search_data_2 = requests.get(_api_2).json()
				_movie_count_2 = len(_search_data_2['data']['movies'])
				f = 0
				for z in range(_movie_count_2):
					_search_data['data']['movies'].append(_search_data_2['data']['movies'][f])
					f+=1
					

			print("\n ------------------------------------------------------------------------------------------ ")

			if _movie_count == 0:
				print("                  : 0 YIFY Movies Found! :( Try Using Different Keywords :")
				print(" ------------------------------------------------------------------------------------------ ")
				time.sleep(1)
				_pause_()
				os.system("cls")
				continue


			else:
				for mx in range(_movie_count):
					_index_ = str(_index_)
					_index_ = _index_.zfill(2)
					print(f" : {_index_} : " + _search_data['data']['movies'][_count]['title_long'])
					print(" ------------------------------------------------------------------------------------------ ")
					_count+=1
					_index_ = int(_index_)
					_index_+=1

				try:
					_movie_number = int(input("\n Enter Movie Number : "))
					if _movie_number >= (_movie_count+1):
						print("\n Invalid Input...")
						_pause_()
						time.sleep(1.5)
						sys.exit()
				except Exception as _string_error:
					print("\n Invalid Input...")
					_pause_()
					time.sleep(1.5)
					sys.exit()

				_movie_id = (_movie_number - 1)
				_url = (_search_data['data']['movies'][_movie_id]['url'])

			_url_ = re.match(r'^(https:|)[/][/]yts([.])*mx[/]movies[/]', _url)
			break
		except requests.exceptions.ConnectionError as _network_failure:
			print("\n ConnectionError...")
			time.sleep(2.5)
			sys.exit()

	try:
		if _url_:

			req = requests.get(_url).content.decode("utf-8")

			_main_data_ = [] 
			_modified_webdata_ = [] 
			_extracted_textdata_ = [] 
			_file_size_data_ = []
			_file_size_packets_ = []
			_mobile_movie_data = []
			_seen_1 = set()
			_result_1 = []  
			_seen_2 = set()
			_result_2 = []

			soup = BeautifulSoup(req, features="html5lib")

			for _movie_name_ in soup.find_all('h1', {'itemprop': "name"}):
				_name_tag_ = _movie_name_.text

			for _movie_data_ in soup.find_all('div', {'id': "mobile-movie-info"}):
				_mobile_movie_data = _movie_data_.text.split("\n")

			if len(_mobile_movie_data) == 0:
				print("\n Error! Not Found (This Movie does not Exist in our Domain!)")
				_pause_()
				time.sleep(2.5)
				sys.exit()
			del _mobile_movie_data[0]
			del	_mobile_movie_data[-1]

			for _element_ in soup.find_all('a', {'rel': "nofollow"}):
				_main_data_.append(_element_['href'])
				for _item_ in _main_data_:
					_link_ = re.match(r'^(magnet):[?]', _item_)
					if _link_:
						_modified_webdata_.append(_item_)
						_quality_ = re.match(r'^(720p|1080p|2160p|3D)[.](WEB|BluRay)', _element_.text)
						if _quality_:
							_extracted_textdata_.append(_element_.text)

			for _file_size_ in soup.find_all('div', {'class': "tech-spec-element col-xs-20 col-sm-10 col-md-5"}):
				_file_size_data_.append(_file_size_.text)

			for _size_packet_ in _file_size_data_:
				_size_ = re.match(r"^([ ][0-9]+)|[.]([0-9]+)|[ ](MB|GB)", _size_packet_)
				if _size_:
					_file_size_packets_.append(_size_packet_)

			for _y_ in _extracted_textdata_:
				if _y_ not in _seen_2:
					_seen_2.add(_y_)
					_result_2.append(_y_)

			for _x_ in _modified_webdata_:
				if _x_ not in _seen_1:
					_split_ = _x_.split("&")
					_seen_1.add(_x_)
					_result_1.append(_split_[0])
			os.system("cls")
			print("\n ------------------------------------------------------------------------------------------ ")
			print(f" : Movie  : {_mobile_movie_data[0]} ({_mobile_movie_data[1]}) IMDb : [{_search_data['data']['movies'][_movie_id]['rating']}/10] Runtime : {_search_data['data']['movies'][_movie_id]['runtime']} Min")
			print(f" : Genres : {_mobile_movie_data[2]}")
			print(" ------------------------------------------------------------------------------------------ ")

			for _xy_ in range(len(_result_1)):
				print(f" : {_result_1[_xy_]}  :  {_result_2[_xy_]}{_file_size_packets_[_xy_]}")
				print(" ------------------------------------------------------------------------------------------ ")


			print("\n Success...")
			time.sleep(1)
			_pause_()
			os.system("cls")

		else:
			print("\nLink not related with [ YTS.mx] Domain!")
			break

	except requests.exceptions.ConnectionError as _network_failure:
		print("\n ConnectionError...")
		time.sleep(2.5)
		sys.exit()

	except KeyboardInterrupt as _user_block:
		print("\n Programe Interrupted...")
		time.sleep(2.5)
		sys.exit()

	except Exception as Identifier:
		print("\n Programe Interrupted...")
		time.sleep(2.5)
		sys.exit()
  
print("\nExiting...")
time.sleep(1)
