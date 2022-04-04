# 7.Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n.
num=int(input("Enter the Number: "))
sum=0
for i in range(1,num+1):
    sum=sum+(i/i+1)
print("The value is:",sum)