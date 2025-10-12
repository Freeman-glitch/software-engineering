results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
           27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

sorted_results = sorted(results)
print("Три лучших результата:")
best_results = sorted_results[:3]
for i, result in enumerate(best_results, 1):
    print(f"   {i} место: {result} сек")

print()
print("Три худших результата:")
worst_results = sorted_results[-3:]
for i, result in enumerate(reversed(worst_results), 1):
    print(f"   {i} место с конца: {result} сек")
print()
print("3. Все результаты начиная с 10:")
results_from_10 = [result for result in sorted_results if result >= 10]
print(f"   Количество результатов от 10 сек и выше: {len(results_from_10)}")
print(f"   Список: {results_from_10}")