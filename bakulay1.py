class Transport():
    def __init__(self,name,capacity):
    
    self._name=name
    self._capacity

    def set_name(self,name):
    self._name=name
    def get_name(self):
    return self._name =name


    
    def set_capacity(self,capacity):
    self._capacity=capacity
    def get_name(self):
    return self._capacity = capacity

class Bus(Transport):
    def __init__(self,pick_up,move)
    super(). __init__(self,pick_up,move)
    self._pick_up = pick_up
    self._move =  move
    def pick_up(self):
     print("Автобус жолаушыларды отыргызады")
    def move(self):
     print("Автобус остановколарда журеды")
    self.pick_up()

class Train(Transport):
    def __init__(self,cargo,move)
    super(). __init__(self,cargo,move)
    self._cargo = cargo
    self._move =  move
    def pick_up(self):
     print("Автобус жолаушыларды отыргызады")
    def move(self):
     print("Автобус остановколарда журеды")
    self.cargo()

class Airplane(Transport):
    def __init__(self,take_off,move)
    super(). __init__(self,take_off,move)
    self._take_off = take_off
    self._move =  move
    def pick_up(self):
     print("Автобус жолаушыларды отыргызады")
    def move(self):
     print("Автобус остановколарда журеды")
    self.take_ff()

avtobus=Bus("53",80)
train=Train("Talgo",200)
airplane=Airplane("Fly-Arystan",100)

for movement in move:
    movement.move()




 