from Datatype import greeting
from variables import firstname

text = "Hello there"
course = "WEB DEVELOPMENT"

print(text)

#accessing an element in a string
print(text[6])

#size/length of a string
print(len(text))

#modifing a string
print(course.lower())
print(text.upper())

#string concatenation - joining strings
greeting = "hello"
firstname = "xai"

print(greeting + firstname)
print(greeting + " " + firstname)