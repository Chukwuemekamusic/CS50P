import sys


def main():
    while True:
        fraction = input("Fraction: ")

        percentage = convert(fraction)
        # print(percentage)
        if percentage == False:
            continue
        else:
            break

    print(gauge(percentage))


def convert(fraction):
    split = fraction.split("/")
    
    try:
        if len(split) !=2:
            raise ValueError
        x = int(split[0])
        y = int(split[1])
        if y >= x:
            percentage = round((x / y) * 100)
            return percentage
        elif y == 0:
            raise ZeroDivisionError
        else:
            raise ValueError

    except (ValueError, ZeroDivisionError):
        return False


def gauge(percentage):

    if percentage >= 99:
        return "F"

    elif percentage <= 1:
        return "E"

    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
