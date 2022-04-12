import array as arr
a=arr.array('i',range(3))
x=int(input("Enter the 3 digit number: "))
a[0]=int(x%10)
a[1]=int(x/10%10)
a[2]=int(x/100)
for i in range(0,3):
    if a[i]==0:
        print("Zero")
    elif a[i]==1:
        print("One")
    elif a[i]==2:
        print("Two")
    else:
        print("ni")
