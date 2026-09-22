class ZooAnimal:
    def __init__(self, species, weight):
        self._species = species
        self._weight = weight


    def getter_species(self):
        return self._species

    def getter_weight(self):
        return self._weight


    def setter_species(self, species):
        self._species = species

    def setter_weight(self, weight):
        self._weight = weight


    def sound(self):
        print("Жануар дауыс шығарады")


class Lion(ZooAnimal):
    def roar(self):
        print("Арыстан гүрілдейді")

    def sound(self):
        print("Арыстан ақырады")


class Elephant(ZooAnimal):
    def roar(self):
        print("Піл кернейдейді")

    def sound(self):
        print("Піл дауыс шығарады")


class Penguin(ZooAnimal):
    def swim(self):
        print("Пингвин жүзеді")

    def sound(self):
        print("Пингвин дауыс шығарады")



lion = Lion("Арыстан", 190)
elephant = Elephant("Піл", 5000)
penguin = Penguin("Пингвин", 25)


print(lion.getter_species())
print(lion.getter_weight())


lion.setter_weight(200)
print(lion.getter_weight())


lion.sound()
elephant.sound()
penguin.sound()


lion.roar()
elephant.roar()
penguin.swim()