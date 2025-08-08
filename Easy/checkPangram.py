
def pangrams(s):
    alphabets = set('qwertyuiopasdfghjklzxcvbnm')
    string = set(s.lower())

    if alphabets.issubset(string):
        return 'pangram'
    else:
        return 'not pangram'


        
s = "Pack my box with five jugs"
result = pangrams(s)
print(result)
        
