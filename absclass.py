from abc import ABC,abstractmethod
class Transport(ABC):
    def __init__(self,brand:str,model:str,max_speed:int,wheels:int):
        self.brand=brand
        self.model=model
        self.max_speed=max_speed
        self.wheels=wheels
        self.current_speed=0

@abstractmethod
def start_moving(self):
    pass

@abstractmethod
def accelerate(self,value:int):
    pass
@abstractmethod
def brake(self,value:int):
    self.current_speed=max(0,self.current_speed-value)
    print(
        f"{self.brand}{self.model:self.current_speed}"
    )
def stop(self):
    self.current_speed=0
    print(
        f"{self.brand}{self.model}"
    )
def get_info(self):
    print(
        f"[{self.__class__.__name__}]{self.brand}{self.model}|"
         f"Дөңгелектер: {self.wheels} | Макс. жылдамдық: {self.max_speed} км/сағ | "
            f"Ағымдағы жылдамдық: {self.current_speed} км/сағ"
        )


# 2. Автомобиль класы
class Car(Transport):

    def _init_(self, brand: str, model: str, max_speed: int):
        super()._init_(brand, model, max_speed, wheels=4)

    def start_moving(self):
        print(
            f"Автомобиль {self.brand} {self.model} қозғалтқышын оталдырып, жүріп кетті."
        )

    def accelerate(self, value: int):
        self.current_speed = min(self.max_speed, self.current_speed + value)
        print(
            f"Автомобиль жылдамдықты {self.current_speed} км/сағ-қа дейін арттырды."
        )


# 3. Мотоцикл класы
class Motorcycle(Transport):

    def _init_(self, brand: str, model: str, max_speed: int):
        super()._init_(brand, model, max_speed, wheels=2)

    def start_moving(self):
        print(
            f"Мотоцикл {self.brand} {self.model} қозғалтқышын іске қосып, қозғалысты бастады."
        )

    def accelerate(self, value: int):
        # Ерекшелігі: Жылдамдықты автомобильнікіне қарағанда тезірек жинайды
        boosted_value = int(value * 1.5)
        self.current_speed = min(
            self.max_speed, self.current_speed + boosted_value
        )
        print(
            f"Мотоцикл жылдамдықты тез арада {self.current_speed} км/сағ-қа арттырды."
        )


# 4. Велосипед класы
class Bicycle(Transport):

    def _init_(self, brand: str, model: str, max_speed: int):
        super()._init_(brand, model, max_speed, wheels=2)

    def start_moving(self):
        print(
            f"Велосипедтің {self.brand} {self.model} двигателі жоқ. Қозғалыс үшін педальді айналдыру керек."
        )

    def accelerate(self, value: int):
        self.current_speed = min(self.max_speed, self.current_speed + value)
        print(
            f"Велосипед педаль айналдыру арқылы жылдамдықты {self.current_speed} км/сағ-қа жеткізді."
        )


# 5. Демонстрациялық бағдарлама
if _name_ == "_main_":
    vehicles = [
        Car("Toyota", "Camry", 220),
        Motorcycle("Yamaha", "R1", 299),
        Bicycle("Trek", "Marlin 7", 45),
    ]

    for vehicle in vehicles:
        print("\n" + "=" * 50)
        vehicle.get_info()
        vehicle.start_moving()
        vehicle.accelerate(30)
        vehicle.brake(10)
        vehicle.stop()
    