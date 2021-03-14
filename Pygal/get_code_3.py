from pygal.maps.world import COUNTRIES

def get_country_code(name_country):
	for code, country_name in sorted(COUNTRIES.items()):
		if name_country == country_name:
			return code
		elif name_country == "Yemen, Rep.":
			return 'ye'
		elif name_country == "Egypt, Arab Rep.":
			return 'eg'
		elif name_country == "Venezuela, RB":
			return 've'
		elif name_country == "Tanzania":
			return 'tz'
		elif name_country == "Libya":
			return 'ly'
		elif name_country == "Mayotte":
			return 'yt'
		elif name_country == "Moldova":
			return 'md'
		elif name_country == "Slovak Republic":
			return 'sk'
		elif name_country == "Bolivia":
			return 'bo'
		elif name_country == "Congo, Dem. Rep.":
			return 'cd'
		elif name_country == "Congo, Rep.":
			return 'cg'
		elif name_country == "Korea, Rep.":
			return 'kr'
		elif name_country == "Korea, Dem. Peopleâ€™s Rep.":
			return 'kp'
		elif name_country == "Iran, Islamic Rep.":
			return "ir"
		elif name_country == "Kyrgyz Republic":
			return 'kg'
		elif name_country == "Vietnam":
			return 'vn'
		elif name_country == "Gambia, The":
			return 'gm'
		elif name_country == "Eritrea":
			return "er"
	return False
