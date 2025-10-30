# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    """
    A simple Dog class to learn OOP concepts
    
    Atrributes:
        breed-breed
        fur_color-fur color
        name
        age
    """
    def __init__(self, breed = "dog", fur_color = "brown", name = "no name", age = "1"):
        self.breed = breed
        self.fur_color = fur_color
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.fur_color} {self.breed}"

    def bark(self):
        return f"{self.name} says: Woof Woof!"

    def birthday(self):
        self.age += 1
        print(f"{self.name} is celebrating their {self.age} birthday!")
    
    def paint_dog(self, new_color):
        old_color = self.fur_color
        self.fur_color = new_color
        print(f"{self.name} hs changed their fur color from {old_color} to {new_color}")
if __name__ == "__main__":
    my_dog = Dog("weimaraner","brown", "marshmello", 5)
    berg_dog = Dog("labrador", "black", "logan", 9)
    matthew_dog = Dog(breed = "labrador", name = "bella", age = 1)
    default_dog = Dog()




    print(my_dog)
    print(berg_dog)
    print(default_dog)
    print(matthew_dog)
    
    print()

    print(my_dog.bark())
    matthew_dog.birthday()
    my_dog.paint_dog("neon yellow")