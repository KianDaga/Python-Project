class Car:

    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self ,speed):
        self.speed += speed
        print(f"The {self.make, self.model} is now going: {self.speed} km/h")

    def brake(self,speed):
        self.speed -= speed
        print(f"The {self.make, self.model} is now going: {self.speed} km/h")


car1 = Car("Bugatti", "Chiron", 2024, 0)
car1.accelerate(100000000)
car1.brake(500000)