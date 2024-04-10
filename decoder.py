def decoder(string):
    decoded = ""
    for digit in string:
        digit = int(digit)
        if digit < 3:
            digit = digit + 10 - 3
        else:
            digit -= 3
        decoded = decoded + str(digit)
    return decoded
