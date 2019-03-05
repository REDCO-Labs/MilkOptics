import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

style.use("ggplot")
sns.set()

files = ["fanta"]

for file in files:
    data = np.loadtxt(file)
    # sns.scatterplot(data[:, 0], data[:, 1]*(1 + i/100))
    plt.plot(data[:, 0], data[:, 1], label=file)

plt.legend(loc='best')
plt.show()
