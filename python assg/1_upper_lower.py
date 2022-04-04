# 1.Write a program that accepts a sentence and calculate
#  the number of upper case letters and lower case letters and 
# calculate the number of letters and digits.

def strings(s):
    d={"UPPERCASE":0,"LOWERCASE":0,"DIGIT":0,"LETTERS":0}
    for c in s:
        if c.isupper():
            d["UPPERCASE"]+=1
        elif c.islower():
            d["LOWERCASE"]+=1
        elif c.isdigit():
            d["DIGIT"]+=1
        elif len(c):
            sp=len(s)-s.count(' ')
            d["LETTERS"]+=sp
        else:
            pass
    print("THe origial String: ",s)
    print("No. of Upper cases: ",d["UPPERCASE"])
    print("No. of Lower cases: ",d["LOWERCASE"])
    print("No. of Digits: ",d["DIGIT"])
    print("No. of Letters: ",d["LETTERS"])
s=input("Enter the string: ")
strings(s)