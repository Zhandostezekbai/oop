class Student:
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	def get_name(self):
		return self.name
	def set_name(self,new_name):
		self.name=new_name

class ExStudent(Student):
	def __init__(self,name,grade):
		super().__init__(name,grade)
	def move(self):
		print("Sabaqqa barady")

class FuStudent(Student):
	def __init__(self,name,grade):
		super().__init__(name,grade)
	def move(self):
		print("Sabaqqa keide barady")

class NewStudent(Student):
	def __init__(self,name,grade):
		super().__init__(name,grade)
	def move(self):
		print("Sabaqqa barmaidy")

Exstudent=ExStudent("Eraly","2")
Fustudent=FuStudent("Nurlan","1")
Newstudent=NewStudent("Mans","3")

stud=[Exstudent,Fustudent,Newstudent]
for student in stud:
	student.move()