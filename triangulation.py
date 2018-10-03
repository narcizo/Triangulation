import matplotlib.pyplot as plt
import numpy as np
import math

################### Variáveis #######################
xi = [1.55, -4.02, -4.40, 9.27, 9.15]
yi = [17.63, 0, 9.6, 4.64, 12]
ro0 = [-26, -33.8, -29.8, -31.2, -33]
lk = [2.1, 1.8, 1.3, 1.4, 1.5]
raio = []

#caso 1
#rok = [-48.4, -50.6, -32.2, -47.4, -46.3]
#xreal = 0
#yreal = 9

#caso 2
rok = [-46.9, -46.4, -41.2, -45.8, -48.7]
xreal = 3
yreal = 3

##################### Execução ####################
for i in range(5):
     raio.append(10**((ro0[i] - rok[i])/(10*lk[i])))
     print(raio[i])
A = np.matrix([[xi[4] - xi[0], yi[4] - yi[0]],
               [xi[4] - xi[1], yi[4] - yi[1]],
               [xi[4] - xi[2], yi[4] - yi[2]],
               [xi[4] - xi[3], yi[4] - yi[3]],
               [xi[1] - xi[4], yi[1] - yi[4]]])
#Wi = Xi:^2 + Yi^2 - Di^2
B = np.matrix([[  (xi[4]**2 + yi[4]**2 -raio[4]**2) - (xi[0]**2 + yi[0]**2 -raio[0]**2)],
                 [(xi[4]**2 + yi[4]**2 -raio[4]**2) - (xi[1]**2 + yi[1]**2 -raio[1]**2)],
                 [(xi[4]**2 + yi[4]**2 -raio[4]**2) - (xi[2]**2 + yi[2]**2 -raio[2]**2)],
                 [(xi[4]**2 + yi[4]**2 -raio[4]**2) - (xi[3]**2 + yi[3]**2 -raio[3]**2)],
                 [(xi[1]**2 + yi[1]**2 -raio[1]**2) - (xi[4]**2 + yi[4]**2 -raio[4]**2)]])


print(A)
print(B)
#(At * A)^-1 * B
A *= 2
X = (A.T * A).I * A.T * B
print(X)


circle1 = plt.Circle((xi[0], yi[0]), raio[0], color='b', clip_on=False, fill=False)
circle2 = plt.Circle((xi[1], yi[1]), raio[1], color='b', clip_on=False, fill=False)
circle3 = plt.Circle((xi[2], yi[2]), raio[2], color='b', clip_on=False, fill=False)
circle4 = plt.Circle((xi[3], yi[3]), raio[3], color='b', clip_on=False, fill=False)
circle5 = plt.Circle((xi[4], yi[4]), raio[4], color='b', clip_on=False, fill=False)

fig, ax = plt.subplots()

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)
ax.add_artist(circle4)
ax.add_artist(circle5)

ax = plt.gca()
ax.cla()

ax.set_xlim((-15, 30))
ax.set_ylim((-15, 30))

ax.plot(xreal, yreal, 'o', color='r')#real
ax.plot(X[0][0], X[1][0], 'go', color='g')#estimado

ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)
ax.add_patch(circle4)
ax.add_patch(circle5)
plt.show()

fig.savefig('caso2.png')
