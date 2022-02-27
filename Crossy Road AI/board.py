from random import randint
from car import Car

class Board:


    def __init__(self):
        self.matrix = self.generate_board()
        self.y = 13
        self.x = 12
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
        OR moves up back to starting position
        """
        if self.y != 13:
            self.y -= 1
            return

        for i in range (0, 15):
            self.matrix[i] = self.matrix[i + 1]
            if self.matrix[i] != None:
                for rect in self.matrix[i].get_rects():
                    rect.y += 50

        self.matrix[15] = Car(0) if randint(0, 10) < 8 else None
        self.score += 1
        print(self.score)


    #****GETTERS****
    def get_matrix(self):
        return self.matrix

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_score(self):
        return self.score

    #****SETTERS****
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y