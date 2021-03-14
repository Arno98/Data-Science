import json
from pygal.maps.world import World
from pygal.style import LightColorizedStyle, RotateStyle
from get_code_3 import get_country_code

gdp_file = 'gdp_json.json'
with open(gdp_file) as gdp:
	gdp_read = json.load(gdp)
	
world_gdp = {}
for dic in gdp_read:
	if dic['Year'] == 2016:
		country_name = dic['Country Name']
		gdp_value = dic['Value']
		code = get_country_code(country_name)
		if code:
			world_gdp[code] = gdp_value
			
gdp_1, gdp_2, gdp_3, gdp_4, gdp_5, gdp_6, gdp_7, gdp_8, gdp_9, gdp_10, gdp_11 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
for c, v in world_gdp.items():
	if int(v) < 10000000000:
		gdp_1[c] = v
	elif int(v) < 20000000000:
		gdp_2[c] = v
	elif int(v) < 50000000000:
		gdp_3[c] = v
	elif int(v) < 100000000000:
		gdp_4[c] = v
	elif int(v) < 200000000000:
		gdp_5[c] = v
	elif int(v) < 500000000000:
		gdp_6[c] = v
	elif int(v) < 1000000000000:
		gdp_7[c] = v
	elif int(v) < 2000000000000:
		gdp_8[c] = v
	elif int(v) < 5000000000000:
		gdp_9[c] = v
	elif int(v) < 10000000000000:
		gdp_10[c] = v
	else:
		gdp_11[c] = v
			
wm_style = RotateStyle('#113355', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = "World GDP by Country (2016)"
wm.add("< 10b", gdp_1)
wm.add("< 20b", gdp_2)
wm.add("< 50b", gdp_3)
wm.add("< 100b", gdp_4)
wm.add("< 200b", gdp_5)
wm.add("< 500b", gdp_6)
wm.add("< 1000b", gdp_7)
wm.add("< 2000b", gdp_8)
wm.add("< 5000b", gdp_9)
wm.add("< 10000b", gdp_10)
wm.add("> 10000b", gdp_11)

wm.render_to_file("World GDP.svg")
