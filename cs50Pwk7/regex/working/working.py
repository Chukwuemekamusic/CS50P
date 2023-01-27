import re 
import sys


def main():
    print(convert(input("Hours: ")))


def add_zero(s):
        if s < 10:
            return f"0{s}"
        return f"{s}"

def convert(s):
    if matches:= re.search(r"(\d{1,2}(?:\:\d{1,2})?) (AM|PM) to (\d{1,2}(?:\:\d{1,2})?) (AM|PM)", s):
        if ":" in matches.group(1):
            Hr_first, Mn_first = matches.group(1).split(":")
            timeHr_first = int(Hr_first)
            timeMn_first = int(Mn_first)
        else:
            timeHr_first = int(matches.group(1))
            timeMn_first = 0
            Mn_first = "00"
        if ":" in matches.group(3):
            Hr_second, Mn_second = matches.group(3).split(":")
            timeHr_second = int(Hr_second)
            timeMn_second = int(Mn_second)
        else:
            timeHr_second = int(matches.group(3))
            timeMn_second = 0
            Mn_second = "00"
        if timeHr_first<=12 and timeMn_first<60 and timeHr_second<=12 and timeMn_second<60:
            if matches.group(2) == "PM" and timeHr_first != 12:
                timeHr_first = timeHr_first + 12
            elif matches.group(2) == "AM" and timeHr_first == 12:
                timeHr_first = 0
            if matches.group(4) == "PM" and timeHr_second != 12:
                timeHr_second = timeHr_second + 12
            elif matches.group(4) == "AM" and timeHr_second == 12:
                timeHr_second = 0
            new_format = f"{add_zero(timeHr_first)}:{Mn_first} to {add_zero(timeHr_second)}:{Mn_second}"
            return new_format
    raise ValueError
    #return False

    
        


if __name__ == "__main__":
    main()