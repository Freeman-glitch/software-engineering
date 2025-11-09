class Tomato:
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
            print(f"Томат {self._index} перешел на стадию: {self.states[self._state]}")
        else:
            print(f"Томат {self._index} уже полностью созрел!")

    def is_ripe(self):
        return self._state == 3

class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        print(f"Собран урожай с {len(self.tomatoes)} томатов!")
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f"{self.name} ухаживает за растениями...")
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай!")
            self._plant.give_away_all()
            return True
        else:
            print(f"{self.name}: Томаты еще не созрели! Нужно продолжать ухаживать.")
            return False

    @staticmethod
    def knowledge_base():
        print("\n Справка по садоводству ")
        print("1. Помидор проходит 4 стадии созревания:")
        print("   - отсутствует")
        print("   - цветение")
        print("   - зеленый")
        print("   - красный (созрел)")
        print("2. Садовник должен ухаживать за растениями,")
        print("   пока все томаты не станут красными.")
        print("3. Собирать урожай можно только когда")
        print("   все томаты полностью созрели.\n")

# Тесты
if __name__ == "__main__":
    Gardener.knowledge_base()

    bush = TomatoBush(3)
    gardener = Gardener("Вячеслав", bush)

    print(f"Создан садовник: {gardener.name}")
    print(f"Создан куст с {len(bush.tomatoes)} томатами\n")
    print("  Первый день ухода  ")
    gardener.work()
    print("\n  Попытка сбора урожая  ")
    gardener.harvest()
    print("\n  Второй день ухода  ")
    gardener.work()
    print("\n  Третий день ухода ")
    gardener.work()
    print("\n   Сбор урожая  ")
    gardener.harvest()