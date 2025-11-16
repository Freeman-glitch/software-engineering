import time
from functools import wraps


class RetryOnError:
    def __init__(self, max_attempts=3, delay=1):
        self.max_attempts = max_attempts
        self.delay = delay

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(self.max_attempts):
                try:
                    print(f"Попытка {attempt + 1}/{self.max_attempts}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Ошибка: {e}")
                    if attempt < self.max_attempts - 1:
                        print(f"Ждем {self.delay} сек...")
                        time.sleep(self.delay)
            print("Все попытки провалились!")
            raise

        return wrapper


# Декораторы с разными настройками
retry_3_times = RetryOnError(max_attempts=3, delay=1)
retry_fast = RetryOnError(max_attempts=2, delay=0.5)


# Функция 1: Имитация ненадежного соединения
@retry_3_times
def fake_api_call():
    import random
    if random.random() < 0.7:  # 70% вероятность ошибки
        raise ConnectionError("Сервер не отвечает")
    return "Данные получены!"


# Функция 2: Деление с проверкой
@retry_fast
def safe_divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b


# Демонстрация
print(" ДЕМО ДЕКОРАТОРА ПОВТОРА \n")

print("1. Тест API вызова:")
try:
    result = fake_api_call()
    print(f"Успех: {result}")
except:
    print("API вызов провален")

print("\n2. Тест деления:")
try:
    result = safe_divide(10, 0)
    print(f"Результат: {result}")
except:
    print("Деление не удалось")