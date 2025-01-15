class Car:
    def __init__(self, model, model_year, color):
        self.model = model
        self.model_year = model_year
        self.color = color
        self.current_speed = 0

    def turn_engine_on(self):
        print(f'{self.model} turned on.')

    def accelerate(self, speed):
        print(f'{self.model} is accelerating by {speed}m/s!!!')
        self.current_speed += speed

    def brake(self, speed):
        print(f'{self.model} is decelerating by {speed}m/s!!!')
        self.current_speed -= speed

    def turn_engine_off(self):
        print(f"{self.model} turned off.")
        self.current_speed = 0

    def get_speed(self):
        print(f"{self.model}'s current speed is {self.current_speed}m/s!!!")


lumina = Car('chevy lumina', 1997, 'white')
lumina.turn_engine_on() # The engine is on!
lumina.get_speed()    # Your speed is 0 mph.
lumina.accelerate(20)   # You accelerated 20 mph.
lumina.get_speed()    # Your speed is 20 mph.
lumina.accelerate(30)   # You accelerated 30 mph.
lumina.get_speed()    # Your speed is 50 mph.
lumina.brake(15)      # You decelerated 15 mph.
lumina.get_speed()    # Your speed is 35 mph.
lumina.brake(30)      # You decelerated 30 mph.
lumina.get_speed()    # Your speed is 5 mph.
lumina.turn_engine_off()   # Let's park this baby!
                      # The engine is off
lumina.get_speed()    # Your speed is 0 mph.