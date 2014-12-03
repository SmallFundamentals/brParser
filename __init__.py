import core
import constants
import reddit_wrapper

def main():
	header = core.get_player_page_table_header(constants.ID_PREFIX_PER_GAME)
	stat = core.get_stats_by_player_season("Tim Duncan", "1998", constants.ID_PREFIX_PER_GAME)
	stat1 = core.get_stats_by_player_season("Tim Duncan", "2014", constants.ID_PREFIX_PER_GAME)
	stat2 = core.get_stats_by_player_season("Tim Duncan", "2013", constants.ID_PREFIX_PER_GAME)
	stat3 = core.get_stats_by_player_season("Tim Duncan", "2011", constants.ID_PREFIX_PER_GAME)

	print reddit_wrapper.build_table(header, [stat, stat1, stat2, stat3])

main() 
