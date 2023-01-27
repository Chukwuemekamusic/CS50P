from pyfiglet import Figlet
import sys
import random

figlet =  Figlet()

if len(sys.argv) == 1:
    text = input("Text: ")
    f = random.choice(figlet.getFonts())
    figlet.setFont(font = f)
    print(figlet.renderText(text))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    try:
        #f = sys.argv[2]
        figlet.setFont(font = sys.argv[2])

    except:
        sys.exit("Invalid usage")

    else:
        text = input("Text: ")
        print(figlet.renderText(text))

else:
    sys.exit("Invalid usage")
