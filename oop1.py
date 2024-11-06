from Datatype import student


class person:
# properties/variables/attributes/characteristics
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

# behavior/method/function
     def study(self):
         print("student is studying")

 #creating an object
student1 = person("hussein",20,"male")
print(student1.name)
student12 = person("jay",22,"male")
print(student12.name)
student3 = person("jane",23,"female")

