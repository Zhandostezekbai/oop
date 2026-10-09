class Book():
	def __init__(self, title, author):
	self._title = title
        self._author = author

	def set_title(self, title):
		self._title = title
        def get_title(self):
		return self._title


	def set_author(self, author):
        	self._author=author
	def get_author(self):
 		return self._author

class Novel(Book):
   super().init(self,read,describe):
	self._read = read
	self._describe = describe

	def read(self):
	print("Роман окылады")

        def describe(self):
	print("")
	self.read()
	
class Textbook(Book):
	super().init(self,read,describe):
		self._read = read
		self._describe = describe

 	def study(self):
	print("Оқулықпен сабақ оқылады")

 	def describe(self):
	print("Окулыкпен сабак окытылады")
 	self.study()

class Comicbook(Book):
	super().init(self, ilistrate , describe):
		self._ilistrate = ilistrate
		self._describe = describe

 	def ilistrate(self):
	print("Комикс суреттермен баяндалады")

 	def describe(self):
	print("Комикстын кытаптары суреттермен баяндалады")
 	self.ilistrate()

Novl=Novel("djadjjda","Bekzhan")
TxtBook=Textbook("Physics","Almaty kitap")
Comics=Comicbook("Avengers","Marvel")


for book in decribe():
	book.describe()
  

	
