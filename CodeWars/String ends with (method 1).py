#String ends with?


def solution(text, ending):
    
    if len(ending) > len(text):
        return False
    
    i = -1
    count = 0
    
    while count < len(ending):
        if ending[i] != text[i]:           
            return False
        
        i -= 1
        count += 1
    
    return True
        
        
