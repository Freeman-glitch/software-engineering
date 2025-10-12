import math

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

min_triangle = [min(one), min(two), min(three)]
area_min = triangle_area(*min_triangle)

max_triangle = [max(one), max(two), max(three)]
area_max = triangle_area(*max_triangle)

print(f" Площадь треугольника из минимальных элементов: {area_min:.2f}")
print(f" Площадь треугольника из максимальных элементов: {area_max:.2f}")