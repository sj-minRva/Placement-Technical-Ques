#NPTEL WEEK-2 assignment - 1

n = int(input())
total = 0
for x in range(1,n+1): #n goes only until n-1
    if x%2 != 0:
        total += x
print(total)
    

'''
Gautam Gambhir, freshly appointed head coach for India’s 2025 away Test series against England, has asked the new analyst, Aryan, to keep a quirky statistic:
“At the end of each day’s play,” Gambhir says, “tell me the total runs we scored in every odd-numbered over—1st, 3rd, 5th … all the way up to the last over bowled that day. It helps me spot momentum in the sessions where bowlers are freshest.”
Aryan realises the job boils down to simple maths: if n is the last over of the day (always a positive integer), he just needs the sum of all odd integers from 1 through n.
Your task is to step into Aryan’s shoes and automate this little ritual.
Input Format:
A single integer
Output Format:
A single integer: the sum of all odd numbers from 1 to n
'''
