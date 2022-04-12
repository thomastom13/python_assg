import datetime
def agecal(y,m,d):
    today=datetime.datetime.now().date()
    dob=datetime.date(y,m,d)
    age=int((today-dob).days/365.25)
    print(age,"Years")
agecal(2001,12,10)
# h=datetime.datetime.now().date()
# print(h)
# t=datetime.date(2001,12,10)
# print(t)
# print(int((h-t).days/365.25))