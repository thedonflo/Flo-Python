# Write a function called speak  that accepts a single parameter, animal.

# If animal is "pig", it should return "oink".
# If animal is "duck", it should return "quack".
# If animal is "cat", it should return "meow"
# If animal is "dog", it should return "woof"
# If animal is anything else, it should return "?"
# If no animal is specified, it should default to "dog"


def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"


speak()  # "woof"
speak("pig")  # "oink"
speak("duck")  # "quack"
speak("cat")  # "meow"
speak("dog")  # "woof"
speak("banana")  # "?"
