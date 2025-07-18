a = [1, 2, 3, 4, 3, 2, 1]

def lonelyinteger(a):
    # Write your code here
    count = 0
    for i in a:
        for j in a:
            if i == j:
                count +=1
        if count == 1:
            result = i
        count = 0
    return result
        
ans = lonelyinteger(a)
print(ans)
