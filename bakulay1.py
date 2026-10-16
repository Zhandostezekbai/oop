class Sensor:
    def _init_(self, sensor_type):
        self.sensor_type = sensor_type 

    def read_data(self):
        return f"Сенсор ({self.sensor_type}) деректерді оқып жатыр..."


class Robot:
    def _init_(self, sensor_type: str):
        self.sensor = Sensor(sensor_type)

    def execute_task(self):
        print("Робот тапсырманы орындауда.")
        print(self.sensor.read_data())


class Service:
    def _init_(self, name,price):
        self.__price=price
        self._name=name

    def get_price(self):
        return self.__price

    def set_price(self,price):
        self.__price = price

    def display_info(self):
        print(f"Қызмет атауы: {self._name}, Бағасы: {self.get_price()}")

    def provide_service(self):
        print("Қызмет көрсетілуде...")

    def calculate_cost(self):
        return self.get_price()


class Delivery(Service):
    def _init_(self, name,price):
        super()._init_(name, price)

    def calculate_cost(self):
        
        
        return self.get_price() * 5

    def provide_service(self):
        print(f"Жеткізу қызметі орындалуда. Бағасы: {self.calculate_cost()}")


class Installation(Service):
    def _init_(self, name, price):
        super()._init_(name, price)

    def calculate_cost(self):
        return self.get_price() / 2

    def provide_service(self):
        print(f"Орнату қызметі орындалуда. Бағасы: {self.calculate_cost()}")


class CombinedService(Delivery, Installation):
    def _init_(self, name: str, price: float):
           super()._init_(name, price)

    def provide_service(self):
        print("Біріктірілген қызмет (CombinedService) іске қосылды.")


if _name_ == "_main_":
    print("--- 1-тапсырма нәтижесі ---")
    robot = Robot("Оптический / Лидар")
    robot.execute_task()

    print("\n--- 2-тапсырма нәтижесі ---")
    combined = CombinedService("Кешенді қызмет", 1000)
    combined.display_info()
    
    print("\n[Installation класының әдісін нақты шақыру]:")
    Installation.provide_service(combined)