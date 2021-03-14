import json
from pygal.maps.world import World
from pygal.style import LightColorizedStyle, RotateStyle
from get_code_3 import get_country_code

filename = 'population_json.json'
with open(filename) as datafile:
	pop_data = json.load(datafile)

world_population_data = {}
for dictionary in pop_data:
	if dictionary['Year'] == 2016:
		country_name = dictionary['Country Name']
		population = dictionary['Value']
		country_code = get_country_code(country_name)
		if country_code:
			world_population_data[country_code] = population
			
low_population, middle_population, high_population = {}, {}, {}
for code, population in world_population_data.items():
	if population < 10000000:
		low_population[code] = population
	elif population < 1000000000:
		middle_population[code] = population
	else:
		high_population[code] = population
		
worldmap_style = RotateStyle('#336699', base_style=LightColorizedStyle)		
worldmap = World(style = worldmap_style)
worldmap.force_uri_protocol = 'http'
worldmap.title = "World Population by Country (2016)"
worldmap.add('<10m', low_population)
worldmap.add('10m - 1bn', middle_population)
worldmap.add('>1bn', high_population)

worldmap.render_to_file('world_population_by_country_2016.svg')
		
