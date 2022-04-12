class parent:
    name="Ram"
    def over_fun(self):
        print("The overrided method")
    def ano_fun(self):
        print("Another method")
class child(parent):
    name1="Kumar"
    def over_fun(self):
        print("The overrided function is :")

obj=child()
# obj.name1="RAM kumaer"
print("name Change",obj.name1)
obj.over_fun()
obj.ano_fun()
# def over_fun(name):
#     name="Kumar"
#     print("The name of over_fun1 is: ",name)
# def over_fun(name):
#     name="Kumar1"
#     print("The name of over_fun2 is: ",name)
# name="ram"
# over_fun(name)