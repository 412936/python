#6вариант
class Figure:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def calculate_volume(self):
        return self.a * self.b * self.c

    def __add__(self, other):
        if isinstance(other, HollowBody):
            return HollowBody(self.a + other.a, self.b + other.b, self.c + other.c, other.d)
        if isinstance(other, MultiFigure) and (self.a, self.b, self.c) == (other.a, other.b, other.c):
            return MultiFigure(self.a, self.b, self.c, other.count)
        if isinstance(other, Figure):
            return Figure(self.a + other.a, self.b + other.b, self.c + other.c)
        return self.calculate_volume() + other.calculate_volume()

class HollowBody(Figure):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def calculate_volume(self):
        return super().calculate_volume() - (self.a - self.d) * (self.b - self.d) * (self.c - self.d)
class MultiFigure(Figure):
    def __init__(self, figure):
        self.figure = figure

    def calculate_volume(self):
        volume = 0
        for figures in self.figure:
            volume += figures.calculate_volume()
        return volume
def main():
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))

    figures = Figure(a, b, c)
    volume = figures.calculate_volume()
    print("Объем : {}".format(volume))

    hb = HollowBody(a, b, c, 1)
    volume = hb.calculate_volume()
    print("Объем тела за вычетом пустоты: {}".format(volume))

    mf = MultiFigure([figures, hb])
    volume = mf.calculate_volume()
    print("Суммарный объем нескольких фигур: {}".format(volume))

if __name__ == '__main__':
    main()