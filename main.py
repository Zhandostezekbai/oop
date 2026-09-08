# мынау класс

# класс дегеніміз әзірлеуші өзі анықтайтын деректер типі;
# объект дегеніміз сол кластың айнымалысы

# кластың атрибуттары:
    # 1) өріс (field) - кластың ішіндегі кез келген айнымалы
    # 2) свойство (property) - кластың ішіндегі өріске доступ
    # 3) әдіс (method) - кластың ішіндегі кез келген функция (def)

    
# ООП парадигмалары:
#     1) Инкапсуляция (encapsulation) - кластың ішіндегі атрибуттарды жасыру концепциясы
# Access modifiers: 
    # 1) PUBLIC - класс атрибуты (кез келген) кластың сыртында да көріне береді
    # 2) PROTECTED - кластың өзінде және мұрагерлерінде көрінеді (python-да public сияқты істейді)
    # 3) PRIVATE - кластың ішінде ғана көрінеді
#     2) Мұрагерлік (inheritance) - кластың басқа кластарға кодын бере алу механизмі
#     3) Полиморфизм (polymorphysm) - бір кластың ішіндегі әдіс басқа класта өзгеріп жазылуы
    # Полиморфизм түрлері:
    #     1) OVERRIDING (переопределение) - қайта анықтау - әдістің басқа класта тек ішкі кодының өзгеруі
    #     2) OVERLOADING (перегрузка) - қайта жүктеу - әдістің параметрлер саны мен кодының өзгеруі (Python-да жоқ нәрсе)
    #     3) HIDING (сокрытие) - жасыру - әдістің атынан басқасының барлығының өзгеруі
class Cosmetics:
    # мынау класс конструкторы
    # объект құрылған кезде шақырылатын функция
    # self - объектіге сілтеме
    def __init__(self, face_type: str, price: float, brand: str) -> None:
        self.face_type = face_type # өріс - public
        self._price = price # өріс - protected
        self.__brand = brand # өріс - private
        
        
    # геттер
    def get_face_type(self) -> str:
        return self.face_type

    # сеттер
    def set_face_type(self, new_face_type) -> None:
        self.face_type = new_face_type

    # әдіс (method)
    # бұл жерде метод 1 параметр қабылдайды - discount
    # self деген параметр емес!
    def sell(self, discount) -> None:
        self._price = self._price - discount


# мынау объект
cosmetics = Cosmetics("brows", 100, "Dior")

print("FACE TYPE IS:", cosmetics.get_face_type())
cosmetics.set_face_type("lashes")
print("FACE TYPE IS:", cosmetics.get_face_type())

# print("PRICE BEFORE: ", cosmetics.price)
cosmetics.sell(0.5)
# print("PRICE AFTER: ", cosmetics.price)

print("PRICE IS: ", cosmetics._price)


class Lipstick(Cosmetics):
    def __init__(self, face_type, price, brand):
        super().__init__(face_type, price, brand)
        # super деген суперкласс немесе атасы (Cosmetics класы)

    def sell(self, discount1, discount2) -> float:
        self._price = self._price - discount1 - discount2
        return self._price

lipstick = Lipstick("lips", 3000, "SHANEL")
