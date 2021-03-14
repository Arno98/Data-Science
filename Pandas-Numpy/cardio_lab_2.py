import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.ticker
import matplotlib.pyplot as plt

sns.set_context("notebook", font_scale=1.5, rc={"figure.figsize": (12, 8), "axes.titlesize": 14})

df = pd.read_csv('mlbootcamp5_train.csv', sep=';', index_col='id')

df_uniques = pd.melt(frame=df, value_vars=['gender'], id_vars=['height']) 
df_uniques = pd.DataFrame(df_uniques.groupby(['variable', 'value', 'height'])['value'].count()).sort_index(level=[0, 1]).rename(columns={'value': 'count'}).reset_index()

#з цієї матриці ми бачимо, що з ознакою height найбільше корелюються дві ознаки (gender та weight)
sns.heatmap(df.corr(), annot=True)

#візуалізація, яка показує зріст по гендеру
sns.violinplot(x='variable', y=df['height'], hue='value', scale='count', data=df_uniques, kind='bar', height=8)

#кореляція за методом Спірмена показує, що найбільш корелюються зріст та гендер, api_hi та api_lo, глюкоза та холестерин
sns.heatmap(df.corr(method='spearman'), annot=True)

#спільний графік розподілу двох найбільше корелюючих ознак за методом Спірмена показує 6 чітких кластерів
data_filtered = df[(df['ap_hi'] > 0) & (df['ap_lo'] > 0)][['ap_lo', 'ap_hi']].apply(np.log1p)
g = sns.jointplot(data_filtered['ap_hi'], data_filtered['ap_lo'], height=10,  marginal_kws=dict(bins=100, rug=False, hist_kws={'log': True}), marker='.')
g.ax_joint.grid(True)
g.ax_joint.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, pos: str(round(int(np.exp(x))))))
g.ax_joint.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, pos: str(round(int(np.exp(x))))))

#графік показує, що у віці 53 років частка хворих перевищує частку здорових
df['age_years'] = (df['age'] // 365.25).astype(int)
sns.countplot(x=df['age_years'], hue=df['cardio'], data=df)

plt.show()
