from math import pi


class CircleAngles:
    def __init__(self):
        self.n = 0
        self.to = 2 * pi

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.to:
            raise StopIteration

        result = self.n
        self.n += 2 * pi / 600
        return result
