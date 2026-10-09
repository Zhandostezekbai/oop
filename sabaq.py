from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand: str, model: str, max_speed: float, wheels_count: int):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
        self.wheels_count = wheels_count
        self.current_speed = 0.0

    @abstractmethod
    def start_moving(self):
        """Абстрактный метод: запуск движения/двигателя"""
        pass

    @abstractmethod
    def accelerate(self, amount: float):
        """Абстрактный метод: ускорение"""
        pass

    def stop(self):
        """Общий метод остановки"""
        self.current_speed = 0.0
        print(f"{self.brand} {self.model} остановился.")

    def brake(self, amount: float):
        """Общий метод торможения"""
        self.current_speed = max(0.0, self.current_speed - amount)
        print(f"{self.brand} {self.model} затормозил. Текущая скорость: {self.current_speed} км/ч.")

    def get_info(self):
        """Общий метод вывода информации"""
        print(f"[{self.__class__.__name__}] {self.brand} {self.model} | "
              f"Колёс: {self.wheels_count} | Макс. скорость: {self.max_speed} км/ч | "
              f"Текущая скорость: {self.current_speed} км/ч")



class Car(Vehicle):
    def __init__(self, brand: str, model: str, max_speed: float):
        super().__init__(brand, model, max_speed, wheels_count=4)

    def start_moving(self):
        print(f"{self.brand} {self.model}: Двигатель запущен, машина готова к поездке.")

    def accelerate(self, amount: float):
        self.current_speed = min(self.max_speed, self.current_speed + amount)
        print(f"{self.brand} {self.model} ускорился до {self.current_speed} км/ч.")



class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, max_speed: float):
        super().__init__(brand, model, max_speed, wheels_count=2)

    def start_moving(self):
        print(f"{self.brand} {self.model}: Двигатель зарёван, мотоцикл готов к старту.")

    def accelerate(self, amount: float):
        # Мотоцикл ускоряется быстрее (увеличение на 1.5 * amount)
        boosted_amount = amount * 1.5
        self.current_speed = min(self.max_speed, self.current_speed + boosted_amount)
        print(f"{self.brand} {self.model} быстро ускорился до {self.current_speed} км/ч!")


class Bicycle(Vehicle):
    def __init__(self, brand: str, model: str, max_speed: float = 35.0):
        super().__init__(brand, model, max_speed, wheels_count=2)

    def start_moving(self):
        print(f"{self.brand} {self.model}: Двигателя нет. Начинаем крутить педали!")

    def accelerate(self, amount: float):
        self.current_speed = min(self.max_speed, self.current_speed + amount)
        print(f"{self.brand} {self.model} разгонался до {self.current_speed} км/ч (крутим педали).")



if __name__ == "__main__":
    vehicles: list[Vehicle] = [
        Car("Toyota", "Camry", 210),
        Motorcycle("Yamaha", "R1", 299),
        Bicycle("Giant", "Escape 3", 40)
    ]

    print("=== ДЕМОНСТРАЦИЯ РАБОТЫ ТРАНСПОРТНЫХ СРЕДСТВ ===\n")

    for v in vehicles:
        v.get_info()
        v.start_moving()
        v.accelerate(20)
        v.brake(5)
        v.stop()
        print("-" * 50)