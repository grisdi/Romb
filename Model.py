class Model:
    def __init__(self):
        self.side_a = 0
        self.height_h = 0
        self.perimeter = 0
        self.area = 0
        self.diagonal = 0


    def calculate_romb(self, side_a, height_h):
        self.side_a = side_a
        self.height_h = height_h

        self.perimeter = 4 * side_a
        self.area = side_a * height_h
        self.diagonal = (side_a ** 2 + height_h ** 2) ** 0.5

        return self.perimeter, self.area, self.diagonal

    def start_new_calculation(self):
        self.side_a = 0
        self.height_h = 0
        self.perimeter = 0
        self.area = 0
        self.diagonal = 0
