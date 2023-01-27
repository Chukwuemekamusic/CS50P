from validator_collection import validators, errors


def main():
    print(validate(input("Email address: ")))


def validate(s):
    try:
        response = validators.email(s)
        if response:
            return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
