import matplotlib.pyplot as plt
from py_ecc.bn128 import G1, Z1, multiply, neg, curve_order, field_modulus
import math

# inv of a = neg(a)
# z1 is point of infinity Z1 is None
"""
point_at_infinity = order*G1
(order + x - x)*G1 = point_at_infinity
(order - x)*G1 = -xG1 + point_at_infinity
(order - x)*G1 = -xG1 + point_at_infinity
(order - x)*G1 = -xG1
(order - x)*G1 = neg(x*G1)
"""


# import numpy as np
xs = []
ys = []
for i in range(1,1000):
    xs.append(i)
    ys.append(int(multiply(G1, i)[1]))
    xs.append(i)
    ys.append(int(neg(multiply(G1, i))[1]))
plt.scatter(xs, ys, marker='.')

print(f"Generator is {G1}")
print(f"curve order is {curve_order}\nfield modulus is {field_modulus}")

plt.show()