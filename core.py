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
	headers = soup.find(id=table) \
		.find("thead") \
		.find("tr") \
		.find_all("th")
	return [asciify_string(header.string) for header in headers if header.string]

def get_stats_by_player_season(player_name, season, table):
	proper_season = get_proper_season(season)
	soup = search_player(player_name)
	stats = soup.find(id=constants.ID_PREFIX_PER_GAME + "." + str(proper_season)) \
		.find_all("td")
	ret = [] 
	for cat in stats:
		if cat.find("a") and cat.find("a").string:
			el = cat.find("a").string
		else:
			el = cat.string
		ret.append(asciify_string(el))
	return ret

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
		
def asciify_string(string):
	if string:
		return string.encode("ascii", "replace")
	else:
		return None