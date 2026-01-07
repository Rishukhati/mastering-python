# This is a sample Python script.
from sympy import python

print(' Basic of python ')

# Arithmetic

addition = 32 + 54
print(addition)

multiplication = 32 * 54
print(multiplication)

division = 32 / 54   # if want division without decimal use //   (2.5 we say this type of number is floating point number )
print(division)

modulo = 32 % 54
print(modulo)

exponent = 2 ** 4
print(exponent)

# input()

# user_input = input('Enter a number: ')
# print('Your number is this :', user_input)

# Assigment operator

x = 5
x += 2
print(x)

# string is - single coat -''  Double coat-"" multiline string-''' '''
#concatenation -

str1 = 'yoooo this is'
str2 = 'rishabh'


print(str1 + ' ' + str2)

# string indexing and slicing

text = 'python'
first_char = text[0]
substring = text[1:4]
print(first_char + substring)

# string length
str_length = 'pythin'
my_length = len(str_length)
print(my_length)
# or
print(len('this is a apple'))

# string formatting

name = 'huxn'
age = 20

formatted_string = f'My name is {name} and I am {age} years old'
print(formatted_string)

# Escape characters     not use too much

escaped_string = ('this is a line \n this is a new line')
print(escaped_string)


# if want to know a type on any variable use type()

name = 'rishabh'
print(type(name))

#  String methods

# str.upper() and str.lower()
## str.capitalize() and str.title()
## str.startswith(prefix) and str.endswith(suffix)
## str.replace(old, new)
## str.find(substring) and str.index(substring)
## str.split(separator)
## str.count(substring)























