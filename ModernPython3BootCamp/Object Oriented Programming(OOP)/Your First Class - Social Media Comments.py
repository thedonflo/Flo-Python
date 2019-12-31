# Your First Class - Social Media Comments
# It's time to define your own class! Suppose we're creating a social network application where users can comment on posts and photos.
#
# Create a class called Comment .  Each comment should have the following attributes:
#
# username  - the username of the person who created the comment (like "bluethecat")
# text  - the actual comment itself (like "omg so cute!" or "hahah")
# likes  - the number of likes the comment has.  Likes should default to 0.
# The following code should work:
#
# c = Comment("davey123", "lol you're so silly", 3)
# c. username       #"davey123"
# c. text           #"lol you're so silly"
# c.likes           #3
# another_comment = Comment("rosa77", "soooo cute!!!")
# another_comment.username        #"rosa77"
# another_comment.text            #"soooo cute!!!"
# another_comment.likes           #0
# Hints:
#
# __init__ is like any other function.  To add a default value for a parameter, just use the equals sign =.
# Remember that your default parameters need to come at the end!


class Comment:

    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


c = Comment("davey123", "lol you're so silly", 3)
print(c. username)       #"davey123"
print(c. text)           #"lol you're so silly"
print(c.likes)           #3
another_comment = Comment("rosa77", "soooo cute!!!")
print(another_comment.username)        #"rosa77"
print(another_comment.text)            #"soooo cute!!!"
print(another_comment.likes)           #0

