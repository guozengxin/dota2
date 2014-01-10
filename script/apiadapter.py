#!/usr/bin/env python
#encoding=utf-8

import urllib2
import urllib

def fetch(url, args):
	url = url + '?' + urllib.urlencode(args)
	request = urllib2.Request(url)
	request.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/30.0.1599.114 Chrome/30.0.1599.114')
	response = urllib2.urlopen(request)
	data = response.read()
	return data

def GetLeagueListing(key, language=''):
	url = 'http://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/v1/'
	args = {'key':key, 'language':language}
	return fetch(url, args)

def GetLiveLeagueGames(key):
	url = 'http://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v1/'
	args = {'key':key}
	return fetch(url, args)

def GetMatchDetails(key, match_id=''):
	url = 'http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1'
	args = {'key': key, 'match_id': match_id}
	return fetch(url, args)

def GetMatchHistory(key, args):
	'''
	args:
	player_name (Optional) (string)
		Exact match of a player's display-name at the time of the match.
	hero_id (Optional) (uint32)
		A list of hero IDs can be found via the GetHeroes method.
	game_mode (Optional) (uint32)
		0 - None
		1 - All Pick
		2 - Captain's Mode
		3 - Random Draft
		4 - Single Draft
		5 - All Random
		6 - Intro
		7 - Diretide
		8 - Reverse Captain's Mode
		9 - The Greeviling
		10 - Tutorial
		11 - Mid Only
		12 - Least Played
		13 - New Player Pool
		14 - Compendium Matchmaking
		16 - Captain's Draft
	skill (Optional) (uint32)
		Skill bracket for the matches (Ignored if an account ID is specified).
		0 - Any
		1 - Normal
		2 - High
		3 - Very High
	date_min (Optional) (uint32)
		Minimum date range for returned matches (unix timestamp, rounded to the nearest day).
	date_max (Optional) (uint32)
		Maximum date range for returned matches (unix timestamp, rounded to the nearest day).
	min_players (Optional) (string)
		Minimum amount of players in a match for the match to be returned.
	account_id (Optional) (string)
		32-bit account ID.
	league_id (Optional) (string)
		Only return matches from this league. A list of league IDs can be found via the GetLeagueListing method.
	start_at_match_id (Optional) (string)
		Start searching for matches equal to or older than this match ID.
	matches_requested (Optional) (string)
		Amount of matches to include in results (default: 25).
	tournament_games_only (Optional) (string)
		Whether to limit results to tournament matches.

	Result:
	status
		1 - Success
		15 - Cannot get match history for a user that hasn't allowed it.
	statusDetail
		A message explaining the status, should status not be 1.
	num_results
		The number of matches in this response.
	total_results
		The total number of matches for the query.
	results_remaining
		The number of matches left for this query.
	matches
		A list of matches.
		match_id
			The matches unique ID.
		match_seq_num
			A 'sequence number', representing the order in which matches were recorded.
		start_time
			Unix timestamp of when the match began.
		lobby_type
			-1 - Invalid
			0 - Public matchmaking
			1 - Practise
			2 - Tournament
			3 - Tutorial
			4 - Co-op with bots.
			5 - Team match
			6 - Solo Queue
		players
			The list of players within the match.
			account_id
				32-bit account ID.
			player_slot
				See #Player Slot below.
			hero_id
				The hero's unique ID. A list of hero IDs can be found via the GetHeroes method.
		Player Slot
		A player's slot is returned via an 8-bit unsigned integer. The first bit represent the player's team, false if Radiant and true if dire. The final three bits represent the player's position in that team, from 0-4.
			┌─────────────── Team (false if Radiant, true if Dire).
			│ ┌─┬─┬─┬─────── Not used.
			│ │ │ │ │ ┌─┬─┬─ The position of a player within their team (0-4).
			│ │ │ │ │ │ │ │
			0 0 0 0 0 0 0 0
	'''
	url = 'http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1'
	args.update({'key':key})
	return fetch(url, args)

