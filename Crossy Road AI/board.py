from random import randint
from car import Car

class Board:

    def __init__(self):
        self.matrix = self.generate_board()
        self.player_y = 13
        self.player_x = 12
        self.score = 0
    
    def __del__(self):
        print("Board has been deleted")


    def generate_board(self):
        """
        Generates beggning board of rows of Car objects or None
        """
        li = [None, None, None]
        for i in range(3, 16):
            li.append(Car(15-i) if randint(0, 10) < 8 else None)
        return li
    

    def move_upward(self):
        """
        Moves down each car row by 1 and adds 1 to score
        OR moves player up back to starting position
        """
        if self.player_y != 13:
            self.player_y -= 1
            return

        for i in range (0, 15):
            self.matrix[i] = self.matrix[i + 1]
            if self.matrix[i] != None:
                for rect in self.matrix[i].get_rects():
                    rect.y += 50

        self.matrix[15] = Car(0) if randint(0, 10) < 8 else None
        self.score += 1

    def move_horizontal(self, incrementer):
        """
        Moves player position horizontally
        """
        self.player_x = self.player_x + incrementer if self.player_x + incrementer > -1 and self.player_x + incrementer < 24 else self.player_x


    def move_backward(self):
        """
        returns bool if moving down is valid, 
        if valid will move player downs 
        """
        if self.player_y == 15:
            return False

        self.player_y += 1
        return True

    #****GETTERS****
    def get_matrix(self):
        return self.matrix

    def get_px(self):
        return self.player_x

    def get_py(self):
        return self.player_y

    def get_score(self):
        return self.score
