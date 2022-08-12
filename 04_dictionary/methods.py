# Dictionary methods

a = {
    "name"  : "Jenil",
    "from"  : "India",
    "marks" : [92,98,96]
}

# 1) a.items()  ---> returns a list of (key,value) tuples
print(a.items())                  # print dict_items([('name', 'Jenil'), ('from', 'India'), ('marks', [92, 98, 96])])
print(type(a.items()))            # print <class 'dict_items'>
print(list(a.items()))            # [('name', 'Jenil'), ('from', 'India'), ('marks', [92, 98, 96])]

# 2) a.keys() ---> returns a list containing dictionary's key
print(a.keys())                   # dict_keys(['name', 'from', 'marks'])           , also there is method of a.value()
print(type(a.keys()))             # <class 'dict_keys'>
print(list(a.keys()))             # ['name', 'from', 'marks']

# 3) a.update({"ferind" : "Rohit"})  ---> update dictionary with supplied key-value pair
a.update({"freind" : "Rohit"})
print(a["freind"])

# 4) a.get("name")  ---> return value of specified key (return a value)
print(a.get("marks"))             # [92,98,96]

# Difference between .get and [] syntax in the dictionary
print(a.get("name2"))             # not throw an error print none
# print(a["name2"])       throws an error
