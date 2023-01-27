import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if address:= re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        if int(address.group(1))<=255 and int(address.group(2))<=255 and int(address.group(3))<=255 and int(address.group(4))<=255:
            return True
    return False



if __name__ == "__main__":
    main()