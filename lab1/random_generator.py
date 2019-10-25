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


def rand_linear(n, point_range, pa, pb):
    result = []
    for i in range(n):
        x = rang(point_range)
        y = (pa[1]-pb[1])/(pa[0]-pb[0])*x+(pa[1]-(pa[1]-pb[1])/(pa[0]-pb[0])*pa[0])
        result.append([x, y])
    return result


print(rand_linear(5, 1000, [0.0, 0.0], [1.0, 1.0]))
