class Square():
    def side(self, a):
        if a != 0:
            ans = a ** 2
            return round(ans, 7)
        else:
            return 'Ошибка'

    def diagonal(self, a):
        if a != 0:
            ans = a ** 2 / 2
            return round(ans, 7)
        else:
            return 'Ошибка'

    def examination(self, *args):
        for i in args:
            if i == 0:
                return 'Ошибка'
        return True

