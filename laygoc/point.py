class MyNum:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNum(self.value + other.value)

    def __str__(self):
        return str(self.value)
a=MyNum(1)

b=MyNum(2)
print(a+b)