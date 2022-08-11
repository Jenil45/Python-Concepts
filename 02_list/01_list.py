# List are used to store value with any data type in one container

# declaring list
mylist = [45 , "Jenil" , bool , 93.18 , 7 , (12,18,24)]                         # we can store any dataype like int , string , boolean , float and tuples too.

#printing the list
print(mylist)                                                                   # will output this : [45, 'Jenil', <class 'bool'>, 93.18, 7, (12, 18, 24)]

# we can do indexing of list
# we can slice the list
print(mylist[2:5])

# we can also change or update the list
mylist[2] = true

# Lists methods
l1 = [1,8,7,2,21,15 ]

# list.sort()     ---->    sorting of list
l1_sorted = l1.sort()
print(l1)                        # on l1.sort() our real l1 is sort

# l.reverse()      ----> reverse an list
l1_reverse = l1.reverse()
print(l1)

# l.append(number)         ----> add number at end
l1_append = l1.append(45)
print(l1)

# l.insert(3,8)        ----> add 8 at 3rd index
l1_insert = l1.insert(3,8)
print(l1)

# l.pop(2)             ----> will delete a number at index 2
l1_pop = l1.pop(4)
print(l1)

# l.remove(21)         ----> remove 21 from last
l1_remove = l1.remove(21)
print(l1)
