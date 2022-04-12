# import statistics,math
# sample=[40,30]
# print(round(statistics.stdev(sample)))

import math
n=int(input("Enter the value: "))
weight=[]
s=0
for i in range(n):
    w=int(input("Enter the Weight: "))
    weight.append(w)
    s=s+w   #total weight
    print(s)
    print(weight)
average=int(s/n) #total weight/total number of weight
print(average)
d=0
for i in range(n):
    d=(weight[i]-average)**2
print(d)
sd=math.sqrt(d)
print("Standard Deviation is: ",sd)