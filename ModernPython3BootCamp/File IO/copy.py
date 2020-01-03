# copy
# Write a function called copy, which takes in a file name and a new file name and
# copies the contents of the first file to the second file.
#
# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland
# to give you some sample text to work with. This is also the text used in the tests.


def copy(file1, file2):
    with open(file1, encoding="utf-8") as readfile:
        with open(file2, 'w') as writefile:
            for lines in readfile:
                writefile.write(lines)


print(copy('story.txt', 'story_copy.txt')) # None
# expect the contents of story.txt and story_copy.txt to be the same

