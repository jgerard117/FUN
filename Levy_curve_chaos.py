# Levy Curve from the Chaos Game.
# Justin Gerard - 04/10/24
# It took it from : https://www.youtube.com/watch?v=dklWNdM9WSg
# It's an example of choas theory. 

import numpy as np
import matplotlib.pyplot as plt
import random

N = 25000
ini = [.65, .25]

A = [[.5, .5],
     [-.5, .5]]

B = [[.5, -.5],
     [.5, .5]]

def f1(x):
    return np.matmul(A, x)

def f2(x):
    return np.matmul(B, x) - [.5, .5]

fig, ax = plt.subplots()
point = ini
for i in range(N+1):
    if random.random() < 0.5:
        point = f1(point)
        ax.plot(point[0], point[1], linestyle='None', marker='o', markersize=0.5, color='blue')
    else:
        point = f2(point)
        ax.plot(point[0], point[1], linestyle='None', marker='o', markersize=0.5, color='red')
    if i%1000 == 0:
        print("{:.2f}".format(100*i/N)+"% DONE")
plt.show()
