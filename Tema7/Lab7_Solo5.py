import random


def get_quote_of_the_day():
    try:
        with open("Solo75.txt", "r", encoding="utf-8") as file:
            quotes = file.readlines()

        if quotes:
            quote_line = random.choice(quotes).strip()
            quote, author = quote_line.split("|")
            print(f"«{quote}»")
            print(f"— {author}")
        else:
            print("Цитаты не найдены!")

    except FileNotFoundError:
        print("Создайте файл Solo75.txt с цитатами!")


def add_quote_simple():
    quote = input("Цитата: ")
    author = input("Автор: ")

    with open("Solo75.txt", "a", encoding="utf-8") as file:
        file.write(f"{quote}|{author}\n")
    print("Цитата сохранена!")

print("1 - Получить цитату дня")
print("2 - Добавить цитату")
choice = input("Выберите: ")

if choice == "1":
    get_quote_of_the_day()
elif choice == "2":
    add_quote_simple()