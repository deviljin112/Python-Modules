import requests


def main():
    arg = input("Please enter your PostCode.\nOr say 'random'.\n=> ")

    if arg == "random":
        link = "http://api.postcodes.io/random/postcodes"
    else:
        link = f"http://api.postcodes.io/postcodes/{arg}"

    r = requests.get(link)
    status = r.status_code
    r_json = r.json()

    display_info = ["postcode", "longitude", "latitude"]

    if status == requests.codes.ok:
        for i in display_info:
            print(f"{i.capitalize()}: {r_json['result'][i]}")
    else:
        print(r_json["error"])


if __name__ == "__main__":
    main()