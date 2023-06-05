import re

string = "we had class on regular expressions\nThis is a python class.\nThe class is at 10pm IST"
print(string)

reg = re.compile("This")
print("\nworking on ^ - beginning with")
print("The matched string is %s" % (reg.match(string)))

print("The searched string is %s" % (reg.search(string)))
print(reg.search(string).group())
print()

reg = re.compile("^This")
print("\nworking on ^ - beginning with")
print("The matched string is %s" % (reg.match(string)))

print("The searched string is %s" % (reg.search(string)))
# print(reg.search(string).group())
print()

reg = re.compile("^This", re.M)
print("compiled regex object is ", reg)

print("\nworking on ^ - beginning with")
print("The matched string is %s" % (reg.match(string)))

print("The searched string is %s" % (reg.search(string)))
print(reg.search(string).group())
print()
