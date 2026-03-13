import requests


def fetch_data(option):
    url = f"https://swapi.mimo.dev/api/{option}/"
    data = []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"Fetched Data: {len(data)}")
    except requests.HTTPError as e:
        print(f"Errors fetching data: {e}")
        return None
    return data


def main():
    option = input("Which StarWars data you would like to explore"
                   "i.e. planets, people, starships): ").strip().lower()
    data = fetch_data(option)
    if data:
        for entity in data:
            print(entity["name"])
    else:
        print("Unable to download data")


if __name__ == "__main__":
    main()
