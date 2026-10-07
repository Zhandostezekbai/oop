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


class Refrigerator(Appliance):

    def __init__(self, brand, power):
        super().__init__(brand, power)

    def cool(self):
        print("Тоназытқыш салқындатады")

    def operate(self):
        print("Тоназытқыш салқындатып тұр")


class Microwave(Appliance):

    def __init__(self, brand, power):
        super().__init__(brand, power)

    def heat(self):
        print("Микротолқынды пеш тағамды қыздырады")

    def operate(self):
        print("Микротолқынды пеш тағамды қыздырып тұр")


kirmachine = WashingMachine("LG", 2000)
refri = Refrigerator("Samsung", 150)
micro = Microwave("Bosch", 350)

appliances = [kirmachine, refri, micro]

for obj in appliances:
    obj.operate()
