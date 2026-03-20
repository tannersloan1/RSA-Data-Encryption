import random

hundredPrimes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 
    113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 
    251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 
    397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541
]

def getRandom(bits):
    return random.randrange(2**(bits-1)+1, 2**(bits)-1)

# Grabs a potentially prime number from the n bit range then tests primality based off small number primes
def relativePrime(bits):
    while True:
        pp = getRandom(bits)

        for num in hundredPrimes:
            if pp % num == 0: # Might need " and num**2 <= pp" if using bits<20 otherwise, 541**2 is always <= pp
                break
        else:
            return pp
            
def millerRabinTest(pp):
    maxDivisionsByTwo = 0
    ec = pp-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == pp-1)

    def trial(currTest):
        if pow(currTest, ec, pp) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(currTest, 2**i * ec, pp) == pp-1:
                return False
        return True
    
    rabinTrials = 20
    for i in range(rabinTrials):
        currTest = random.randrange(2, pp)
        if trial(currTest):
            return False
    return True

def getPrime():
    while True:
        bits = 64
        pp = relativePrime(bits)
        if not millerRabinTest(pp):
            continue
        else:
            print("Your random", bits, "bit prime is:", pp)
            return pp
