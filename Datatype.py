

number = 67 #integer
second = 34.56 #float
greeting = "Hello world" #string
isPythonInteresting = True #Boolean

#Data structures - multiple values in a single variable
cars = ["Toyota","Nissan","vw"] #List are ordered and changeable
fruits = ("apple","banana","cherry") #Turple - Ordered but unchangeable
countries = {"kenya","Tunisia","Algeria"} #set - unordered and unchangeable
student = {
    "firstname": "John",
    "lastname": "Smith",
    "age" : 20,
    "course" : "wed Development",
    "gender" : "Male"
} #Dictionery - key-value pair

print(cars)
print(fruits)
print(countries)
print(student["firstname"])

print(number)
print(second)
print(isPythonInteresting)


#Determing a Datatype
print(type(greeting))
print(type(number))
print(type(second))


#Typecasting - converting from one datatype to another
print(float(number))
print(int(second))