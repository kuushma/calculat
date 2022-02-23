import math


class rectangle():
    def side(self, a, b):
        if rectangle.examination(a, b):
            ans = a * b
            return ans
        else:
            return 'Ошибка'

    def diagonal(self, d, injection):
        if rectangle.examination(d, injection):
            ans = 0.5 * d ** 2 * math.sin(math.radians(injection))
            return ans
        return 'Ошибка'

    def side_diagonal(self, a, d):
        if rectangle.examination(a, d):
            if (d ** 2 - a ** 2) >= 0:
                ans = a * math.sqrt(d ** 2 - a ** 2)
                return ans

        return 'Ошибка'

    def radius_and_side(self, a, R):
        if rectangle.examination(a, R):
            ans = a * math.sqrt(4 * R ** 2 - a ** 2)
            return ans
        else:
            return 'Ошибка'

    def diametr_and_side(self, a, D):
        if rectangle.examination(a, D):
            ans = a * math.sqrt(D ** 2 - a ** 2)
            return ans
        else:
            return 'Ошибка'

    def examination(self, *args):
        for i in args:
            if i == 0:
                return 'Ошибка'
        return True