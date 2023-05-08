from random import randint
from car import Car

class Board:

    def __init__(self):
        self.__score = 0
        self.__matrix = self.__generate_board()
        self.__player_y = 13
        self.__player_x = 12
    
    
    def __generate_board(self):
        """
        Generates beggning board of rows of Car objects or None
        """
        li = [None, None, None] #First three rows will always be safe
        for i in range(12, -1, -1):
            li.insert(0, Car(i, self.__score) if randint(0, 10) < 8 else None)
        return li
    

    def move_upward(self):
        """
        Moves up each car row by 1 and adds 1 to score
        OR moves player up back to starting position
        """
        if self.__player_y != 13:
            self.__player_y -= 1
            return

        for i in range (15, 0, -1):
            self.__matrix[i] = self.__matrix[i - 1]
            if self.__matrix[i] != None:
                for rect in self.__matrix[i].get_rects():
                    rect.top += 50

        self.__matrix[0] = Car(0, self.__score) if randint(0, 10) < 8 else None
        self.__score += 1


    def move_horizontal(self, incrementer):
        """
        Moves player position horizontally
        """
        self.__player_x = self.__player_x + incrementer if self.__player_x + incrementer > -1 and self.__player_x + incrementer < 24 else self.__player_x


    def move_backward(self):
        """
        returns bool if moving down is valid, 
        if valid will move player downs 
        """
        #If player is at bottom of screen, not valid
        if self.__player_y == 15:
            return False

        self.__player_y += 1
        return True

    #****GETTERS****
    def get_matrix(self):
        return self.__matrix

    def get_px(self):
        return self.__player_x

    def get_py(self):
        return self.__player_y

    def get_score(self):
        return self.__score