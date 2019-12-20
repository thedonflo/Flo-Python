from pyfiglet import figlet_format
from termcolor import colored
import requests
from random import choice


def print_art():
    color = "magenta"           # define color for graphic
    msg = "Dad Joke 3000"       # define message
    print(colored(figlet_format(msg), color = color))  # combine functions


def dad_jokes(search):
    url = "https://icanhazdadjoke.com/search"

    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": search}
    )
    data = response.json()
    joke_count = data.get('total_jokes')
    if joke_count > 1:
        print(f"I've got {joke_count} jokes about {search}. Here's one")
        print(choice(list(map(lambda word: word['joke'], data['results']))))
    elif joke_count == 1:
        print(f"I've got one joke about {search}. Here it is ")
        print(choice(list(map(lambda word: word['joke'], data['results']))))
    else:
        print(f"Sorry I don't know any jokes about {search}! Please try again")


print_art()
dad_jokes(input("Let me tell you a joke! Give me a topic: "))
