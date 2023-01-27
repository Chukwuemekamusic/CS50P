import random
import sys


countGood = 0
countQ = 0

def main():
    n = get_level("Level: ")
    while True:
        global countQ
        x, y = generate_integer(n)
        result = solve(x, y)
        countQ += 1
        if result:
            print("Correct!")
        else:
            print("Incorrect.")
            print(x+y)
        if countQ == 10:
            sys.exit(f"Score: {countGood}")
            

def get_level(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n == 1 or n == 2 or n == 3:
                return n
            else:
                pass
        except ValueError:
            pass

def generate_integer(n):
    match n:
        case 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        case 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        case 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        
    return x, y

def solve(x, y):
    countE = 0
    global countGood
    while True:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer != x + y:
                countE += 1
            else:
                countGood += 1
                return True
        except ValueError: 
            print("EEE")
            countE += 1
        
        if countE == 3:
            return False
    

if __name__ == "__main__":
    main()
