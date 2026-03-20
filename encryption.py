#fileName = input("What is your file name? ")

pt = open("plaintext.txt", "r")
io = open("integer_output.txt", "w")
bo = open("binary_output.txt", "w")

chars = 7 # 7 characters for a 56 bit block size
currChars = 0
currBlock = ""

while True:
    while currChars != chars:
        char = pt.read(1)

        # Once EOF reached, pad the rest of the chars to reach 7 chars in the last block then break
        if not char:
            # Need to add padding logic here
            break

        ASCII = ord(char)
        binary = format(ASCII, '08b')
        currBlock += binary

        currChars += 1

    # Accounts for text size exactly divisible by chars
    if currBlock == "":
        break

    decimal = int(currBlock, 2)

    # Hardcoded public key for now
    e = 65537
    n = 184046416711673963014408940636636297981

    integerOutput = pow(decimal, e, n)
    io.write(str(integerOutput) + "\n")
    binaryOutput = format(integerOutput, '0128b')
    bo.write(binaryOutput + "\n")
    

    currBlock = ""
    currChars = 0

    if not char:
        break

pt.close()
bo.close()
io.close()
