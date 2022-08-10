greeting = "Goed Morning, "
name = "Jenil"

#Concatinating two strings
c = greeting+name   
print(c)                                           # print Good Morning, Jenil

#slice string
print(name[2])                                                          # print 2 index character
print(name[0:3])                                                        #print characters from 0 to 2 ==> Jen
print(name[:4])                           #same as name[0:4]            # take minimum index (0)
print(name[0:])                           #same as name[0;length]       # take maximum index (0)

# name[3] = "d"   ----> doesn't work we can't change the element...............................

#Negative indices

print(name[-4:-1])                        #print "eni"                 # same as name[1:4]

#Slicing with skip value
d = name[1:4:1]                              # it means 1 to 4 print and print every 1 element so eni
print(d)

e = greeting[1::3]                              # it means 1 to 4 print and print every 3 element so o rn
print(e)