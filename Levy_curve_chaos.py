# Levy Curve from the Chaos Game.
# Justin Gerard - 04/10/24
# It took it from : https://www.youtube.com/watch?v=dklWNdM9WSg
# It's an example of choas theory. 

# Start by importing some good stuff
import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
N = 25000
ini = [.65, .25]

A = [[.5, .5],
     [-.5, .5]]

B = [[.5, -.5],
     [.5, .5]]

# Define the two functions
def f1(x):
    return np.matmul(A, x)

def f2(x):
    return np.matmul(B, x) - [.5, .5]

# Plot the transformation
fig, ax = plt.subplots()
point = ini
for i in range(N+1):
    if random.random() < 0.5: # Flip a coin to see which function it takes
        point = f1(point) # Take function 1
        ax.plot(point[0], point[1], linestyle='None', marker='o', 
                markersize=0.5, color='blue')
    else:
        point = f2(point) # Take function 2
        ax.plot(point[0], point[1], linestyle='None', marker='o', 
                markersize=0.5, color='red')
    if i%1000 == 0: # Print the process
        print("{:.2f}".format(100*i/N)+"% DONE")
plt.show()
