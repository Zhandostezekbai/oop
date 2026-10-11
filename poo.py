
class Car:
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    def get_name(self):
        return self.nam
    
    def set_name(self, new_name):
        self.name = new_name

    def get_speed(self):
        return self.speed

    def set_speed(self, new_speed):
        self.speed = new_speed

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color


class Mers(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

    def move(self):
        print("VMVM")

    def voice(self):
        print("ARRR")


class Bmw(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

    def move(self):
        print("MMMM")

    def voice(self):
        print("XXXX")


class Mazda(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

    def move(self):
        print("AAAA")

    def voice(self):
        print("KKKK")


mers = Mers("SLC", 300, "red")
bmw = Bmw("m5", 330, "blue")
mazda = Mazda("Mini", 200, "white")

cars = [mers, bmw, mazda]

for car in cars:
    car.voice()