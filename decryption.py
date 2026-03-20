from encryption import chars

bo = open("binary_output.txt", "r")
do = open("decrypted.txt", "w")

# Hardcoded private key for now
n = 184046416711673963014408940636636297981
d = 143646463237847855116190660847814428773
blockSize = chars*8


for line in bo:
    currString = line.strip()
    decimal = int(currString, 2)
    message = pow(decimal, d, n)
    binary = format(message, "056b")
    currBit = 0
    while currBit < blockSize:
        binaryChar = ""
        binaryChar += binary[currBit]
        binaryChar += binary[currBit+1]
        binaryChar += binary[currBit+2]
        binaryChar += binary[currBit+3]
        binaryChar += binary[currBit+4]
        binaryChar += binary[currBit+5]
        binaryChar += binary[currBit+6]
        binaryChar += binary[currBit+7]

        ASCII = int(binaryChar, 2)
        char = chr(ASCII)
        do.write(char)

        currBit += 8