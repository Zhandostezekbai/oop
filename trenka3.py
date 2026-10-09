class Vegetables:
	def __init__(self , name , taste ):
		self.name = name
		self.taste = taste
	
	def get_taste(self):
		return self.taste

	def set_taste(self, new_taste):
		self.taste = new_taste


class Cucumber(Vegetables):
	def __init__(self, name, taste):
		super().__init__(name, taste)

	def what_taste(self):
		print("ote balgyyn")

	def eat(self):
		print("Qyttyrlaidy")

class Carrot(Vegetables):
	def __init__(self, name, taste):
		super().__init__(name, taste)

	def what_taste(self):
		print("ote tatti")
	
	def eat(self):
		print("qytyrlaidy")


class Salad(Vegetables):
	def __init__(self, name, taste):
		super().__init__(name, taste)

	def what_taste(self):
		print("balgyyn")

	def eat(self):
		print("qytyrlaidy")

cucumber=Cucumber("qiar","ote balgyn")
carrot=Carrot("morkov","ote tatti")
salad=Salad("salad","balgyn")

vegetables=[cucumber,carrot,salad]

for vegetable in vegetables:
	vegetable.what_taste()

cucumber.set_taste("srok otken")
print(cucumber.get_taste())
