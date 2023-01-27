import csv
import os
import sys

old_file_path = sys.argv[1]
new_file_path = sys.argv[2]

filename, file_extension = os.path.splitext(old_file_path)
if file_extension != ".csv":
    sys.exit("Old file is not a CSV file")

filename, file_extension = os.path.splitext(new_file_path)
if file_extension != ".csv":
    sys.exit("New file is not a CSV file")

old_file_data = []

with open(old_file_path) as old_file:
    reader = csv.DictReader(old_file)
    for row in reader:
        old_file_data.append(row)

new_file_data = []
for row in old_file_data:
    name = row['name']
    last, first = name.split(",")
    new_file_data.append({"first": first.lstrip(), "last": last, "house": row['house']})

fieldnames = ["first","last","house"]

with open(new_file_path, "w") as new_file:
    writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in new_file_data:
        writer.writerow(row)
