def get_office_interval(tuple_data, employee_id):

    if employee_id not in tuple_data:
        return ()
    first_index = tuple_data.index(employee_id)

    try:
        second_index = tuple_data.index(employee_id, first_index + 1)
        return tuple_data[first_index:second_index + 1]
    except ValueError:
        return tuple_data[first_index:]

test_cases = [
    ((1, 2, 3), 8),
    ((1, 8, 3, 4, 8, 8, 9, 2), 8),
    ((1, 2, 8, 5, 1, 2, 9), 8)
]

print("Результаты:")
for i, (tuple_data, emp_id) in enumerate(test_cases, 1):
    result = get_office_interval(tuple_data, emp_id)
    print(f"Тест {i}: {result}")