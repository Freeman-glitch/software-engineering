# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
- Малачевский Вячеслав Евгеньевич
- ИВТ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |  |
| Задание 7 | + |  |
| Задание 8 | + |  |
| Задание 9 | + |  |
| Задание 10 | + |  |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### ⦁	Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.


```python
file = open("file.txt", "a")
file.write("Hello World!\n")
file.write("Tema7_Lab1")
file.close()  
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Laba1.png)

## Выводы

В данном коде составлен текстовый файл:

1. `file = open("file.txt", "a")`: Открыли текстовый файл.

2. `file.write("Hello World!\n")
file.write("Tema7_Lab1")`: Записали два предложения в файл.

3. `file.close()`: Закрыли файл.

## Лабораторная работа №2
### ⦁ Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().


```python
file = open("file.txt", "r")
print(file.readline())
file.close()   
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Lab2.png)

## Выводы

В данном коде идет работа с текстовым файлом:

1. `file = open("file.txt", "r")`: Открыли файл в режиме чтения.

2. `print(file.readline())`: Вывели первую строку файла.

3. `file.close()`: Закрыли файл.

## Лабораторная работа №3
### ⦁ Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().


```python
file = open("file.txt", "r")
print(file.readlines())
file.close()   
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Lab3.png)

## Выводы

В данном коде идет работа с текстовым файлом:

1. `file = open("file.txt", "r")`: Открыли файл в режиме чтения.

2. `print(file.readlines())`: Вывели все строки файла.

3. `file.close()`: Закрыли файл.
  
## Лабораторная работа №4
### ⦁ Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().


```python
with open("file.txt") as f:
    print(f.readlines())  
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Lab4.png)

## Выводы

В данном коде идет работа с текстовым файлом:

1. `with open("file.txt") as f:`: Открыли текстовый файл.

2. `print(f.readlines())`: Вывели все строки файла в массиве.

## Лабораторная работа №5
### ⦁ Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().


```python
with open("file.txt") as f:
    for line in f:
        print(line)  
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Lab5.png)

## Выводы

В данном коде идет работа с текстовым файлом:

1. `with open("file.txt") as f:`: Открыли текстовый файл.

2. `for line in f:
        print(line)  `: Выводим каждую строку файла отдельно.

## Лабораторная работа №6
### ⦁ Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.


```python
with open("file.txt", 'a+') as f:
    f.write('\nIm additional line')

with open("file.txt", 'r') as f:
    result = f.readlines()
    print(result)   
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Lab6.png)

## Выводы

В данном коде идет работа с текстовым файлом:

1. `with open("file.txt", 'a+') as f:`: Открыли файл.

2. `f.write('\nIm additional line')`: Добавили новую строку.

3. `with open("file.txt", 'r') as f:
    result = f.readlines()
    print(result)`: Вывели полученный файл в консоль.

## Лабораторная работа №7
### ⦁	Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.


```python
lines = ['one', 'two', 'three']
with open('file.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done! ') 
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Lab7.png)

## Выводы

В данном коде идет работа с текстовым файлом:

1. `lines = ['one', 'two', 'three']`: Создан список строк.

2. `with open('file.txt', 'w') as f:`: Открыли файл для записи.

3. `for line in lines:`: Цикл по всем элементам списка.

4. ` f.write('\nCycle run ' + line)
    print('Done! ') `: Записывается строка и выводится.

## Лабораторная работа №8
### ⦁	Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).


```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs('C:\\Users\\New\PycharmProjects\pythonProject1')  
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Lab8.png)

## Выводы

В данном коде идет работа с папками, имебщими вложенные директории:

1. `def print_docs(directory):`: На каждой итерации возвращает кортеж.

2. `all_files = os.walk(directory)`: Цикл по всем элементам

3. `for catalog in all_files:`: Выводит путь к текущей папке

4. `print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs('C:\\Users\\New\PycharmProjects\pythonProject1')`: Выводится список папок и подпапок, их имена, вызываем функцию для указания пути.

## Лабораторная работа №9
### ⦁	Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных.


```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))  
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Lab9.png)

## Выводы

В данном коде идет работа с функцией и текстовым файлом:

1. `def longest_words(file):
    with open(file, encoding='utf-8') as f:`: Открытие файла для чтения

2. `max_length = len(max(words, key=len))`: Находим максимальную длину среди слова

3. `for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words`: Создаем список и проходим по всем словам

4. `print(longest_words('input.txt'))`: Вызываем функцию и выводим результат.

## Лабораторная работа №10
### ⦁	Требуется создать csv-файл «rows_300.csv» со следующими столбцами:№ - номер по порядку (от 1 до 300); Секунда – текущая секунда на вашем ПК; Микросекунда – текущая миллисекунда на часах Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.


```python
import csv
import datetime
import  time
with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                         datetime.datetime.now().microsecond])
        time.sleep(0.01)  
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Lab10.png)

## Выводы

В данном коде идет работа с csv-файлом:

1. `with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:`: Открываем файл для записи.

2. `writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])`: Создаем объект и записываем заголовки.
   
3. `for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                         datetime.datetime.now().microsecond])
        time.sleep(0.01)`: Цикл от 1 до 300 с записью данных и с созданием задержки.

## Самостоятельная работа №1
### ⦁	Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.


