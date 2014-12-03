def build_table(header, rows):
	for cat in rows:
		assert(len(header) == len(cat)) 
	ret = ""
	ret += "|".join([cat for cat in header]) + "\n"
	ret += "|".join(["-" for num in xrange(len(header))]) + "\n"
	for cat in rows:
		ret += "|".join([stat for stat in cat]) + "\n"
	return ret