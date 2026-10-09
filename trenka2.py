class Appliance:
	def __init__(self,brand,power):
		self._brand=brand
		self._power=power
	def get_brand(self):
		return self._brand
	def set_brand(self,new_brand):
		self._brand=new_brand

	def get_power(self):
		return self._power
	def set_power(self,new_power):
		self._power=new_power


class WashingMachine(Appliance):
	def __init__(self,brand,power):
		super().__init__(brand,power)
	def wash(self):
		print("Juady")
	def operate(self):
		print("Jugysh")
class Refrigerator(Appliance):
	def __init__(self,brand,power):
		super().__init__(brand,power)
	def cool(self):
		print("suytady")
	def operate(self):
		print("tonazytqysh")

class Microwave(Appliance):
	def __init__(self,brand,power):
		super().__init__(brand,power)
	def heat(self):
		print("ysytady")
	def operate(self):
		print("ysytqysh")

kirmash=WashingMachine("LG",220)
holod=Refrigerator("Samsung",140)
micro=Microwave("LG",100)

technics=[kirmash,holod,micro]

for technika in technics:
	technika.operate()
