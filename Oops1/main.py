class Animal():
    def Animal_sound(self):
        print("Animal makes a sound")

class Pig(Animal):
    def Animal_sound(self,name):
        print("Pig says: WEE WEE"+name)


class Dog(Animal):
    def Animal_sound(self):
        print("Dog says: bhoo bhoo")

a=Animal()
b=Pig()
c=Dog()

a.Animal_sound()
b.Animal_sound("leo")
c.Animal_sound()