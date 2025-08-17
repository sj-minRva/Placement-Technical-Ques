'''
“A positive integer has been given as an input. Convert decimal value to binary
representation. Toggle all bits of it after the most significant bit including the most
significant bit. Print the positive integer value after toggling all bits”.
Constrains-1<=N<=100
'''
def dbConvertor(n):
    binary = []
    num = n
    while num > 0:
        rem = num % 2
        binary.append(rem)
        num = num // 2
        
    binary.reverse()
    print(binary)
    
    toogle = [], 
    for i in binary:
        if binary[i] == 1:
            toogle.append = 0
        else:
            toogle.append(one) 
    print(toogle)

dbConvertor(23)

"""

    """
        
