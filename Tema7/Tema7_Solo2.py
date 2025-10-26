import json
from datetime import datetime

try:
    with open("Solo72.txt", "r", encoding="utf-8") as f:
        expenses = json.load(f)
except:
    expenses = []

while True:
    print("\n1 - Добавить расход")
    print("2 - Посмотреть расходы")
    print("3 - Выход")

    choice = input("> ")

    if choice == "1":
        cat = input("Категория: ")
        summa = float(input("Сумма: "))
        desc = input("Описание: ")

        expenses.append({
            "дата": datetime.now().strftime("%d.%m.%Y"),
            "категория": cat,
            "сумма": summa,
            "описание": desc
        })

        with open("expenses.txt", "w", encoding="utf-8") as f:
            json.dump(expenses, f, ensure_ascii=False, indent=2)

    elif choice == "2":
        for exp in expenses:
            print(f"{exp['дата']} - {exp['категория']} - {exp['сумма']} руб. - {exp['описание']}")

    elif choice == "3":
        break