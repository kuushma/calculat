import math


class Circle():
    def examination(self, *args):
        for i in args:
            if i == 0:
                return 'Ошибка'
        return True

    def radius(self, r):
        if Circle.examination(r):
            ans = r ** 2 * math.pi
            return ans
        else:
            return 'Ошибка'

    def diametr(self, d):
        if Circle.examination(d):
            ans = d ** 2 * math.pi / 4
            return ans
        else:
            return 'Ошибка'

    def len(self, le):
        if Circle.examination(le):
            ans = le ** 2 / (4 * math.pi)
            return ans
        else:
            return 'Ошибка'