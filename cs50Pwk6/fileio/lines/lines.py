import sys

lines = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".py")==False:
    sys.exit("Not a python file")

try:
    with open(sys.argv[1]) as file:
        move = True
        for line in file:
            if line.rstrip().startswith("#") or len(line.rstrip())==0 :
                continue
            if line.rstrip().startswith('"""'):
                if line.rstrip().endswith('"""'):
                    continue
                move = False
                continue

            if move == False:
                if line.rstrip().endswith('"""'):
                    move = True
                    continue
                else: 
                    continue  
            
            lines.append(line.rstrip())

except FileNotFoundError:
    raise

print(len(lines))

