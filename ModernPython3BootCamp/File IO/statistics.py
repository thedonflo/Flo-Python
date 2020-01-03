# statistics
# Write a function called statistics, which takes in a file name and
# returns a dictionary with the number of lines, words, and characters in the file.
#
# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland
# to give you some sample text to work with. This is also the text used in the tests.)

# statistics('story.txt')
# {'lines': 172, 'words': 2145, 'characters': 11227}


def statistics(file1):
    with open(file1, encoding="utf-8") as readfile:
        fullread = readfile.readlines()
        stats = {'lines': len(fullread),
                 'words': sum(len(line.split(" ")) for line in readfile)
        }
    return stats

print(statistics('story.txt'))