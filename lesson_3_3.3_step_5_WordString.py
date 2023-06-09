class WordString:
    def __init__(self, string=""):
        self.__string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        if type(value) == str:
            self.__string = value

    def __len__(self):
        while self.__string.count("  ") > 0:
            self.__string = self.__string.replace("  ", " ")
        return len(self.__string.split())

    def __call__(self, indx):
        return self.__string.split()[indx]


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
