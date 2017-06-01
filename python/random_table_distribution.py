import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from random_table import *

scores = []

for i in range(10000):
    scores.append(random_table().score())
    if i %1000 == 0:
        print i

plt.hist(scores, normed=True, bins = 20)
plt.xlabel("Score")
plt.ylabel("")
plt.title("Scoreverdeling van random roosters")
plt.show()
print np.std(scores)
print np.average(scores)
