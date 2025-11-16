def check_file_content(filename):
    try:

        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        if len(content.strip()) == 0:
            raise Exception("файл пустой")
        else:
            print(f"Содержимое файла '{filename}':")
            print(content)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден")
    except Exception as e:
        print(f"Ошибка: {e}")


with open('test_empty.txt', 'w', encoding='utf-8') as f:
    pass

with open('test_with_data.txt', 'w', encoding='utf-8') as f:
    f.write("Змеи используют свой раздвоенный язык для «обоняния»: он собирает частицы из воздуха, которые затем анализируются в ротовой полости, а не ноздрями.\n")
    f.write("Они также обладают уникальным строением черепа, позволяющим заглатывать добычу значительно крупнее их самих, и могут не иметь зрения, которое у них есть\n")
    f.write("Конец данных.")

print(" Проверка пустого файла ")
check_file_content('test_empty.txt')

print("\n Проверка файла с данными ")
check_file_content('test_with_data.txt')
