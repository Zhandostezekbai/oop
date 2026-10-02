class Appliance:
    def __init__(self,brand,power):
        self._brand=brand
        self._power=power

        def get_brand(self):
            return self._brand
        def set_brand(self):
            self._brand=brand
        def get_power(self):
            return self._power
        def set_power(self):
            self._power=power
class WashingMachine(Appliance):
    def wash(self):
        print("Кір жуғыш машина жуады")
    def operate(self):
        print(f"Кір жуғыш машина ({self._brand}) кір жууды бастады.")

class Refrigerator(Appliance):
    def cool(self):
        print("Тоңазытқыщ салқындатады")
    def operate(self):
        print(f"Тоңазытқыш ({self._brand}) тамақты салқындатып жатыр.")
class Microwave(Appliance):
    def heat(self):
        print("Микротолқынды пеш тағамды қыздырады")    
    def operate(self):
        print(f"Микротолқынды пеш ({self._brand}) тамақты қыздырып жатыр.")
Kirmachine=WashingMachine("LG",2000)
ref=Refrigerator("Samsung",150)
mc=Microwave("Xiaomi",800)

Kirmachine.wash()
ref.cool()
mc.heat()

devices=[Kirmachine,ref,mc]

for dev in devices:
    dev.operate()