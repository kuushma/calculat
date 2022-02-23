import math


class Trapezoid():
    def sides_hide(self, a, b, h):
        if Trapezoid.examination(a, b, h):
            ans = ((a + b) / 2) * h
            return ans
        else:
            return 'Ошибка'

    def hide_linesr(self, h, line):
        if Trapezoid.examination(h, line):
            ans = line * h
            return ans
        else:
            return 'Ошибка'

    def sides(self, a, b, c, d):
        if Trapezoid.examination(a, b, c, d):
            ans = ((a + b) / 2) * math.sqrt(c ** 2 - (((b - a) ** 2 + c ** 2 - d ** 2) / (2 * (b - a))) ** 2)
            return ans
        else:
            return 'Ошибка'

    def ravnobedrenny_side(self, a, b, c):
        if Trapezoid.examination(a, b, c):
            ans = ((a + b) / 2) * math.sqrt(c ** 2 - (((b - a) ** 2) / 4))
            return ans
        else:
            return 'Ошибка'
    def ravnobedrenny_osns_ugol(self, a, b, ugol):
        if Trapezoid.examination(a, b, ugol):
            ans = ((b ** 2 - a ** 2) * math.tan(math.radians(ugol))) / 4
            return ans
        else:
            return 'Ошибка'

    def examination(self, *args):
        for i in args:
            if i == 0:
                return 'Ошибка'
        return True