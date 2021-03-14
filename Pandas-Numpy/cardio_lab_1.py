import numpy as np
import pandas as pd

#зчитуємо дані з файлу (csv формат)
df = pd.read_csv('mlbootcamp5_train.csv', sep=';',index_col='id')

#знаходимо середнє значення зросту для обох гендерів та робимо висновок, що жінок позначено як "1", а чоловіків як "2"
mean1 = round(df[df['gender'] == 1]['height'].mean(), 2)
mean2 = round(df[df['gender'] == 2]['height'].mean(), 2)

#рахуємо кількість жінок і чоловіків
gender1 = df[df['gender'] == 1]['gender'].count()
gender2 = df[df['gender'] == 2]['gender'].count()

#знаходимо середнє значення по вживанню алкоголю серед обох гендерів і визначаем що жінки (1) в середньому рідше вказують, що вживають алкоголь
mean_alco1 = df[df['gender'] == 1]['alco'].mean()
mean_alco2 = df[df['gender'] == 2]['alco'].mean()

#рахуємо відсоток тих, кто курить для обох гендерів і визначаємо що відстоток чоловіків, що курять в 12.2 разів більше ніж відстоток жінок, що курять
count_smoke1 = pd.crosstab(df[df['gender'] == 1]['gender'], df[df['smoke'] == 1]['smoke'])
count_smoke2 = pd.crosstab(df[df['gender'] == 2]['gender'], df[df['smoke'] == 1]['smoke'])

procent_smoke1 = round(count_smoke1 * 100 / gender1, 1)
procent_smoke2 = round(count_smoke2 * 100 / gender2, 1)

bigger_smoke = round(procent_smoke2 / 1.8, 1)

#рахуємо середнє значення віку для тих, хто курить і не курить, потім рахуємо різницю в місяцях, яка становить 13.8 місяців
mean_smoke0 = df[df['smoke'] == 0]['age'].mean()
mean_smoke1 = df[df['smoke'] == 1]['age'].mean()

differ = round((mean_smoke0 - mean_smoke1) / 30, 1)

#додаємо ознаку age_years до данних та виділяємо 2 підгрупи по 22 людини (щоб зрівняти результати, бо в групі №1 78 людей, а в групі №2 22 людини) та рахуємо кількість хворих в групах і бачимо що в групі №2 в 4.7 разів більше хворих людей
df['age_years'] = round(df['age'] / 365)

group1 = df[(df['ap_hi'] < 120) & (df['age_years'] >= 60) & (df['age_years'] <= 64) & (df['cholesterol'] == 1) & (df['smoke'] == 1) & (df['gender'] == 2)][['age_years', 'cholesterol','ap_hi','smoke','cardio']].head(22)
group2 = df[(df['ap_hi'] >= 160) & (df['ap_hi'] < 180) & (df['age_years'] >= 60) & (df['age_years'] <= 64) & (df['cholesterol'] == 3) & (df['smoke'] == 1) & (df['gender'] == 2)][['age_years', 'cholesterol','ap_hi','smoke','cardio']]

cardio01 = group1[group1['cardio'] == 1]['cardio'].count()
cardio02 = group2[group2['cardio'] == 1]['cardio'].count()

differ_ill = cardio02 / cardio01

#додаємо ознаку bmi
df['bmi'] = round(df['weight'] / (df['height'] / 100) ** 2)

#медіана перевищує норму
median = df['bmi'].median()

#у жінок bmi вище ніж у чоловіків
mean_bmi1 = df[df['gender'] == 1]['bmi'].mean()
mean_bmi2 = df[df['gender'] == 2]['bmi'].mean()

#у здорових bmi нижче ніж у хворих
mean_bmi11 = df[df['cardio'] == 1]['bmi'].mean()
mean_bmi22 = df[df['cardio'] == 0]['bmi'].mean()

#у сегменті здорових чоловіків, які не вживають алкоголь bmi ближче до норми ніж у такого ж сегменту жінок
mean_bmi111 = df[(df['gender'] == 1) & (df['alco'] == 0) & (df['cardio'] == 0)]['bmi'].mean()
mean_bmi222 = df[(df['gender'] == 2) & (df['alco'] == 0) & (df['cardio'] == 0)]['bmi'].mean()
