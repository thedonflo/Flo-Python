# make_song
# Write a function called make_song, which takes a count and a beverage,
# and returns a generator that yields verses from a popular song about a the beverage.
# The number of verses in the song is determined by the count.
#
# Each verse of the song should involve one fewer beverage, until there are no beverages remaining.
# (Check the examples for details on the structure of the lyrics.)
#
# The default count should be 99, and the default beverage should be soda.

# kombucha_song = make_song(5, "kombucha")
# next(kombucha_song) # '5 bottles of kombucha on the wall.'
# next(kombucha_song) # '4 bottles of kombucha on the wall.'
# next(kombucha_song) # '3 bottles of kombucha on the wall.'
# next(kombucha_song) # '2 bottles of kombucha on the wall.'
# next(kombucha_song) # 'Only 1 bottle of kombucha left!'
# next(kombucha_song) # 'No more kombucha!'
# next(kombucha_song) # StopIteration


def make_song(count=99, beverage="soda"):
    for i in range(count, -1, -1):
        if i > 1:
            yield f"{i} bottles of {beverage} on the wall."
        elif i == 1:
            yield f"Only {i} bottle of {beverage} left!"
        else:
            yield f"No more {beverage}!"



kombucha_song = make_song(5, "kombucha")
print(next(kombucha_song)) # '5 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '4 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '3 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '2 bottles of kombucha on the wall.'
print(next(kombucha_song)) # 'Only 1 bottle of kombucha left!'
print(next(kombucha_song)) # 'No more kombucha!'
print(next(kombucha_song)) # StopIteration