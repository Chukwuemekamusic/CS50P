import re

email = input("email?: ")

# # this allows only one dot after the @ sign
# if re.search(r"^[^@]+@[^@.]+\.[^@.]+$", email):
#     print("Valid")
# else:
#     print("Invalid")



# """this allows only alpha numeric character and ends with .edu"""
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu+$", email):
#     print("Valid")
# else:
#     print("Invalid")


"""much improved alpha numeric code"""
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|gov)+$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")




