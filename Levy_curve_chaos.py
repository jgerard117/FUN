import numpy as np
import matplotlib.pyplot as plt

N = 1e5
ini = [.65, .25]

A = [[.5, .5],
     [-.5, .5]]

B = [[.5, -.5],
     [.5, .5]]

def f1(x):
    return np.matmul(A, x)

def f2(x):
    return np.matmul(B, x) - [.5, .5]

all_points = [ini]

for point in all_points:
    f1_point = f1(point)
    f2_point = f2(point)
    all_points.append(f1_point)
    all_points.append(f2_point)
    if len(all_points) > N:
        break

traj_x_f1 = []
traj_y_f1 = []
traj_x_f2 = []
traj_y_f2 = []

for point_in, point in enumerate(all_points):
    if point_in%2 == 0:
        traj_x_f1.append(point[0])
        traj_y_f1.append(point[1])
    else:
        traj_x_f2.append(point[0])
        traj_y_f2.append(point[1])


fig, ax = plt.subplots()
ax.plot(traj_x_f1[1000:], traj_y_f1[1000:], linestyle='None', marker='o', markersize=0.1, color='blue')
ax.plot(traj_x_f2[1000:], traj_y_f2[1000:], linestyle='None', marker='o', markersize=0.1, color='red')
plt.show()