# 10.With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

def remove_dups(lists):
    newlist=[]
    seen=set()
    for items in lists:
        if items not in seen:
            seen.add(items)
            newlist.append(items)
    return newlist
li=[12,24,35,24,88,120,155,88,120,155]
print(remove_dups(li))
