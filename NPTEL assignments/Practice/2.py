
n = int(input("Enter Number: "))
total = 0
sq = n**2
#print(sq)
temp = sq
while(temp > 0):
    digit = temp % 10
    #print("digit", digit)
    temp = temp // 10
    #print("temp", temp)
    total += digit 
    #print("total", total)


if(total == n):
    print(f"{n} is a Neon Number")
else:
    print(f"{n} is not Neon Number")
