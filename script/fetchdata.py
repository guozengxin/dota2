#!/usr/bin/env python
#encoding=utf-8

import apiadapter
import simplejson
import time

KEY = '3103AA4F6DED20345780558E594BAC3D'

def jsonparse(jsondata):
	jsonobj = simplejson.loads(jsondata)
	result = jsonobj['result']
	num = result['num_results']
	matches = result['matches']
	ids = []
	for match in matches:
		ids.append(match['match_id'])
	data = simplejson.dumps(matches, indent=2)
	data = data + ','
	return (num, ids, data)

def main():
	now = int(time.time())
	begin = now - 86400 * 30
	args = {
			#'game_mode': 1,
			#'min_players': '10',
			'date_min': begin,
			}
	data = apiadapter.GetMatchHistory(KEY, args)
	(num, ids, data) = jsonparse(data)
	while num > 0 and len(ids) > 0:
		start_at_match_id = ids[-1]
		args = {
				#'game_mode': 1,
				#'min_players': '10',
			'date_min': begin,
			'start_at_match_id': start_at_match_id
				}
		data = apiadapter.GetMatchHistory(KEY, args)
		(num, ids, data) = jsonparse(data)
		for match_id in ids:
			data = apiadapter.GetMatchDetails(KEY, match_id)
			print data
			break

def test_seq():
	begin = time.strptime('2014-01-01 14:00:00', '%Y-%m-%d %H:%M:%S')
	args = {
			'game_mode': 1,
			'min_players': '10',
			'date_min': begin,
			}
	data = apiadapter.GetMatchHistoryBySequenceNum(KEY, start_at_match_seq_num=414730006)
	print data

if __name__ == '__main__':
	main()
	#test_seq()
