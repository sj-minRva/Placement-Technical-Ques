def timeConversion(s):
    hour = int( s[0:2] )
    period = s[-2:]
    rest =  s[2:-2]

    if period == "PM":
        if hour != 12:
            hour = hour+12
    elif period == "AM":
        if hour == 12:
            hour = 00    
    print( f"{hour:02d}{rest}" )
 
s = "12:05:28 AM"
timeConversion(s)
