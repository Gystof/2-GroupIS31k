import math


class Algorithms():

    def linear_algoritm(self, x, y, z) -> float:
        if -1 <= z <= 1:
            return math.sqrt(10 * (x ** (1 / 3) + x ** (y + 2))) * ((math.asin(z) ** 2) - abs(x - y))
        else:
            return '-1 <= z <= 1 Исправь :)'

    def f(self, func: str, x: float) -> float:
        if func == "cos(x)":
            return math.cos(x)
        elif func == "exp(x)":
            return math.exp(x)
        elif func == "sqr(x)":
            return x ** 2

    def branching_algorithm(self, x: float, y: float, func: str) -> float:
        if 4 > (x * y) > 1 :
            return (self.f(func, x) + y) ** 2
        elif 8 < (x * y) < 10:
            return self.f(func, x) * math.tan(y)
        else:
            return self.f(func, x) + y


if __name__ == "__main__":
    res = Algorithms()
    print(res.linear_algoritm(1, 2, 1))
