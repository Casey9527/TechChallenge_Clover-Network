
# the python version is: 2.7.6
# usage:
# python imdb.py movie_series_1 movie_series_2 begin_year end_year

import sys
import urllib2
import json
import datetime
from operator import itemgetter

api_key = '7a2fdeeb-1482-44c9-b330-c7155cbd05e8'
base_url = 'http://www.myapifilms.com/tmdb/searchMovie?'

def search_imdb_by_name(name):
	"""
		query IMDB API provided by http://www.myapifilms.com/
		store <release_date, title> in a dict
		store dicts in a list, sorted in descending order
	"""
	movieName = name.replace(' ', '+')	
	final_url = base_url + '&token=' + api_key + '&movieName=' + movieName
	#print final_url
	json_obj = urllib2.urlopen(final_url)
	json_decode = json.load(json_obj)

	results = []
	for item in json_decode["data"]["results"]:
		title_and_date = {}
		title_and_date['title'] = item['title']
		if item['release_date'] != '':
			title_and_date['release_date'] = datetime.datetime.strptime(item['release_date'], '%Y-%m-%d')
		else:
			title_and_date['release_date'] = datetime.datetime(1910,01,01)
		results.append(title_and_date)
	newlist = sorted(results, key = itemgetter('release_date'), reverse = True)
	results = newlist
	#print results
	
	for item in results:
		print '{:80}'.format(item['title']), item['release_date']
	print '*'*100
	print '\n'
	return results


def get_release_velocity(data, begin, end):
	"""
	get the number of movie released between begin date and end date

	"""
	begin_date = datetime.datetime(int(begin)-1, 12, 31)
	end_date = datetime.datetime(int(end), 12, 31)
	firstdate = datetime.datetime(1910, 01, 01)
	lastdate = datetime.datetime(1910, 01, 01)
	count = 0;
	start_index = 0;
	end_index = 0;

	for item in data:
		if item['release_date'] >= begin_date and item['release_date'] <= end_date:
			count += 1
	return count


def main(argv):
	# parse variables from command line
	name_1 = argv[1]
	name_2 = argv[2]
	begin = argv[3]
	end = argv[4]

	result_1 = search_imdb_by_name(name_1)
	result_2 = search_imdb_by_name(name_2)

	num_1 = get_release_velocity(result_1, begin, end)
	num_2 = get_release_velocity(result_2, begin, end)

	print name_1 + ' has released <' + str(num_1) + '> movies from ' + str(begin) + ' to ' + str(end)
	print name_2 + ' has released <' + str(num_2) + '> movies from ' + str(begin) + ' to ' + str(end)

	if num_1 == num_2:
		print name_1 + ' is the same popular as ' + name_2
	elif num_1 > num_2:
		print name_1 + ' is the more popular than ' + name_2
	else:
		print name_1 + ' is the less popular than ' + name_2

	print '\n'

if __name__ == "__main__":
	main(sys.argv)
