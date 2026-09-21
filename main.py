class Student:
    def __init__(self,name:str,grade:int,student_id:str):
        self.name=name
        self._grade=grade
        self.__student_id=student_id

    def get_name(self):
        return self.get_name

    def set_name(self,new_name):
        self.name=new_name

    def add_grade(self,points):
        self._grade=self._grade + points                

Eraly=Student("Eraly",8,"432ff1")

print(Eraly.set_name("Eraly"))
print("New name is:",Eraly.get_name())

print("Bastapqy bagasy:",Eraly._grade)
Eraly.add_grade(5)
print("Songy bagasy:",Eraly._grade)

class ExcellentStudent(Student):
    def __init__(self, name, grade, student_id):
        super().__init__(name, grade, student_id)
    def add_grade(self, points,points1):
        self._grade=self._grade +points+points1
        return self._grade

student=ExcellentStudent("Nurlan",12,"23gg2")

print("Bastapqy bagasy:",student._grade)
student.add_grade(5,6)
print("Songy bagasy:",student._grade)