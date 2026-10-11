class Appliance:

    def __init__(self, brand, power):
        self._brand = brand
        self._power = power

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_power(self):
        return self._power

    def set_power(self, power):
        self._power = power


class WashingMachine(Appliance):

    def __init__(self, brand, power):
        super().__init__(brand, power)

    def wash(self):
        print("Кір жуғыш машина жуады")

    def operate(self):
        print("Кір жуғыш машина істеп тұр:")
        self.wash()


class Refrigerator(Appliance):

    def __init__(self, brand, power):
        super().__init__(brand, power)

    def cool(self):
        print("Тоназытқыш салқындатады")

    def operate(self):
        print("Тоназытқыш салқындатып тұр")
        self.cool()


class Microwave(Appliance):

    def __init__(self, brand, power):
        super().__init__(brand, power)

    def heat(self):
        print("Микротолқынды пеш тағамды қыздырады")

    def operate(self):
        print("Микротолқынды пеш тағамды қыздырып тұр")
        self.heat()


kirmachine = WashingMachine("LG", 2000)
refri = Refrigerator("Samsung", 150)
micro = Microwave("Bosch", 350)

appliances = [kirmachine, refri, micro]

kirmachine.wash()
kirmachine.operate()
print("-------------------")

refri.cool()
refri.operate()
print("-------------------")

micro.heat()
micro.operate()
print("-------------------")

for obj in appliances:
    obj.operate()
