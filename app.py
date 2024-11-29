import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"

    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()

        if joke_data.get("type") == "single":
            print(f"joke: {joke_data.get('joke')}")

        else:
            print(f"setup: {joke_data.get('setup')}")
            print(f"delevery: {joke_data.get('delevery')}")

    except requests.exceptions.RequestException as e:
        print("An error occurred: {e}")

if __name__== "__main__":
    get_joke()
