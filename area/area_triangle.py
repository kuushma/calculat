from math import sqrt, sin, radians


class Triangle():
     def Geron(self, a, b, c):
          if Triangle().examination(a, b, c):
               if a + b > c and a + c > b and c + b > a:
                    p = 0.5 * (a + b + c)
                    ans = sqrt(p*(p - a)*(p - b)*(p - c))
                    return round(ans, 5)
               else:
                    return 'Ошибка'
          else:
               return 'Ошибка'

     def Hight_a(self, hight, a):
          if Triangle().examination(hight, a):
               ans = 0.5 * hight * a
               return round(ans, 7)
          else:
               return 'Ошибка'

     def isosceles_triangle(self, a, b):
          if Triangle().examination(a, b):
               if a + a > b and a + b > a:
                    ans = (b * sqrt(a ** 2 - (b ** 2 / 4)) / 2)
                    return round(ans, 7)
               else:
                    return 'Ошибка'
          else:
               return 'Ошибка'

     def equilateral_triangle(self, a):
          if Triangle().examination(a):
               ans = (sqrt(3) / 4 * a ** 2)
               return round(ans, 5)
          else:
               return 'Ошибка'

     def right_triangle(self, a, c):
          if Triangle().examination(a, c):
               if a + c > sqrt(a ** 2 + c ** 2) or a + sqrt(a ** 2 + c ** 2) > c or \
                       c + sqrt(a ** 2 + c ** 2) > a:
                    ans = 0.5 * a * c
                    return round(ans, 5)
               else:
                    return 'Ошибка'
          else:
               return 'Ошибка'

     def angle_between_them(self, a, b, injection):
          if Triangle().examination(a, b, injection):
               i = radians(injection)
               ans = 0.5 * a * b * sin(i)
               return round(ans, 5)
          else:
               return 'Ошибка'

     def examination(self, *args):
          for i in args:
               if i == 0:
                    return 'Ошибка'
          return True

