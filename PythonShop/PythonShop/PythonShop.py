class Person:
	name = "Ivan"
	age = 10

	def set(self, name, age):
		self.name = name
		self.age = age

class Student (Person):
	course = 1

igor = Student ()
igor.set("Igor", 19)
print (igor.name, igor.age)

vlad = Person ()
vlad.set("Влад", 25)
print (vlad.name + " " + str(vlad.age))

ivan = Person ()
ivan.set ("Иван", 56)
print (ivan.name + " " + str(ivan.age))