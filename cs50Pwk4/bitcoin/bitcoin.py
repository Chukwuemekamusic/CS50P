import requests
import sys
import json

# sys.argv[1] must be a float
website = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    unit = getFloat()
    rate = getRate()

    amount = unit * rate
    print(f"${amount:,.4f}")


def getFloat():
    try:
        n = float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")

    return n


def getRate():
    try:
        response = requests.get(website).json()

    except requests.RequestException:
        sys.exit("link not available")

    # print(json.dumps(response, indent=2))
    rate = response["bpi"]["USD"]["rate"]
    return float(rate.replace(",", ""))


if __name__ == "__main__":
    main()
