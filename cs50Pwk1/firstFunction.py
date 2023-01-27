def main():
    name = input("what is your name: ")
    hello(name)

    x = int(input("what is x: "))
    print(f"x tripled is {triple(x)}")



def hello(name="world"):
    print("hello, ", name)

def triple(n):
    return pow(n, 3)

main()