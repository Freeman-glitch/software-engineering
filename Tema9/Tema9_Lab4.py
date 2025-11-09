class Mammal:
    classname = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'

dog = Dog()
print(f"Dog is {dog.classname}, but they say {dog.sounds}")
cat = Cat()
print(f"Cat is {cat.classname}, but they say {cat.sounds}")
