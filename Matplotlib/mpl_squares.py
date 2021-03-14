import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

x = list(range(1, 101))
y = [v ** 2 for v in x]

fig, ax = plt.subplots()

ax.scatter(x, y, s=20, c=y, cmap=plt.cm.Greens)
#ax.plot(x, y, linewidth=3)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)

plt.show()
