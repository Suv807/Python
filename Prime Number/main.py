class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Display(self):
        print(f"The name of the person is{self.name}")
        print(f"The age of the person is{self.age}")

class Student(Person):
    def __init__(self,name,age,section):
        self.section=section
        #Person.__init__(name,age);
        super().__init__(name,age);

    def Display_student(self):
        a=self.Display()
        print(f"The section is{self.section}")

b=Student("Ram",16,"B")
b.Display_student()

