#!/bin/python3

import sys

def timeInWords(h, m):
    hour=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
    minute=[
                                                                                                    'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','quarter','sixteen',
        'seventeen','eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four','twenty five','twenty six',
        'twenty seven','twenty eight','twenty nine','half']
    if m==0:
        return("{} o' clock".format(hour[h-1]))
    elif m>=1 and m<=9:
        return("%s minute past %s" %((minute[m-1]),(hour[h-1])))
    elif m==15 or m==30:
        return("%s past %s" %(minute[m-1],hour[h-1]))
    elif m>=10 and m<30:
        return("%s minutes past %s" %((minute[m-1]),(hour[h-1])))
    elif m==45:
        return("quarter to %s" %(hour[h]))
    else:
        return("%s minutes to %s" %(minute[60-(m+1)],hour[h]))
        
    # Complete this function

if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)
