

import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np
import random


random.seed(42)


def f(x):
    return x ** 2


a = 0
b = 2

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, "r", linewidth=2, label="f(x)")

limit_x = np.linspace(a, b)
limit_y = f(limit_x)
ax.fill_between(limit_x, limit_y, color="gray", alpha=0.3)


def monte_carlo_function(a, b, num_points):
    count_under_curve = 0

    for _ in range(num_points):
        x = random.uniform(a, b)
        y = random.uniform(0, f(b))

        if y <= f(x):
            count_under_curve += 1

    ratio = count_under_curve / num_points

    integral_value = ratio * (b - a) * max(f(x)
                                           for x in np.linspace(a, b, num_points))

    return integral_value


ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
ax.legend()
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

plt.grid()
plt.show()


points = 100000

monte_carlo_value = monte_carlo_function(a, b, points)
quad_value, error = spi.quad(f, a, b)

print("Значення методом Монте-Карло:", monte_carlo_value)
print("Значення за допомогою quad:", quad_value)


tolerance = 1e-5
if np.isclose(monte_carlo_value, quad_value, rtol=tolerance):
    print("Результати збігаються. Метод Монте-Карло є ефективним.")
else:
    print(
        f"Результати не збігаються при {points} випадкових точках")
