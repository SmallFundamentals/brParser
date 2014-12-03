import requests
import constants

from bs4 import BeautifulSoup

def get_soup(url):
    try:
        doc = requests.get(url)
        return BeautifulSoup(doc.text)
    except:
        return None

def search_player(player_name, recent=True):
	soup = get_soup(constants.SERVER_NAME + "/players/%s/" \
	    % get_last_initial(player_name).lower())
	if not soup:
		return None
	results = [link.get('href') for link in soup.find_all('a') if player_name in link]
	if len(results) == 0:
		return None
	elif len(results) > 1:
		# TODO: Improve ambiguity logic
		if recent:
			return get_soup(constants.SERVER_NAME + results[-1])
	return get_soup(constants.SERVER_NAME + results[0])

def get_player_page_table_header(table):
	soup = search_player(constants.TIMMY)
	headers = soup.find(id=constants.ID_PREFIX_PER_GAME) \
		.find("thead") \
		.find("tr") \
		.find_all("th")
	return [header.string for header in headers]

def get_per_game_stats_by_player_season(player_name, season):
	proper_season = get_proper_season(season)
	soup = search_player(player_name)
	return soup.find(id=constants.ID_PREFIX_PER_GAME + "." + str(proper_season))

def get_last_initial(player_name):
	return player_name.split()[-1][0]

def get_proper_season(season):
	splitted = season.split("-")
	if len(splitted) == 1:
		if not splitted[0]:
			return None
		return int(splitted[0])
	else:
		season = int("19%s" % splitted[1])
		if season < constants.INAUGURAL_SEASON:
			return int("20%s" % splitted[1])
		else:
			return season
			
	