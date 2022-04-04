# 3.Define a function which can generate and 
# print a tuple where the value are square of numbers between 1 and 20 (both included).

def tup_sq():   
    t=[]
    for i in range(1,21):
        t.append(i*i)
    print(tuple(t))
tup_sq()