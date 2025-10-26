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