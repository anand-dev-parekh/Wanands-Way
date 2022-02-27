from random import randint
from pygame import Rect


class Car:

    def __init__(self, height_factor):
        self.cars = self.generate_rects(height_factor)
        self.speed = randint(2, 9) * (-1 if randint(0,1) == 0 else 1)


    def generate_rects(self, i):
        """
        Generates 1-3 rectangles returns it to the Car
        """
        num = randint(0, 4)

        if num == 0:
            return [Rect(randint(-150, 1350), i*50+ 5, 75, 40)]

        if num == 1 or num == 2:
            return [Rect(randint(-150, 1350), i*50+ 5, 75, 40), Rect(randint(-150, 1350), i*50+ 5, 75, 40)]

        return [Rect(randint(-150, 1350), i*50+ 5, 75, 40), Rect(randint(-150, 1350), i*50+ 5, 75, 40), Rect(randint(-150, 1350), i*50+ 5, 75, 40)] 


    #****GETTERS****
    def get_rects(self):
        return self.cars       

    def get_speed(self):
        return self.speed


    
