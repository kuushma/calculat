import math


class Parallelogram():
    def side_hide(self, a, h):
        if Parallelogram.examination(a, h):
            ans = a * h
            return round(ans, 7)
        else:
            return 'Ошибка'

    def side_injection(self, a, b, injection):
        if Parallelogram.examination(a, b, injection):
            ans = a * b * math.sin(math.radians(injection))
            return round(ans, 7)
        else:
            return 'Ошибка'

    def diagonal_ugol(self, d1, d2, ugol):
        if Parallelogram.examination(d1, d2, ugol):
            ans = 0.5 * d1 * d2 * math.sin(math.radians(ugol))
            return round(ans, 7)
        else:
            return 'Ошибка'

    def examination(self, *args):
        for i in args:
            if i == 0:
                return 'Ошибка'
        return True