# 8.The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Write a program using list comprehension to 
# print the Fibonacci Sequence in comma separated form with a given n input by console.

def f(n):
    if n<2:
        fibo[n]=n
        return fibo[n]
    fibo[n]=f(n-1)+f(n-2)
    return fibo[n]

n=int(input("Enter Number: "))
fibo=[0]*(n+1)  # initialize a list of size (n+1)
f(n)            # call once and it will set value to fibo[0-n]
fibo = [str(i) for i in fibo]  # converting integerdata to string type
ans = ",".join(fibo)  #join all string element of fibo with ',' character
print(ans)
