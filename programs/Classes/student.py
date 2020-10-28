class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_ = 'student'

    def average(self, score1, score2, score3):
        return((score1+score2+score3)/3)


Iwan = Student("Iwan", "21")

print(Iwan.average(12, 24, 43))
