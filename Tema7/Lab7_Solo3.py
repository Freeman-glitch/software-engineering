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