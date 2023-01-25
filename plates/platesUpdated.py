
noList = []


def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    length = len(plate)
    if length <= 6 and plate[0:2].isalpha() and length >= 2 and plate.isalnum():
        for i in plate:
            if i.isdigit():
                index =  plate.index(i)
                if plate[index: ].isdigit() and int(i) != 0:
                    return True
                else:
                    return False
        return True
    else:
        return False


main()
