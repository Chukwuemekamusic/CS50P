word = input("word: ")
list = {'a','e','i','o','u'}
upperList = {x.upper() for x in list}
newWord = ""

for c in word:
    if c not in list and c not in upperList:
        newWord += c

print(newWord)
print(upperList)