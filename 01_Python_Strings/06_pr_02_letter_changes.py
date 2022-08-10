# Practise set 3 - problem 2

letter = ''' Dear <|Name|>,
You are selected
<|Date|>'''

letterupdate = letter.replace("<|Name|>",input())
letterupdate1 = letterupdate.replace("<|Date|>" , input())
print(letterupdate1)
