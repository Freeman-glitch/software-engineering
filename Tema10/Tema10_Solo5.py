class AnimalError(Exception):
    pass

class Animal:
    def __init__(self, name, animal_type):
        if animal_type not in ["собака", "кошка"]:
            raise AnimalError(f"Неизвестный вид: {animal_type}")
        self.name = name
        self.type = animal_type
        self.hungry = True
        print(f"Создано: {name} ({animal_type})")

    def feed(self):
        if not self.hungry:
            raise AnimalError(f"{self.name} уже сыт")
        self.hungry = False
        print(f"{self.name} покормлен")

    def play(self):
        if self.hungry:
            raise AnimalError(f"{self.name} слишком голоден для игр")
        self.hungry = True
        print(f"{self.name} поиграл")

try:
    animal1 = Animal("Барсик", "кошка")
    animal2 = Animal("Шарик", "собака")

    animal1.feed()
    animal1.play()

    animal2.play()
except AnimalError as e:
    print(f"Ошибка! {e}")

try:
    animal3 = Animal("Рекс", "динозавр")
except AnimalError as e:
    print(f"Ошибка! {e}")

try:
    animal1.feed()
    animal1.feed()
except AnimalError as e:
    print(f"Ошибка! {e}")