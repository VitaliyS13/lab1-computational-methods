# Модель: Метод Ньютона (5 семестр)
# Автор: Самсонов Віталій, група АІ-233

import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Функція
def f(x):
    return 2 * x**4 + 8 * x**3 + 8 * x**2 - 1

# Похідна
def df(x):
    return 8 * x**3 + 24 * x**2 + 16 * x

# Побудова графіка
x = np.linspace(-5, 5, 1000)
y = f(x)

plt.plot(x, y)
plt.axhline(0, linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції')
plt.grid(True)
plt.ylim(-10, 30)
plt.show()

# Метод Ньютона
def newton_method(a, b, epsilon):
    x0 = (a + b) / 2
    iteration = 0

    while True:
        iteration += 1
        fx0 = f(x0)
        dfx0 = df(x0)

        # Захист від ділення на 0
        if dfx0 == 0:
            print("Похідна дорівнює нулю. Метод зупинено.")
            return None, iteration

        x1 = x0 - fx0 / dfx0

        print(f"Ітерація {iteration}: x = {x1:.12f}, f(x) = {f(x1):.12f}, |x1-x0| = {abs(x1-x0):.12f}")

        if abs(x1 - x0) < epsilon or abs(f(x1)) < epsilon:
            return x1, iteration

        x0 = x1


epsilon = 1e-8

# Інтервали
intervals = [(-1.0, 0.0), (0.0, 0.5), (-3.0, -2.0), (-2.0, -1.5)]

roots = []
iterations_list = []

for a, b in intervals:
    root, iterations = newton_method(a, b, epsilon)
    roots.append(root)
    iterations_list.append(iterations)

# Вивід результатів
for i, root in enumerate(roots):
    print(f"Корінь {i+1}: {root:.12f}, f(x) = {f(root):.12f}")

# Таблиця
data = [
    ['Метод Ньютона'] + roots + iterations_list
]

headers = ['Метод', 'Корінь 1', 'Корінь 2', 'Корінь 3', 'Корінь 4',
           'Ітерації 1', 'Ітерації 2', 'Ітерації 3', 'Ітерації 4']

table = tabulate(data, headers, tablefmt="grid")
print(table)

# Запис у файл
with open("results.txt", "w") as f:
    f.write(table)

print("Результати записані в файл results.txt")