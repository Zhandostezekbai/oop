class Device:
    def __init__(self, model, power):
        self.__model = model
        self._power = power

    def turn_on(self):
        print("Құрылғы іске қосылды")

    def computer_info(self):
        return {"model": self.__model,"power": self._power}

    def calculate_time(self):
        return self._power


class Computer(Device):
    def turn_on(self):
        print("Компьютер іске қосылды")

    def display_info(self):
        return self.computer_info()

    def calculate_time(self):
        return self._power * 5


class Printer(Device):
    def __init__(self, model, power, speed):
        super().__init__(model, power)
        self.speed = speed

    def turn_on(self):
        print("Принтер іске қосылды")

    def display_info(self):
        return {"model": self._Device__model,"speed": self.speed}

    def calculate_time(self):
        return self._power / 2


class OfficeDevice(Computer, Printer):
    def __init__(self, computer, printer):
        self.computer = computer
        self.printer = printer
        


computer = Computer("Yepo", 100)
printer = Printer("Print", 50, 20)


print(computer.display_info())
print(computer.calculate_time())


print(printer.display_info())
print(printer.calculate_time())

office = OfficeDevice(computer, printer)

office.computer.turn_on()



