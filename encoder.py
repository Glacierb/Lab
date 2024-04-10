def encoder(message):
    crypt = ""
    try:
        for num in message:
            crypt = crypt + str((int(num)+3))
        return int(crypt)
    except:
        print("Error, please enter number string only")

#print(encoder("0055511"))