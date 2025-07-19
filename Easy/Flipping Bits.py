def flippingBits(n):

    binary = format(n, '32b')
    flipped = ''
    for i in binary:
        if i == '1':
            flipped += '0'
        else:
            flipped += '1'
    print(flipped)

    result = int(flipped, 2)
    print(result)

flippingBits(23)
