import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.walk()

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(rw.x_value, rw.y_value, linewidth=3)
#ax.scatter(rw.x_value, rw.y_value, s=20)
ax.scatter(0, 0, c='green', s=100)
ax.scatter(rw.x_value[-1], rw.y_value[-1], c='red', s=100)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()
