#Simple text inverter logic in python

words = ("I support open source with Hacktoberfest !")
splitted = words.split()
inv = []
x = len(splitted) - 1
while x >= 0:
    inv.append(splitted[x]) 
    x = x-1
result=" ".join(inv)
print (result)
