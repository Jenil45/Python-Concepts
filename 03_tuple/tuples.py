# tuple is immutable(can't change) data type in python

# empty tuple
t1 = ()
print(t1)

# tuple with single element
t2 = (1,)
print(t2)                                  # wrong way is t2 = (1) it consider as a number

# creating a tuple using ()
t = (1,2,4,5)

# printing tuple elements
print(t[0])

# cannot update values of tuple
# t[0] = 34   it shows an error

# tuple methods

a = (1,7,2,1,5)

# a.count(1)    ----> it count number of times 1 occurs
print(a.count(1))

# a.index(1)    ----> will return a index of first occurence of 1 in a
print(a.index(5))
