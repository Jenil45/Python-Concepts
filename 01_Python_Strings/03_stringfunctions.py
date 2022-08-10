story = "once upon a time there is one player"

# String Functions
print(len(story))                            # return length of a string

print(story.endswith("abc"))                 # if yes than return true else false
print(story.endswith("player"))              # return true

print(story.count("o"))                      # return how many times o is printed
print(story.count("er"))                     # return 2

print(story.capitalize())                    # make capital the first letter of string

print(story.find("player"))                  # return first occurence of that written

print(story.replace("once","now"))           # return replaced word string

print(story.encode())                        # this method encodes the string using the specified encoding 

print(story.format(time=12))                 # formats the specified value(s) and insert them inside the string's placeholder

print(story.islower())                       # method returns True if all the characters are in lower case, otherwise False.

print(story.split())                         # this method splits a string into a list.

print(story.title())                         # in this method returns a string where the first character in every word is upper case
