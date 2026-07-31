class Car:
    speed=120
    @classmethod
    def show_speed(cls,accelerate):
        print("speed is:",cls.speed)
        print("new speed is:",cls.speed+accelerate)



Car.show_speed(2)
Car.show_speed(5)
Car.speed=130
Car.show_speed(5)
