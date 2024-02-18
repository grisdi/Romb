class Rhombus:
    def __init__(self, a, h):
        self.side_a = a
        self.height_h = h

    def perimeter(self):
        return 4 * self.side_a

    def area(self):
        return self.side_a * self.height_h

    def diagonal(self):
        return (self.side_a ** 2 + self.height_h ** 2) ** 0.5


'''        
self.__perimeter = 0
        self.__area = 0
        self.__diagonal = 0
        self.calculate_data()

    @property
    def perimeter(self):
        return self.__perimeter

    @property
    def area(self):
        return self.__area

    @property
    def diagonal(self):
        return self.__diagonal

    def calculate_data(self):
        self.__area = self.__side_a * self.__height_h
        self.__perimeter = 4 * self.__side_a
        self.__diagonal = (self.__side_a ** 2 + self.__height_h ** 2) ** 0.5
'''