
def main():
    word = input("word: ")
    newWord = shorten(word)

    print(newWord)
   

def shorten(word):
    list = {'a','e','i','o','u'}
    upperList = {x.upper() for x in list}
    newWord = ""

    for c in word:
        if c not in list and c not in upperList:
            newWord += c
    
    return newWord

if __name__ == "__main__":
    main()