def GetMatchHistoryBySequenceNum(key, start_at_match_seq_num=-1, matches_requested=-1):
	'''
	result
		status
			1 - Success
			8 - 'matches_requested' must be greater than 0.
		statusDetail
			A message explaining the status, should status not be 1.
		matches
			A list of matches.
			players
				The list of players within the match.
			account_id
				32-bit account ID.
			player_slot
				See #Player Slot below.
			hero_id
				The hero's unique ID. A list of hero IDs can be found via the GetHeroes method.
			item_0
				ID of the top-left inventory item.
			item_1
				ID of the top-center inventory item.
			item_2
				ID of the top-right inventory item.
			item_3
				ID of the bottom-left inventory item.
			item_4
				ID of the bottom-center inventory item.
			item_5
				ID of the bottom-right inventory item.
			kills
				The amount of kills attributed to this player.
			deaths
				The amount of times this player died during the match.
			assists
				The amount of assists attributed to this player.
			leaver_status
				What the values here represent are not yet known.
			gold
				The amount of gold the player had remaining at the end of the match.
			last_hits
				The amount of last-hits the player got during the match.
			denies
				The amount of denies the player got during the match.
			gold_per_min
				The player's overall gold/minute.
			xp_per_min
				The player's overall experience/minute.
			gold_spent
				The amount of gold the player spent during the match.
			hero_damage
				The amount of damage the player dealt to heroes.
			tower_damage
				The amount of damage the player dealt to towers.
			hero_healing
				The amount of health the player had healed on heroes.
			level
				The player's level at match end.
		season
			The season the game was played in.
		radiant_win
			Dictates the winner of the match, true for radiant; false for dire.
		duration
			The length of the match, in seconds since the match began.
		start_time
			Unix timestamp of when the match began.
		match_id
			The matches unique ID.
		match_seq_num
			A 'sequence number', representing the order in which matches were recorded.
		tower_status_radiant
			See #Tower Status below.
		tower_status_dire
			See #Tower Status below.
		barracks_status_radiant
			See #Barracks Status below.
		barracks_status_dire
			See #Barracks Status below.
		cluster
			The server cluster the match was played upon. Used for downloading replays of matches.
		first_blood_time
			The time in seconds since the match began when first-blood occured.
		lobby_type
			-1 - Invalid
			0 - Public matchmaking
			1 - Practise
			2 - Tournament
			3 - Tutorial
			4 - Co-op with bots.
			5 - Team match
		human_players
			The amount of human players within the match.
		leagueid
			The league that this match was a part of. A list of league IDs can be found via the GetLeagueListing method.
		positive_votes
			The number of thumbs-up the game has received by users.
		negative_votes
			The number of thumbs-down the game has received by users.
		game_mode
			0 - All Pick
			1 - Single Draft
			2 - All Random
			3 - Random Draft
			4 - Captain's Draft
			5 - Captain's Mode
			6 - Death Mode
			7 - Diretide
			8 - Reverse Captain's Mode
			9 - The Greeviling
			10 - Tutorial
			11 - Mid Only
			12 - Least Played
			13 - New Player Pool
		picks_bans
			A list of the picks and bans in the match, if the game mode is Captains Mode.
		is_pick
			Whether this entry is a pick (true) or a ban (false).
		hero_id
			The hero's unique ID. A list of hero IDs can be found via the GetHeroes method.
		team
			The team who chose the pick or ban; 0 for Radiant, 1 for Dire.
		order
			The order of which the picks and bans were selected; 0-19.

		Player Slot
		A player's slot is returned via an 8-bit unsigned integer. The first bit represent the player's team, false if Radiant and true if dire. The final three bits represent the player's position in that team, from 0-4.
			┌─────────────── Team (false if Radiant, true if Dire).
			│ ┌─┬─┬─┬─────── Not used.
			│ │ │ │ │ ┌─┬─┬─ The position of a player within their team (0-4).
			│ │ │ │ │ │ │ │
			0 0 0 0 0 0 0 0
		Tower Status
		A particular teams tower status is given as a 16-bit unsigned integer. The rightmost 11 bits represent individual towers belonging to that team; see below for a visual representation.
			┌─┬─┬─┬─┬─────────────────────── Not used.
			│ │ │ │ │ ┌───────────────────── Ancient Top
			│ │ │ │ │ │ ┌─────────────────── Ancient Bottom
			│ │ │ │ │ │ │ ┌───────────────── Bottom Tier 3
			│ │ │ │ │ │ │ │ ┌─────────────── Bottom Tier 2
			│ │ │ │ │ │ │ │ │ ┌───────────── Bottom Tier 1
			│ │ │ │ │ │ │ │ │ │ ┌─────────── Middle Tier 3
			│ │ │ │ │ │ │ │ │ │ │ ┌───────── Middle Tier 2
			│ │ │ │ │ │ │ │ │ │ │ │ ┌─────── Middle Tier 1
			│ │ │ │ │ │ │ │ │ │ │ │ │ ┌───── Top Tier 3
			│ │ │ │ │ │ │ │ │ │ │ │ │ │ ┌─── Top Tier 2
			│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ ┌─ Top Tier 1
			│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │
			0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		Barracks Status
		A particular teams tower status is given as an 8-bit unsigned integer. The rightmost 6 bits represent the barracks belonging to that team; see below for a visual representation.
			┌─┬───────────── Not used.
			│ │ ┌─────────── Bottom Ranged
			│ │ │ ┌───────── Bottom Melee
			│ │ │ │ ┌─────── Middle Ranged
			│ │ │ │ │ ┌───── Middle Melee
			│ │ │ │ │ │ ┌─── Top Ranged
			│ │ │ │ │ │ │ ┌─ Top Melee
			│ │ │ │ │ │ │ │
			0 0 0 0 0 0 0 0
		Player Slot
		A player's slot is returned via an 8-bit unsigned integer. The first bit represent the player's team, false if Radiant and true if dire. The final three bits represent the player's position in that team, from 0-4.
			┌─────────────── Team (false if Radiant, true if Dire).
			│ ┌─┬─┬─┬─────── Not used.
			│ │ │ │ │ ┌─┬─┬─ The position of a player within their team (0-4).
			│ │ │ │ │ │ │ │
			0 0 0 0 0 0 0 0
	'''
	url = 'http://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v1'
	#args = {'key': key, 'tart_at_match_seq_num': start_at_match_seq_num, 'matches_requested': matches_requested}
	args = {'key': key}
	if start_at_match_seq_num != -1:
		args.update({'start_at_match_seq_num':start_at_match_seq_num})
	if matches_requested != -1:
		args.update({'matches_requested': matches_requested})
	return fetch(url, args)

