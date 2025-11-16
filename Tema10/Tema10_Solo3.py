def add_two():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = 2 + number
        print(f"Результат: 2 + {number} = {result}")
        return result

    except ValueError:
        print("Ошибка: Неподходящий тип данных. Ожидалось число.")
        return None
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")
        return None


def main():
    while True:
        result = add_two()

        while True:
            continue_choice = input("\nХотите выполнить еще один расчет? (да/нет): ").lower().strip()
            if continue_choice in ['да', 'д', 'yes', 'y']:
                break
            elif continue_choice in ['нет', 'н', 'no', 'n']:
                return
            else:
                print("Пожалуйста, введите 'да' или 'нет'")


if __name__ == "__main__":
    main()