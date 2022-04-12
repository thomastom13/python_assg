#calculating the income in python using if statements

i=int(input("Enter the Income: "))

if (i<200000):
    print("No tax")
elif (i<400000 and i>200000):
    it=((i-200000)*(10/100))
    print(it)
elif(i<600000 and i>400000):
    it=(2000+((i-400000)*(20/100)))
    print(it)
else:
    it=(6000+((i-600000)*(40/100)))
    print(it)