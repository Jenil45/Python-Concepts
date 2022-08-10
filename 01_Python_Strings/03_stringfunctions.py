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