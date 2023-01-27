import sys
import csv
from tabulate import tabulate
import os

menu = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".csv")==False:
    sys.exit("Not a csv file")

if not sys.argv[2] in ["r", "a"]:
    sys.exit("second command not known")

if sys.argv[2] == "r":
    try:
        with open(sys.argv[1]) as file:
            # Create a DictReader object
            reader = csv.DictReader(file)

            # Get the field names from the DictReader object
            field_names = reader.fieldnames

            # Create a list of lists to store the rows of the table
            rows = []

            # Iterate over the rows
            for row in reader:
                # Extract the values from the row dictionary and append them to the rows list
                rows.append([row[field] for field in field_names])

            # Print the table using tabulate
            print(tabulate(rows, headers=field_names, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File not found")
    print(rows)


if sys.argv[2] == "a":
    if not os.path.exists(sys.argv[1]):
        sys.exit("File not found")
    pizza = input("Pizza: ")
    small = input("Small: ")
    large = input("Large:")
    try:
        with open(sys.argv[1], "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Regular Pizza", "Small", "Large"])
            # writer.writerheader()

            writer.writerow({"Regular Pizza": pizza, "Small": small, "Large": large})
    except FileNotFoundError:
        sys.exit("File not found")
