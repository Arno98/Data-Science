import json
gdp_file = 'gdp_json.json'
with open(gdp_file) as gdp:
	gdp_read = json.load(gdp)
	
values = {}
for d in gdp_read:
	if d['Year'] == 2016:
		n_c = d['Country Name']
		value = d['Value']
		values[n_c] = value

min_value = []
for c, v in sorted(values.items()):
	max_v = values['United States']
	min_value.append(values[c])
print(int(min(min_value)))
print(int(max_v))
