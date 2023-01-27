import sys
import csv
from tabulate import tabulate

lines = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".csv")==False:
    sys.exit("Not a csv file")

try:
    with open(sys.argv[1]) as file:
        reader =  csv.reader(file)

        for line in reader:
            header = line
            break
        
        print(tabulate(reader, headers=header, tablefmt="grid"))
        
except FileNotFoundError:
    raise