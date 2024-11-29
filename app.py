import requests

def get_joke():
    # URL de l'API JokesAPI
    url = "https://v2.jokeapi.dev/joke/Any"

    try:
        # Faire une requête GET à l'API
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a réussi
        joke_data = response.json()

        # Vérifie si la réponse contient le type de blague
        joke_type = joke_data.get("type", "unknown")

        # Gestion des différents types de blagues
        if joke_type == "single":
            joke = joke_data.get("joke", "No joke found.")
            print(f"Joke: {joke}")
        elif joke_type == "twopart":
            setup = joke_data.get("setup", "No setup found.")
            delivery = joke_data.get("delivery", "No delivery found.")
            print(f"Setup: {setup}")
            print(f"Delivery: {delivery}")
        else:
            print("Unknown joke format received.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    get_joke()