def GetScheduledLeagueGames(key, date_min=-1, date_max=-1):
	'''
	result
		league_id
			Unique ID for the league of the match being played. A list of league IDs can be found via the GetLeagueListing method.
		game_id
			Unique ID of the game scheduled.
		teams
			List of participating teams; empty if not known.
		team_id
			team_name
		team_logo
			The UGC id for the team logo. You can resolve this with the GetUGCFileDetails method.
		starttime
			Unix timestamp.
		comment
			Description of the game.
		final
			Whether the game is a final or not.
	'''
	url = 'http://api.steampowered.com/IDOTA2Match_570/GetScheduledLeagueGames/v1/'
	args = {'key': key}
	if date_min != -1:
		args.update({'date_min': date_min})
	if date_max != -1:
		args.update({'date_max': date_max})
	return fetch(url, args)

def GetTeamInfoByTeamID(key, start_at_team_id=-1, teams_requested=-1):
	'''
	result
		status
			1 - Success
			8 - 'teams_requested' must be greater than 0.
		statusDetail
			A message explaining the status, should status not be 1.
		teams
			A list of teams.
		team_id
			The team's unique id.
		name
			The team's name.
		tag
			The team's tag.
		time_created
			Unix timestamp of when the team was created.
		rating
		logo
			The UGC id for the team logo. You can resolve this with the GetUGCFileDetails method.
		logo_sponsor
			The UGC id for the team sponsor logo. You can resolve this with the GetUGCFileDetails method.
		country_code
			The team's ISO 3166-1 country-code.
		url
			The URL the team provided upon creation.
		games_played_with_current_roster
			Amount of matches played with the current roster
		player_N_account_id
			32-bit account ID. Where N is incremental from 0 for every player on the team.
		admin_account_id
			32-bit account ID of the team's admin.
	'''
	url = 'http://api.steampowered.com/IDOTA2Match_570/GetTeamInfoByTeamID/v1'
	args = {'key': key}
	if start_at_team_id != -1:
		args.update({'start_at_team_id':start_at_team_id})
	if teams_requested != -1:
		args.update({'teams_requested':teams_requested})
	return fetch(url, args)

