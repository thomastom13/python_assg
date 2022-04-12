class parent():
    def __init__(self,name1):
        self.name='Default constructor'
        self.name1=name1
        # self.dept=dept
        # print("Hello Init")
    def display(self):
        print(self.name,self.name1)
obj=parent("heen")
obj.display()
#     def par_fun(self):
#         print("This is parent Function",self.name)
# class child(parent):
#     def chi_fun():
#         print("This is child Function")
# obj=child("hena")
# obj.par_fun()
# child.chi_fun()
# parent.par_fun("Helen")
# obj=parent()
# obj1=child()
# obj.par_fun()
# obj1.chi_fun()

