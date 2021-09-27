# oop
# Object oriented programming 

# Class : A blue-print of an object. It's a logical entity. A class can have data members and member methods
# Object : An instance of a class.  # hint: instance=> an example or single occurrence of something.
# Methods : A function inside a class is called method. 
# Inheritance : is-a relation between 2 or more classes. for example: Human is an Animal.
# Polymorphism : having many forms. 
# Abstraction : Hiding implementation and showing only functionality. 
# Encapsulation : Wrapping up of data.
# aggregation : has-a relation. for example : Shikha has a Laptop


# Types of Vaiable in class
# 1. Class Variable
# 2. Instance Variable
# 3. Member variable


# define a class
class Animal:
	desc = "I am an animal" # class variable
	name = "Shikha"

	def __init__(self, name, age): # constructor initialize an object, helps in memory assignment
		self.name = name # instance variable
		self.age = age


name = "CMpundhir" # input("Enter your name: ")
age = 12 # input("ENter your age: ")


a1 = Animal(name, age) # object creation
a2 = Animal("Ram", 34)

print(a1.__dict__)
print(a2.__dict__)


print(Animal.desc)
print(Animal.name)

a1.fav_food = "Pedigree"
print(a1.__dict__)

del a1.fav_food
print(a1.__dict__)