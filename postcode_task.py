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

    if status == requests.codes.ok:
        for k, v in r_json["result"].items():
            if isinstance(v, dict):
                print(f"{k.capitalize()}:")
                for x, y in v.items():
                    print(f"    {x.capitalize()}: {y}")
            else:
                print(f"{k.capitalize()}: {v}")
    else:
        print(r_json["error"])


if __name__ == "__main__":
    main()