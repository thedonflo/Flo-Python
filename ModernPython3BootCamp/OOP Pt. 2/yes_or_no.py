# yes_or_no
# Write a function called yes_or_no, which returns a generator that first yields yes ,
# then no , then yes , then no , and so on.

# gen = yes_or_no()
# next(gen) # 'yes'
# next(gen) # 'no'
# next(gen) # 'yes'
# next(gen) # 'no'


def yes_or_no():
    response = ["yes", "no"]
    i = 0
    while i < len(response):
        yield response[i]
        if response[i] == "no":
            i = 0
        else:
            i += 1


gen = yes_or_no()
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
print(next(gen)) # 'yes'
print(next(gen)) # 'no'