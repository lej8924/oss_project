import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#시각화
data1 = pd.read_csv('data/final.csv')
data1 = data1.drop('Unnamed: 0',axis=1)

star = data1['Score']
numstar = data1['Numberofscore']
total = data1['Totalscore']

xs = np.array(star)
ys = np.array(numstar)
zs = np.array(total)
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs, marker='o', s=1, cmap='Greens')
plt.show()

plt.figure()
plt.scatter(ys,zs,marker='+')
plt.grid(True)
plt.show()