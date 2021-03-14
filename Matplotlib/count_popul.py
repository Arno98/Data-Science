import matplotlib.pyplot as plt

years = [1820, 1927, 1960, 1974, 1987, 1999, 2011]
numbers_of_people = [1, 2, 3, 4, 5, 6, 7]

while True:
	next_year = years[-1] + 1
	next_numbers_of_people = numbers_of_people[-1] + 0.065
	years.append(next_year)
	numbers_of_people.append(next_numbers_of_people)
	if years[-1] == 2100:
		False
		plt.plot(years, numbers_of_people, linewidth=3)
		
		plt.title("World population(from 1820 to 2100)", fontsize=20)
		plt.xlabel("Year", fontsize=20)
		plt.ylabel("Billion of people", fontsize=15)
		plt.tick_params(axis='both', which='major', labelsize=15)
		
		plt.show()
		