def GetTournamentPlayerStats(key, account_id='', league_id='', hero_id='', time_frame=''):
	'''
	Method-specific parameters
	account_id (string)
		32-bit account ID.
	league_id (Optional) (string)
		A list of league IDs can be found via the GetLeagueListing method. Will return status 8 - only supports tournament 65006 (The International) unless you provide 65006.
	hero_id (Optional) (string)
		A list of hero IDs can be found via the GetHeroes method.
	time_frame (Optional) (string)
		Only return stats between this time frame (parameter format not yet known).

	Result:
		status
			1 - Success
			8 - only supports tournament 65006 (The International).
		statusDetail
			A message explaining the status, should status not be 1.
		num_results
			Number of matches returned.
		matches
			An array of matches.
			player_slot
				See #Player Slot.
			hero_id
				The hero's unique ID. A list of hero IDs can be found via the GetHeroes method.
			item_0
				ID of the top-left inventory item.
			item_1
				ID of the top-center inventory item.
			item_2
				ID of the top-right inventory item.
			item_3
				ID of the bottom-left inventory item.
			item_4
				ID of the bottom-center inventory item.
			item_5
				ID of the bottom-right inventory item.
			kills
				The amount of kills attributed to this player.
			deaths
				The amount of times this player died during the match.
			assists
				The amount of assists attributed to this player.
			gold
				The amount of gold the player had remaining at the end of the match.
			last_hits
				The amount of last-hits the player got during the match.
			denies
				The amount of denies the player got during the match.
			gold_per_min
				The player's overall gold/minute.
			xp_per_min
				The player's overall experience/minute.
			gold_spent
				The amount of gold the player spent during the match.
			level
				The player's level at match end.
			win
				Whether the player won the match or not (values: "true" or "false").
			match_id
				The match's unique ID.
			duration
				The length of the match, in seconds since the match began.
		account_id
			32-bit account ID.
		persona
			Account's current Steam profile name.
		num_results
			Number of matches returned.
		wins
			Number of the matches won.
		losses
			Number of the matches lost.
		kills
			Number of kills across all of the matches.
		deaths
			Number of deaths across all of the matches.
		assists
			Number of assists across all of the matches.
		kills_average
			Average number of kills per match.
		deaths_average
			Average number of deaths per match.
		assists_average
			Average number of assists per match.
		gpm_average
			Average gold per minute across all of the matches.
		xpm_average
			Average experience per minute across all of the matches.
		best_kills
			Most kills in one of the matches.
		best_kills_heroid
			Which Hero the player was playing when they achieved best_kills. A list of hero IDs can be found via the GetHeroes method.
		best_gpm
			Highest gold per minute in one of the matches.
		best_gpm_heroid
			Which Hero the player was playing when they achieved best_gpm. A list of hero IDs can be found via the GetHeroes method.
		heroes_played
			An array of heroes played.
		id
			The hero's unique ID. A list of hero IDs can be found via the GetHeroes method.
		wins
			Number of matches won with this hero.
		losses
			Number of matches lost with this hero.
	'''
	url = 'http://api.steampowered.com/IDOTA2Match_570/GetTournamentPlayerStats/v1'
	args = {'key': key}
	if account_id:
		args.update({'account_id': account_id})
	if league_id:
		args.update({'league_id': league_id})
	if hero_id:
		args.update({'hero_id': hero_id})
	if time_frame:
		args.update({'time_frame': time_frame})
	return fetch(url, args)

def GetRarities(key, language=''):
	'''
	result
		count
			Possible number of rarities. This number appears to be[1] currently incorrect and off by one.
		rarities
			List of rarity objects
			name
				The internal rarity name string.
			id
				ID of rarity, used for indexing.
			order
				Sorting and logical order of rarities, from most distributed to least.
			color
				String of the hexadecimal RGB tuple of the rarity name as it is displayed in-game.
			localized_name
				The localized name of the rarity for use in name display.
	'''
	url = 'http://api.steampowered.com/IEconDOTA2_570/GetRarities/v1'
	args = {'key': key, 'language': language}
	return fetch(url, args)

def GetHeroes(key, language='', itemizedonly=-1):
	'''
	result
		heroes
			List of heroes.
			name
				The tokenized string for the name of the hero.
			id
				ID of the hero.
			localized_name
				The localized name of the hero for use in name display.
		count
			Number of results.
	'''
	url = 'http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1'
	args = {'key': key}
	if language:
		args.update({'language': language})
	if itemizedonly != -1:
		args.update({'itemizedonly': itemizedonly})
	return fetch(url, args)

def GetSupportedAPIList(key):
	'''
	apilist (array)
		interfaces (array)
			name (string)
				Name of Interface.
			methods (array)
				Methods with-in the interface.
				name (string)
					Name of method.
				version (int)
					Version of method.
				httpmethod (string)
					Allowed HTTP method for method (GET, POST).
				parameters (array)
					name (string)
						Name of parameter.
					type (string)
						Expected type of value.
					optional (bool)
						Is input optional for the method.
					description (string)
						API Documentation of parameter.
	'''
	url = 'http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/'
	args = {'key': key}
	return fetch(url, args)

if __name__ == '__main__':
	key = '3103AA4F6DED20345780558E594BAC3D'
	#print GetLeagueListing(key)
	#print GetMatchHistory(key, {})
	#print GetMatchHistoryBySequenceNum(key)
	#print GetScheduledLeagueGames(key)
	#print GetTeamInfoByTeamID(key)
	#print GetRarities(key)
	#print GetHeroes(key, 'zh')
