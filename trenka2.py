class HeatingSystem:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"Жылыту жүйесі ({self.name}) іске қосылды")


class House:
    def __init__(self, room, heating_name):
        self.room = room
        self.__heating = HeatingSystem(heating_name)

    def live(self):
        print("Үйде тұру процесі басталды...")
        self.__heating.start()
        print("Жылыту жүйесі бағдарламасы іске қосылды")


print("--- 1 тапсырма нәтижесі ---")
my_house = House("pater", "EcoHeat 524")
my_house.live()

class Vehicle:
    def __init__(self, speed, weight)
	self.__speed = speed
	self._weight =  weight
    

    def get_speed(self):
	return self.__speed

    def display_info(self):
	print("Массасы:{self._weight},Жылдамдығы:{self.get_speed()}")

    
    def calculate_fuel(self):
	return self._weight * 0.5

    def move(self):
 	print("Көлік жылжыды")

class Car(Vehicle):
    def __init__(self,speed,weight)
	super().__init__(speed,weight)

    def calculate_fuel(self):
	base_fuel = self._weight * 3
    def move(self):
	print("Автокөлік жылжи бастады! Топливо:{self.calculate_fuel()}")

class  Boat(Vehicle):
    def __init__(self,speed,weight)
	super().__init__(speed,weight)


    def calculate_fuel(self):
	base_fuel = self._weight * 5


    def move(self):
	print("Кеме жылжи бкастады! Топливо:{self.calculate_fuel()}")

class Amphibian(Car,Boat):
    def __init__(self,speed,weight):
	super().__init__(self,speed,weight):

    def calculate_fuel(self):
	return(super().calculate_fuel())

print("--- 2 тапсырма нәтижесі ---")
vehicle_obj = Vehicle(speed=200,weight=30)
vehicle_obj.display_info()
vehicle_obj.move()
print()

car_obj = Car(speed=300,weight = 40)
car_obj.display_info()
car_obj.move()
print()

amphibian_obj = Amphibian(speed = 150, weight = 200)
amphibian.display_info()
print("Amphibian обьектісі арқылы Boat әдісін шақыру:")
Boat.move(amphibian_obj)


