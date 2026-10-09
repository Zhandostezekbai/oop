class Computer:
	def __init__(self, model, year):
		self._model = model
		self._year = year

	def get_model(self):
		return self._model
	
	def set_model(self, new_model):
		self._model = new_model
	
	def get_year(self):
		return self._year
	
	def set_year(self, new_year):
		self._year= new_year

class Desktop(Computer):
	def __init__(self, model, year):
		super().__init__(model,year)
	
	def start(self):
		print("Үстел компьютері іске қосылады")

	def work(self):
		print("Wordta jumys jasap jatyr")

	

class GamingPC(Computer):
	def __init__(self, model, year):
		super().__init__(model,year)
	
	def play_game(self):
		print("Ойын компьютері ойынды іске қосады")

	def work(self):
		print("Oiyn oinap otyr")


class Server(Computer):
	def __init__(self, model, year):
		super().__init__(model , year)
	
	def process_data(self):
		print("Сервер деректерді өңдейді")

	def work(self):
		print("Server qabyldap jatyr")

desktop=Desktop(" hp ", " 2016 ")
gamingpc=GamingPC(" Acer ", " 2024 ")
server=Server(" Eraly ", " 2020 ")

devices=[desktop, gamingpc, server]

for device in devices:
	device.work()

