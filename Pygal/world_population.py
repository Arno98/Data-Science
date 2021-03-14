import json
from pygal.maps.world import World
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
			
worldmap = World()
worldmap.force_uri_protocol = 'http'
worldmap.title = "World Population(2016)"
worldmap.add('2016', world_population_data)

worldmap.render_to_file('world_population_2016.svg')
		
