class Fruit():
	def __init__(self,name,taste):
		self._name=name 
		self._taste=taste
	
	def get_name(self):
		return self._name
	def set_name(self,new_name):
		self._name=new_name

	def get_taste(self):
		return self._taste
	def set_taste(self,new_taste):
		self._taste=new_taste

	def describe():
		print('Bul Zhemis')

class Apple(Fruit):
	def __init__(self,name,taste):
		super().__init__(name,taste)
	
	def crunch(self):
		print('alma qytyrlaidy')
	def describe(self):
		print('Bul zhemis tatti')

class Orange(Fruit):
	def __init__(self,name,taste):
		super().__init__(name,taste)

	def peel(self):
		print('apelsin tazartylady')
	def describe(self):
		print('Bul Zhemis Qyshqyl')

class Banana(Fruit):
	def __init__(self,name,taste):
		super().__init__(name,taste)

	def peel(self):
		print('banan tazartylady')
	def describe(self):
		print('Bul Zhemis uzyn,tatti')

apple=Apple("aport","damdi")
print(apple._name)
orange=Orange('sary',"qyshqyl")

banana=Banana('Afro',"ote tatti")

fruits=[apple,orange,banana]
for fruit in fruits:
	fruit.describe()