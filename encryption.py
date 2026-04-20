pt = open("plaintext.txt", "r")
io = open("integer_output.txt", "w")
bo = open("binary_output.txt", "w")

chars = 190 # 190 bytes mimics RSA-2048 blocks with SHA-256
currChars = 0
currBlock = ""
padding = "11111111" # Pad with 'ÿ' currently since that character will never appear in my test files as of yet.
numOfChars = 0

while True:
    while currChars != chars:
        char = pt.read(1)

        # Once EOF reached, pad the rest of the last block then break
        if not char and currChars > 0:
            # Simple padding using non english character just to match block sizes
            while currChars != chars:
                currBlock += padding
                currChars += 1
            break

        if not char and currBlock == "":
            break

        numOfChars += 1

        ASCII = ord(char)
        binary = format(ASCII, '08b')
        currBlock += binary

        currChars += 1

    # Accounts for text size exactly divisible by chars
    if currBlock == "":
        break

    decimal = int(currBlock, 2)

    # Dont change e
    e = 65537
    # Input public key first value
    n = 27758594710752956739217244527139120423185930180391801879803978936534564894493338977333999253978673341158004510811913046392147280619420490214436857340888686184750970705963329173746325249849122452434830236447004613382045577685302679259597666699826915597208072833919315603676300872735996739832039622139888398558071424139916259468314816870427426265206266479322057497588754232262162016158206651872090475767517984954476454928771514787291380475516123494087838417250479634936674980119870954232344902797816310757560153197688634172100162950201490717692693511028047305385322863343537274697933302224011402428446817709652783452567

    integerOutput = pow(decimal, e, n)
    io.write(str(integerOutput) + "\n")
    binaryOutput = format(integerOutput, '02048b')
    bo.write(binaryOutput + "\n")
    
    currBlock = ""
    currChars = 0

    if not char:
        break

pt.close()
bo.close()
io.close()
