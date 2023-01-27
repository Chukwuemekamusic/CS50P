name = input("title: ")
newName = ""

for c in name:
    if c.isupper():
        newName += "_"+c.lower()
    else:
        newName += c

print (newName)