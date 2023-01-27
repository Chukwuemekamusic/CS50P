import re
import sys

def main():
    print(count(input()))

def count(s):
    um_list = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(um_list)

if __name__ == "__main__":
    main()