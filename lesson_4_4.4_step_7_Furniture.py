class Furniture:
    def __init__(self, name, weight):
        self.__verify_name(name)
        self.__verify_weight(weight)

        self._name = name
        self._weight = weight

    def __verify_name(self, name):
        if type(name) != str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight):
        if weight <= 0:
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, key, value):
        if key == "_name":
            self.__verify_name(key)
        if key == "_weight":
            self.__verify_weight(key)
        super().__setattr__(key, value)

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square
