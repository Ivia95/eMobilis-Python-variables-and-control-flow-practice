# Define the Cat class
class Cat:
    def make_sound(self):
        print("Meow")

# Define the Dog class
class Dog:
    def make_sound(self):
        print("Woof")

# Define a function that takes an object and calls make_sound()
def animal_sound(animal):
    animal.make_sound()

# Create instances of Cat and Dog
my_cat = Cat()
my_dog = Dog()

# Demonstrate polymorphism
animal_sound(my_cat)  # Output: Meow
animal_sound(my_dog)  # Output: Woof
