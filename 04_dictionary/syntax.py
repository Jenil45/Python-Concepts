# Dictionary is a collection of key-value pairs

# Syntax: 
myDict = {   
    "Fast" : "In a quick manner",
    "Jenil" : "A person",
    "Rohit" : "A Cricketer",    
    "Marks" : [1,2,3],
    "anotherdict" : {'Harry' : 'coder'},
    "tuple" : (1,2,3)   
}

print(myDict['Fast'])                  # print In a quick manner
print(myDict['Jenil'])                 # print A person 
print(myDict['Rohit'])                 # print A Cricketer
print(myDict['Marks'])                 # print [1,2,3]
print(myDict["anotherdict"])           # print ['Harry' : 'coder']
print(myDict["anotherdict"]['Harry'])  # print  coder
print(myDict["tuple"])                 # print (1,2,3)

# Dictionary is unordered

# Dictionary is mutable (we can change value of key)
myDict["Marks"] = [5,6] 
print(myDict["Marks"])

# Dictionary is indexed
# Dictionary cannot contain duplicate keys
