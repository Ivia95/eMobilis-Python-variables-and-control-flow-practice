# Base class
class Animal:
    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")

# Subclass
class Dog(Animal):
    def bark(self):
        print("Barking...")

# Create an instance of Dog
my_dog = Dog()

# Using inherited methods
my_dog.eat()
my_dog.sleep()

# Using the new method
my_dog.bark()
