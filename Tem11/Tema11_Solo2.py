def fib(n):
    a, b = 1, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = 200
fibonacci_200 = None

with open("fib.txt", "w", encoding="utf-8") as file:
    for i, num in enumerate(fib(n), 1):
        file.write(f"{num}\n")

        if i == n:
            fibonacci_200 = num
            break

print(f"200-е число Фибоначчи: {fibonacci_200}")
print("Все числа Фибоначчи записаны в файл 'fib.txt'")