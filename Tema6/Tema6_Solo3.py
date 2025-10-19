def count_top_three_digits(digit_string):

    digit_count = {}
    for char in digit_string:
        digit = int(char)
        digit_count[digit] = digit_count.get(digit, 0) + 1
    sorted_digits = sorted(digit_count.items(), key=lambda x: (-x[1], x[0]))

    top_three = dict(sorted_digits[:3])
    return top_three

def print_sorted_result(result_dict):
    print("Топ-3 самых частых цифр:")
    for digit in sorted(result_dict.keys()):
        print(f"Цифра {digit}: {result_dict[digit]} раз(а)")

test_strings = ["98761111234567987654",]

for i, test_str in enumerate(test_strings, 1):
    result = count_top_three_digits(test_str)
    print_sorted_result(result)