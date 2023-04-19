class Pojistenec:
    def __init__(self, name, surname, age, cell):
        self.name = name
        self.surname = surname
        self.age = age
        self.cell = cell

    def __str__(self):
        return self.name+" "*(15-len(self.name))+self.surname+" "*(15-len(self.surname))+str(self.age)+" let"+"          "+self.cell