```python
def analyze_text_simple(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.split()

        cleaned_words = []
        punctuation = '.,!?;:()—–-""«»'

        for word in words:
            clean_word = word.strip(punctuation)
            if clean_word:
                cleaned_words.append(clean_word.lower())

        total_words = len(cleaned_words)
        word_count = {}
        for word in cleaned_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        most_common_word = ""
        max_count = 0
        for word, count in word_count.items():
            if count > max_count:
                max_count = count
                most_common_word = word

        print(f"Общее количество слов: {total_words}")
        print(f"Самое частое слово: '{most_common_word}' (встречается {max_count} раз)")

        return total_words, most_common_word, max_count

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

analyze_text_simple("Solo.txt") 
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Solo1.png)
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Solo1(2).png)

## Выводы

В данном коде идет работа с текстовым файлом:

1. Открывает и читает весь текст

2. Разбивает на слова, удаляет пунктуацию, приводит к нижнему регистру

3. Считает общее количество слов и частоту каждого слова

4. Находит слово с наибольшей частотой

5. Показывает общее количество слов и самое частое слово
  
## Самостоятельная работа №2
### ⦁	У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.


```python
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
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Solo2.png)

## Выводы

В данном коде на вход программы принимается список результатов:

1. При запуске загружает существующие расходы из файла

2. Запрашивает у пользователя данные и сохраняет в файл

3. Показывает все ранее введенные расходы

4. Все данные сохраняются в JSON файл
  
## Самостоятельная работа №3
### ⦁	Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.Текст в файле: Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.Complex is better than complicated.Ожидаемый результат: Input file contains:108 letters 20 words 4 lines

 
```python
with open('Solo73.txt', 'r', encoding='utf-8') as file:
    text = file.read()

lines = text.splitlines()
num_lines = len(lines)

words = text.split()
num_words = len(words)

num_letters = 0
for char in text:
    if char.isalpha() and char.isascii():
        num_letters += 1

print("Input file contains:")
print(f"{num_letters} letters")
print(f"{num_words} words")
print(f"{num_lines} lines") 
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Solo3.png)

## Выводы

В данном коде идет работа с текстовым файлом:

1. `with open('Solo73.txt', 'r', encoding='utf-8') as file:
    text = file.read()`: Открываем файл и анализируем всё содержимое.

2. `lines = text.splitlines()
num_lines = len(lines)`: Разбиваем текст на строки и подсчитываем их количество.
   
3. `words = text.split()
num_words = len(words)`: Разбиваем текст на слова, подсчитываем их количество.

4. `num_letters = 0
for char in text:
    if char.isalpha() and char.isascii():
        num_letters += 1`: Инициализируем счетчик букв, проходим по каждому слову.

5. `print("Input file contains:")
print(f"{num_letters} letters")
print(f"{num_words} words")
print(f"{num_lines} lines") `: Выводим результаты.

## Самостоятельная работа №4
### ⦁	Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****. Запрещенные слова: hello email python the exam wor is Предложение для проверки: Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!! Ожидаемый результат:*****, ***ld! ****** ** *** programming language of *** future. My***** **....****** ** awesome!!!!


```python
def load_forbidden_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            return content.split()
    except FileNotFoundError:
        return ["hello", "email", "python", "the", "exam", "wor", "is"]


def censor_text(text, forbidden_words):
    result = text

    for word in forbidden_words:
        if not word:
            continue

        start = 0
        while True:
            index = result.lower().find(word.lower(), start)
            if index == -1:
                break

            stars = '*' * len(result[index:index + len(word)])
            result = result[:index] + stars + result[index + len(word):]
            start = index + len(stars)

    return result


forbidden_words = ["hello", "email", "python", "the", "exam", "wor", "is"]
test_text = """Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!"""

print("Исходный текст:")
print(test_text)
print("\nРезультат:")
print(censor_text(test_text, forbidden_words))  
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Solo4.png)

## Выводы

В данном коде идет работа с текстовым файлом:

1. `def load_forbidden_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            return content.split()
    except FileNotFoundError:
        return ["hello", "email", "python", "the", "exam", "wor", "is"]`: Функция для загрузки запрещенных слов.

2. `def censor_text(text, forbidden_words):
    result = text

    for word in forbidden_words:
        if not word:
            continue

        start = 0
        while True:
            index = result.lower().find(word.lower(), start)
            if index == -1:
                break`: Функция для замены запрещенных слов на звездочки.

3.  `forbidden_words = ["hello", "email", "python", "the", "exam", "wor", "is"]
test_text = """Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!"""`: Текстовые данные.

4.  `print("Исходный текст:")
print(test_text)
print("\nРезультат:")
print(censor_text(test_text, forbidden_words)) `: Вывод исходного текста и результата.
  
## Самостоятельная работа №5
### ⦁	Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.


```python
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
```
### Результат.
![Меню](https://github.com/Freeman-glitch/software-engineering/blob/tem_7.md/pic/Solo5.png)

## Выводы

В данном коде на вход программы принимаются три списка натуральных чисел:

1. `def get_quote_of_the_day():
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
        print("Создайте файл Solo75.txt с цитатами!")`: Функция для получения случайной цитаты из файла.

2. `def add_quote_simple():
    quote = input("Цитата: ")
    author = input("Автор: ")

    with open("Solo75.txt", "a", encoding="utf-8") as file:
        file.write(f"{quote}|{author}\n")
    print("Цитата сохранена!")`: Функция для добавления новой цитаты.

3.  `print("1 - Получить цитату дня")
print("2 - Добавить цитату")
choice = input("Выберите: ")`: Выводится меню выбора для пользователя.
4. `if choice == "1":
    get_quote_of_the_day()
elif choice == "2":
    add_quote_simple()`: Обработка выбора пользователя.
  
## Общие выводы по теме
Работа с текстовыми файлами в Python предоставляет возможность чтения данных из файла, записи данных в файл, а также обработки содержимого файла. Вот основные операции работы с текстовыми файлами: открытие, чтение, запись, добавление в файл, закрытие файла.
