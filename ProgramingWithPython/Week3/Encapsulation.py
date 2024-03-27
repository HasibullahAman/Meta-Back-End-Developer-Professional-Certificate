"""
class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def set_speed(self, value):
        if type(value) == int:
            self.speed = value
        else:
            print("Check you Entry!")

    def get_speed(self):
        return self.speed


car1 = Car(300, "Red")
car1.set_speed("hasib")
print(car1.speed)

"""

# Encapsulation


class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color


car1 = Car(200, "Hasib")
car1.set_speed(450)
print(car1.get_speed())
