from random import randint
from pygame import Rect


class Car:

    def __init__(self, height_factor, score_factor):
        self.__cars = self.__generate_rects(height_factor)

        score_factor = int(score_factor / 50)
        self.__speed = randint(3 + score_factor, 7 + score_factor) * (-1 if randint(0,1) == 0 else 1)


    def __generate_rects(self, i):
        """
        Generates 1-3 rectangles returns it to the Car
        """
        num = randint(0, 4)

        if num == 0:
            return [Rect(randint(-150, 1350), i*50+ 5, 75, 40)]

        if num == 1 or num == 2:
            return [Rect(randint(-150, 1350), i*50+ 5, 75, 40), Rect(randint(-150, 1350), i*50+ 5, 75, 40)]

        return [Rect(randint(-150, 1350), i*50+ 5, 75, 40), Rect(randint(-150, 1350), i*50+ 5, 75, 40), Rect(randint(-150, 1350), i*50+ 5, 75, 40)] 

    def move_cars(self):
        """
        Moves the rectangles location in each car row
        """
        for rect in self.__cars:
            rect.left -= self.__speed
            if rect.left < -150:
                rect.left = 1350
            if rect.left > 1350:
                rect.left = -150

    #****GETTERS****
    def get_rects(self):
        return self.__cars 