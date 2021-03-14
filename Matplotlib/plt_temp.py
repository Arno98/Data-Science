import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'GHCND_sample_csv.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates, highs, lows, prcp = [], [], [], []
	for row in reader:
		highs.append(int(row[6]))
		lows.append(int(row[7]))
		dates.append(datetime.strptime(row[5], '%Y%m%d'))
		
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.7)
ax.scatter(dates, highs, c='red', s=20)
ax.plot(dates, lows, c='blue', alpha=0.7)
ax.scatter(dates, lows, c='blue', s=20)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
fig.autofmt_xdate()

plt.title("Daily high, lows temperature", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
