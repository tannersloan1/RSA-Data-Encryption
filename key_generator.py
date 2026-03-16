from prime_creation import getPrime
import random

def GCD(A, B):
    while B != 0:
        R = A % B
        A = B
        B = R
    return A

def getE(z):
    while True:
        e = random.randrange(2, z)
        if GCD(e, z) == 1:
            return e

p = getPrime()
q = getPrime()
n = p*q
z = (p-1)*(q-1)
e = getE(z)
d = pow(e, -1, z)

print(f"p value: {p}\nq value: {q}\nn value: {n}\nz value: {z}\ne value: {e}")

print(f"Public Key: {n}, {e}\nPrivate Key: {n}, {d}")
