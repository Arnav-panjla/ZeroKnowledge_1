from py_ecc.bn128 import G1, G2, multiply, neg, eq, add, pairing

print(G1)
print(G2)# 2 dimension (tupple od two points)

A = multiply(G1,5)
B = multiply(G2,7)
C = multiply(G1,5*7)

print(pairing(A,B) == pairing(C,G2))
