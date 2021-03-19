#The model on the basis of which data analysis is performed: https://uk.wikipedia.org/wiki/%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%B0_%D0%BF%27%D1%8F%D1%82%D1%96%D1%80%D0%BA%D0%B0_(%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D1%96%D1%8F)
#Data source: https://www.kaggle.com/tunguz/big-five-personality-test

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pycountry_convert

df = pd.read_csv('Datasets/bf_data.csv', sep='\t')

cols = df.columns.values[:50]
df[cols].dropna().astype(int)

#New columns are created to merge the data (according to the test rules, some values ​​are negative)
df["EXT"] = df["EXT1"] - df["EXT2"] + df["EXT3"] - df["EXT4"] + df["EXT5"] - df["EXT6"] + df["EXT7"] - df["EXT8"] + df["EXT9"] - df["EXT10"]
df["EST"] = df["EST1"] - df["EST2"] + df["EST3"] - df["EST4"] + df["EST5"] + df["EST6"] + df["EST7"] + df["EST8"] + df["EST9"] + df["EST10"]
df["AGR"] = - df["AGR1"] + df["AGR2"] - df["AGR3"] + df["AGR4"] - df["AGR5"] + df["AGR6"] - df["AGR7"] + df["AGR8"] + df["AGR9"] + df["AGR10"]
df["CSN"] = df["CSN1"] - df["CSN2"] + df["CSN3"] - df["CSN4"] + df["CSN5"] - df["CSN6"] + df["CSN7"] - df["CSN8"] + df["CSN9"] + df["CSN10"]
df["OPN"] = df["OPN1"] - df["OPN2"] + df["OPN3"] - df["OPN4"] + df["OPN5"] - df["OPN6"] + df["OPN7"] - df["OPN8"] + df["OPN9"] + df["OPN10"]

#Correlation
sns.heatmap(df[["EXT", "AGR", "CSN", "EST", "OPN"]].corr(), annot=True).set_title("Кореляція 5 якостей людини")

#Distribution (full range of data)
fig, axs = plt.subplots(ncols = 2, nrows = 3)
sns.distplot(df["EXT"], bins = 50, kde = False, ax = axs[0, 0]).set_title("Екстраверсія")
sns.distplot(df["EST"], bins = 50, kde = False, ax = axs[0, 1]).set_title("Нейротизм")
sns.distplot(df["AGR"], bins = 50, kde = False, ax = axs[1, 0]).set_title("Доброзичливість")
sns.distplot(df["CSN"], bins = 50, kde = False, ax = axs[1, 1]).set_title("Сумлінність")
sns.distplot(df["OPN"], bins = 50, kde = False, ax = axs[2, 0]).set_title("Відкритість")
fig.delaxes(axs[2, 1])

#Distribution (Ukraine)

#1
fig, ax = plt.subplots()
traits = ["EXT", "AGR", "CSN", "EST", "OPN"]
bf_ua = df.loc[df['country'] == 'UA', ["EXT", "AGR", "CSN", "EST", "OPN"]].dropna().astype(int)
for t in traits:
	sns.distplot(df[df['country'] == 'UA'][t], hist=False, label = t)
plt.legend()


#2
fig, axs = plt.subplots(ncols = 2, nrows = 3)
sns.distplot(bf_ua["EXT"], bins = 50, kde = False, ax = axs[0, 0]).set_title("Екстраверсія")
sns.distplot(bf_ua["EST"], bins = 50, kde = False, ax = axs[0, 1]).set_title("Нейротизм")
sns.distplot(bf_ua["AGR"], bins = 50, kde = False, ax = axs[1, 0]).set_title("Доброзичливість")
sns.distplot(bf_ua["CSN"], bins = 50, kde = False, ax = axs[1, 1]).set_title("Сумлінність")
sns.distplot(bf_ua["OPN"], bins = 50, kde = False, ax = axs[2, 0]).set_title("Відкритість")
fig.delaxes(axs[2, 1])


plt.show()
