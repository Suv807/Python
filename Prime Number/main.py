class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Display(self):
        print(f"the name is {self.name}")
        print(f"the name is {self.age}")

class Student():
    def __init__(self,name,age,section):
        self.section=section
        self.name = name
        self.age = age
    def Display_student(self):
        print(f"the name is {self.name}")
        print(f"the name is {self.age}")

        print(f"the name is {self.section}")

student=Person("Ravi kumar",28)
student.Display()
print("*******************************")

my=Student("L",9,"M")
my.Display_student()