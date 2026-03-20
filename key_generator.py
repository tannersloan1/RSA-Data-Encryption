from prime_creation import getPrime

def GCD(A, B):
    while B != 0:
        R = A % B
        A = B
        B = R
    return A

e = 65537 # Static e value since it is in the public key anyways, therefore this value is already public knowledge

# While true needed since e value is static high prime number, and rarely e and z could still be not relatively prime and thus p and q need to be redrawn
while True:
    p = getPrime()
    q = getPrime()
    n = p*q
    z = (p-1)*(q-1)
    if GCD(e, z) == 1:
        break

d = pow(e, -1, z) # This solves for d from ed mod z = 1 -> d = e**(-1) mod z

print(f"p value: {p}\nq value: {q}\nn value: {n}\nz value: {z}\ne value: {e}")

print(f"Public Key: {n}, {e}\nPrivate Key: {n}, {d}")
