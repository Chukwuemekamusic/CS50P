import csv
import sys


oldFile = []
newFile = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".csv")==False or sys.argv[2].endswith(".csv")==False:
    sys.exit("not a csv file")

try:
    with open(sys.argv[1]) as file:
        readerDict =  csv.DictReader(file)

        for row in readerDict:
            oldFile.append(row)

except FileNotFoundError:
    pass

#edit the names
fieldnames = ["first","last","house"]
for file in oldFile:
    name = file['name']
    last, first = name.split(",")
    newFile.append({"first":first.strip(),"last":last.strip(),"house":file['house']})

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in newFile:
        writer.writerow(row)
