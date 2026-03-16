from prime_creation import getPrime

def GCD(A, B):
    while B != 0:
        R = A % B
        A = B
        B = R
    return A

e = 65537

while True:
    p = getPrime()
    q = getPrime()
    n = p*q
    z = (p-1)*(q-1)
    if GCD(e, z) == 1:
        break

d = pow(e, -1, z)

print(f"p value: {p}\nq value: {q}\nn value: {n}\nz value: {z}\ne value: {e}")

print(f"Public Key: {n}, {e}\nPrivate Key: {n}, {d}")
