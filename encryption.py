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
        
        # Need to add following flow here: ASCII value->Binary value->Concat binary to current 56-bit string

        currChars += 1

    # Need to add logic here to encrypt the 56-bit string and either save it or output it before emptying it

    currBlock = ""
    currChars = 0

    if not char:
        break