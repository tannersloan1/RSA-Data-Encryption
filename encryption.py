fileName = input("What is your file name? ")

file = open(fileName, "r")

chars = 7 # 7 characters for a 56 bit block size
currChars = 0
currBlock = ""

while True:
    while currChars != chars:
        char = file.read(1)

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

    # Hardcoded PK for now
    e = 65537
    n = 142330907879694598390734510141721402859

    c = pow(decimal, e, n)
    print(c) # For test, replace with actualy save/write command

    currBlock = ""
    currChars = 0

    if not char:
        break
