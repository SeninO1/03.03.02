class Transport:
    def __init__ (self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
       
class Autobus(Transport):
    capacity = 50
    
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
    
    
    def seating_capacity(self):
        print(f'Вместимость одного автобуса {h1.name}:  {h1.capacity} пассажиров')

h1 = Autobus('Renault Logan', 10, 20)
h1.seating_capacity()