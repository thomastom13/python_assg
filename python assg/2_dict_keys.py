# 2.Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
#  and the values are square of keys. The function should just print the keys only.
# dict1={}
# dict2={2:3,3:2}
def dict_sq():
    for i in range(1,21):
        dict1={i:(i*i)}
        # print(list(dict1.keys()),end=",")
        # print(list(dict1.keys()))
        # return list(dict1.keys())
        print(list(dict1.keys()),end=",")
        # return {i:i*i for i in range(1,n+1)}
   
dict_sq()
# print(val)
# for i in range (0,len(val)):
#     print((val.keys()))

