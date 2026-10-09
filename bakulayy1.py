class Transport:
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_capacity(self, capacity):
        self._capacity = capacity

    def get_capacity(self):
        return self._capacity

    def move(self):
        print("Көлік қозғалып барады")


class Bus(Transport):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def pick_up(self):
        print(f"{self._name} автобусы жолаушыларды отырғызады")

    def move(self):
        print(f"{self._name} автобусы аялдамаларда жүреді")


class Train(Transport):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def cargo(self):
        print(f"{self._name} пойызы жүк тасиды")

    def move(self):
        print(f"{self._name} пойызы рельспен жүреді")


class Airplane(Transport):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def take_off(self):
        print(f"{self._name} ұшағы әуеге көтеріледі")

    def move(self):
        print(f"{self._name} ұшағы әуеде ұшады")



avtobus = Bus("53", 80)
train = Train("Talgo", 200)
airplane = Airplane("Fly-Arystan", 100)


transports = [avtobus, train, airplane]

for t in transports:
    t.move()