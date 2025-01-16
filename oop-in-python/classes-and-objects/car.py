class Car:
    @classmethod
    def gas_mileage(cls, miles, gallons):
        mileage = miles / gallons
        print(f'{mileage} miles per gallon')

    def __init__(self, model, model_year, color):
        self.__model = model
        self.__year = model_year
        self.__color = color
        self.current_speed = 0

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    def paint_car(self, color):
        self.color = color
        print(f'Your {color} paint job looks great!')

    def turn_engine_on(self):
        print(f'{self.__model} turned on.')

    def accelerate(self, speed):
        print(f'{self.__model} is accelerating by {speed}m/s!!!')
        self.current_speed += speed

    def brake(self, speed):
        print(f'{self.__model} is decelerating by {speed}m/s!!!')
        self.current_speed -= speed

    def turn_engine_off(self):
        print(f"{self.__model} turned off.")
        self.current_speed = 0

    def get_speed(self):
        print(f"{self.__model}'s current speed is {self.current_speed}m/s!!!")


# lumina = Car('chevy lumina', 1997, 'white')
# lumina.turn_engine_on() # The engine is on!
# lumina.get_speed()    # Your speed is 0 mph.
# lumina.accelerate(20)   # You accelerated 20 mph.
# lumina.get_speed()    # Your speed is 20 mph.
# lumina.accelerate(30)   # You accelerated 30 mph.
# lumina.get_speed()    # Your speed is 50 mph.
# lumina.brake(15)      # You decelerated 15 mph.
# lumina.get_speed()    # Your speed is 35 mph.
# lumina.brake(30)      # You decelerated 30 mph.
# lumina.get_speed()    # Your speed is 5 mph.
# lumina.turn_engine_off()   # Let's park this baby!
#                       # The engine is off
# lumina.get_speed()    # Your speed is 0 mph.
# print()

# print(f'My car is {lumina.color}.')
# # My car is white.

# print(f"My car's model is a {lumina.model}.")
# # My car's model is a chevy lumina.

# print(f"My car's year is {lumina.year}.")
# # My car's year is 1997.

# lumina.color = 'brown'
# print(f'My car is now {lumina.color}.')
# # My car is now brown.

# # lumina.year = 2023
# # # AttributeError: property 'year' of 'Car' object
# # # has no setter

# lumina.paint_car('blue')

Car.gas_mileage(351, 13)
# 27 miles per gallon