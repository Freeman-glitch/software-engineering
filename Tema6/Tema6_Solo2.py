def remove_first_occurrence(tuple_data, element_to_remove):
    temp_list = list(tuple_data)
    if element_to_remove in temp_list:

        temp_list.remove(element_to_remove)

    return tuple(temp_list)

test_cases = [
    ((1, 2, 3), 1),
    ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
    ((2, 4, 6, 6, 4, 2), 9)
]

print("Результаты:")
for i, (tuple_data, element) in enumerate(test_cases, 1):
    result = remove_first_occurrence(tuple_data, element)
    print(f"Тест {i}: {result}")