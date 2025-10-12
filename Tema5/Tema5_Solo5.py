def transform_numbers(numbers):
    result_set = set()

    from collections import Counter
    count = Counter(numbers)
    for num, freq in count.items():
        result_set.add(num)
        for i in range(2, freq + 1):
            result_set.add(str(num) * i)
    return result_set

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

result_1 = transform_numbers(list_1)
result_2 = transform_numbers(list_2)
result_3 = transform_numbers(list_3)

print(result_1)
print(result_2)
print(result_3)