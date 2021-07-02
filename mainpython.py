class Subject:
    def __init__(self, name: str, unit: float, grade: float):
        # name must be not be an empty string 
        # unit must be greater than zero 
        # grade should be between 0 - 100 only
        # raise an Exception if data is invalid
        self.name = name
        if self.name == "":
            raise Exception()
        self.unit = float(unit)
        if self.unit<0:
            raise Exception()
        self.grade = float(grade)
        if self.grade<0 and self.grade>100:
            raise Exception()

class Student:
    def __init__(self, name: str):
        # name must not be an empty string 
        # raise an Exception if data is invalid
        self.name = name
        self.subject = []
        self.subject2 = []
        if self.name == "":
            raise Exception()

    def add_subject(self, subject: Subject):
        A = {"unit":subject.unit, "grade":subject.grade} 
        self.subject2.append(A)
        self.subject.append(subject)


    def solve_gwa(self) -> float:
        F = 0
        for sol in self.subject2:
            F += sol["grade"]*sol["unit"]/sol["unit"]
            return  F