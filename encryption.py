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

        # Once EOF reached, pad the rest of the chars to reach 7 chars in the last block then break
        if not char and currChars > 0:
            # Need to add padding logic here
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

    # Hardcoded public key for now
    e = 65537
    n = 25595514236646107473519646798026218870673445058450134861748566760731216739331724190997236648356557788001357990682349976140656189497288898973964149218609425570731319418006258021477282682985312307581195058298923025253353996981644911021492572271639776306566733236104306450503421785417047243845032381196189536073265973367539633127894950277727903795782229452629172318748153296675745596743631806350583672528344037602347415052410137640915092043644829986693004955088687977560194630034447024762832869032531996007155606759722847325046211989823965249427720881068793546018299643299782728949446565415375775106043433599460746819657

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
