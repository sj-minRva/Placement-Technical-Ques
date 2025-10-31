def SentenceCount(L):
    ans=0
    for w in L:
        if w[len(w)-1]=='!' or w[len(w)-1]=='?':
            ans+=1
        elif(w=="."):
            ans+=1
        elif len(w)>1:
            if w[len(w)-1]=='.' and w[len(w)-2]!='.':
                ans+=1 
    return ans
            
       

string = "Heloo bitch... Heloo-bitch. Heloo bitch. Heloo bitch! Heloo bitch?"

result = SentenceCount(string)
print("Number of sentences:", result)