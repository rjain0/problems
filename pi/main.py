import random
import math

# method 1
pi = 3.14
d = 100.0
A_circle = pi * (d/2) ** 2
A_square = d ** 2
P1 = A_circle / A_square

print(P1)

# method 2
N = 1000
Nc = 0.0
for i in range(N):
  x = random.random() * d
  y = random.random() * d
  distance = math.sqrt(((d/2)-x)**2 + ((d/2)-y)**2)
  if distance < d/2:
    Nc += 1

p_pi = 4.0 * Nc / N
P2 = Nc / N
print(P2)
print(p_pi)