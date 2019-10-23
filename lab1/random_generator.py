import random
import math

rang = lambda point_range: random.uniform(-point_range, point_range)


def det_2(a, b, c):
    return (a[0] - c[0]) * (b[1] - c[1]) - (a[1] - c[1]) * (b[0] - c[0])


def det_1(a, b, c):
    return a[0] * b[1] * 1 + a[1] * 1 * c[0] + 1 * b[0] * c[1] - 1 * b[1] * c[0] - 1 * c[1] * a[0] - 1 * a[1] * b[0]


def rand_list(n, point_range):
    return [[rang(point_range), rang(point_range)] for i in range(n)]


def point_on_cycle(R, t):
    return [R * math.cos((math.pi / 2) * t), R * math.sin((math.pi / 2) * t)]


def rand_cycle_list(n, R):
    return [point_on_cycle(R, random.uniform(0, 4)) for i in range(n)]


def rand_linear(n, point_range, v, start_point):
    x = lambda t: start_point[0] + t * v[0]
    y = lambda t: start_point[1] + t * v[1]
    real_range = (point_range - start_point[0]) / v[0]
    return [[x(rang(real_range)), y(rang(real_range))] for i in range(n)]


n_1 = 10 ** 5
n_2 = 1000
range_1 = 1000
range_2 = 10 ** 14
R = 100
v = [2.0, 0.1]
start_point = [-1.0, 0.0]
print(rand_list(5, range_2))
print(rand_cycle_list(5, 100))
print(rand_linear(5, range_1, v, start_point))
