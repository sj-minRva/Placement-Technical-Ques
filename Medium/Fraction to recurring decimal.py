def fractionToDecimal(numerator, denominator):
    result = numerator/denominator
    print(result)
    
    j = i+1
    for i in range( len(denum) ):
        if denum[i] != denum[j]:
            temp[i] = denum[j]
            j+=1
            count+=1

        if denum[i] == denum[j]:
            for x in range(i , count+i):
                if denum[i] == denum[j]:
                    print(denum[i])
    

fractionToDecimal(4, 333)

     
        
