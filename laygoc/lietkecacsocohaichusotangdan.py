import sys
class Rectangle:
    def __init__(self, a, b, c) :
        self.perimeter = (a+b)*2
        self.area = a*b
        self.color = c[:1].upper() + c[1:].lower()

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter, r.area, r.color))
else: print('INVALID')
sys.exit()

