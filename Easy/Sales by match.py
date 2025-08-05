def sockMerchant(n, ar):
    colorCount = {}
    pairs = 0

    for color in ar:
        if color in colorCount:
            colorCount += 1
        else:
            colorCount = 1
    for color in colorCount.values():
        pairs += color//2
    return pairs



ar = [1,2,3,1,2]
result = sockMerchant(5, ar)
print(result)
