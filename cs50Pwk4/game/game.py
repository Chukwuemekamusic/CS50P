import random
import sys

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            pass
    
    randomNo = random.randint(1,n)
    while True:
        try:
            guessNo = int(input("guess number: "))
            guess(guessNo, randomNo)
        except ValueError:
            pass
            

def guess(guessNo, randomNo):
    if guessNo < randomNo:
        print("Too small!")
    elif guessNo > randomNo:
        print("Too large!")
    else: 
        sys.exit("Just right!")

    
if __name__ == "__main__":
    main()

