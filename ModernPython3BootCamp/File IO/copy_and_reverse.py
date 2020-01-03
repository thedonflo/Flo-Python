# copy_and_reverse
# Write a function called copy_and_reverse, which takes in a file name and a new file name and
# copies the reversed contents of the first file to the second file.
#
# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland
# to give you some sample text to work with. This is also the text used in the tests.)


def copy_and_reverse(file1, file2):
    with open(file1, encoding="utf-8") as readfile:
        with open(file2, 'w') as writefile:
            for lines in readfile:
                writefile.write(lines[::-1])



print(copy_and_reverse('story.txt', 'story_reversed.txt'))