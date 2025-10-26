def load_forbidden_words(filename):
    """Загружает список запрещенных слов из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            return content.split()
    except FileNotFoundError:
        return ["hello", "email", "python", "the", "exam", "wor", "is"]


def censor_text(text, forbidden_words):
    """Заменяет запрещенные слова в тексте на звездочки"""
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


# Тестовые данные
forbidden_words = ["hello", "email", "python", "the", "exam", "wor", "is"]
test_text = """Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!"""

print("Исходный текст:")
print(test_text)
print("\nРезультат:")
print(censor_text(test_text, forbidden_words))