import math


class Rhombus():
    def examination(self, *args):
        for i in args:
            if i == 0:
                return 'Ошибка'
        return True

    def side_ugol(self, a, ugol):
        if Rhombus.examination(a, ugol):
            ans = a ** 2 * math.sin(math.radians(ugol))
            return ans
        else:
            return 'Ошибка'

    def side_hide(self, a, h):
        if Rhombus.examination(a, h):
            ans = a * h
            return ans
        else:
            return 'Ошибка'

    def diagonal(self, d1, d2):
        if Rhombus.examination(d1, d2):
            ans = (d1 * d2) / 2
            return ans
        else:
            return 'Ошибка'

    def diagonal_ugol(self, d, ugol):
        if Rhombus.examination(d, ugol):
            ans = (d ** 2 / 2) * math.tan(math.radians(ugol / 2))
            return ans
        else:
            return 'Ошибка'

    def diagonal_ugol_ne(self, d, ugol):
        if Rhombus.examination(d, ugol):
            ans = (d ** 2 / 2) * (1 / math.tan(math.radians(ugol / 2)))
            return ans
        else:
            return 'Ошибка'

    def ugol_radius(self, ugol, r):
        if Rhombus.examination(r, ugol):
            ans = (4 * r ** 2) / (math.sin(math.radians(ugol)))
            return ans
        else:
            return 'Ошибка'

    def side_radius(self, a, r):
        if Rhombus.examination(a, r):
            ans = 2 * a * r
            return ans
        else:
            return 'Ошибка'