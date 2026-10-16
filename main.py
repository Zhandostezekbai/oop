class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Издает какой-то звук"

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "Гав-гав!"

    def __str__(self):
        return f"Собака породы {self.breed}. " + super().__str__()


class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Исправлен отступ, который был в вашем примере
        self.breed = breed

    def make_sound(self):
        return "Мяу!"

    def __str__(self):
        return f"Кошка породы {self.breed}. " + super().__str__()


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "Чирик-чирик!"

    def __str__(self):
        return f"Птица с размахом крыльев {self.wingspan} см. " + super().__str__()


# --- Пример использования кода ---
if __name__ == "__main__":
    # Создаем объекты разных классов
    dog = Dog(name="Бобик", age=3, breed="Немецкая овчарка")
    cat = Cat(name="Мурка", age=2, breed="Сиамская")
    bird = Bird(name="Кеша", age=1, wingspan=25)

    # Помещаем их в список, чтобы обработать в цикле (полиморфизм)
    animals = [dog, cat, bird]

    print("=== Список наших животных ===")
    for animal in animals:
        print(animal)
        print(f"Что говорит: {animal.make_sound()}")
        print("-" * 30)