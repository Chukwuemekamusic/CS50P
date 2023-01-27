import re

name = input("What's your name? ").strip()

if"," in name:
    last, first = name.split(",")
    name1 = f"{first.strip()} {last}"
print(f"hello, {name1}") 

#using the walrus operator :=
if matches:= re.search(r"^(.+), *(.+)$", name):
    name2=matches.group(2) + " " + matches.group(1)
print(f"hello, {name2}")
