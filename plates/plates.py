noList = []


def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    length = len(plate)
    if length > 6 or plate[0:2].isdigit() or length < 2 or not plate.isalnum():
        return False
    elif plate.isalpha():
        return True
    else:
        count = 0
        countNotNo = 0
        for i in plate:
            if i.isdigit():
                count += 1
            if count > 0:
                try:
                    noList.append(int(i))
                except:
                    countNotNo += 1

        if countNotNo != 0 or noList[0] == 0:
            return False
        else:
            return True

if __name__ == "__main__":
    main()
