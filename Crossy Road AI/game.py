import pygame
import sys
import pymongo
from urllib.parse import quote_plus
from stage import Stage
from board import Board

class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.HEIGHT = self.screen.get_height()
        self.WIDTH = self.screen.get_width()

        pygame.display.set_caption("Crossy Road")

        self.board = None
        self.default_font = pygame.font.Font(None, 25)
        self.stage = Stage.HOME


        password = quote_plus("***REMOVED***")
        cluster = pymongo.MongoClient(f"mongodb+srv://Onion8:{password}@cluster0.tbrc1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = cluster["GalooehsPath"]
        self.collection = db["GalooehData"]


        clock = pygame.time.Clock()

        #Main Game Loop
        while True:
            clock.tick(60)

            if self.stage == Stage.HOME:
                self.homepage()

            if self.stage == Stage.GAME:
                self.startgame()

            if self.stage == Stage.ENDGAME:
                self.endgame()

            if self.stage == Stage.LEADERBOARD:
                self.leaderboard()



    """
    ****THE 4 GAME SCENES****
    :method homepage: starting screen, 2 buttons: start game, check leaderboard
    :method startgame: Playing actual game 
    :method endgame: Screen after death in game
    :method leaderboard: Leaderboard of top scores
    """
    def homepage(self):
        self.screen.fill((0, 0, 0))


        game_button, leader_button = self.create_two_buttons("Play", "Leaderboard")

        self.default_event_check((game_button, True, Stage.GAME), (leader_button, False, Stage.LEADERBOARD))

        pygame.display.flip()


    def startgame(self):
        self.screen.fill((255,123,0))

        player = self.draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.board.move_upward()

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.board.move_horizontal(-1)

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if self.board.move_backward():
                        self.board = None
                        self.stage = Stage.ENDGAME
                        return

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.board.move_horizontal(1)
        
        #Checks Collision
        if self.board.matrix[15-self.board.get_py()] != None:
            for rect in self.board.get_matrix()[15-self.board.get_py()].get_rects():
                if rect.colliderect(player):
                    self.board = None
                    self.stage = Stage.ENDGAME
                    return

        pygame.display.flip()


    def endgame(self):
        self.screen.fill((0,0,0))
        
        game_button, home_button = self.create_two_buttons("Play", "Home")


        self.default_event_check((game_button, True, Stage.GAME), (home_button, False, Stage.HOME))

        pygame.display.flip()

    def leaderboard(self):
        self.screen.fill((155, 223, 23))

        game_button, home_button = self.create_two_buttons("Play", "Home")


        self.default_event_check((game_button, True, Stage.GAME), (home_button, False, Stage.HOME))

        pygame.display.flip()

    """
    ****THE END 4 GAME SCENES****
    """


    #****HELPER FUNCTIONS****
    def create_two_buttons(self, name1, name2):
        """
        Returns two buttons rectangles with names depending on current stage
        :param name1: str
        :param name2: str
        """ 
        surface1 = self.default_font.render(name1, True, (15,236,246), (255,255,255))
        surface2 = self.default_font.render(name2, True, (124,245,23), (255,255,255))

        self.screen.blit(surface1,(100, 100))
        self.screen.blit(surface2, (500, 500))

        rect1, rect2 = surface1.get_rect(), surface2.get_rect()

        rect1.x, rect1.y = 100, 100
        rect2.x, rect2.y = 500, 500

        return rect1, rect2


    def default_event_check(self, changes1, changes2):
        """
        Checks for events for leaderboard scene, home scene. Changes self.board
        :param changes1: Tuple (Rect, bool, Stage)
        :param changes2:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if changes1[0].collidepoint(event.pos):
                    self.board = Board() if changes1[1] else None
                    self.stage = changes1[2]

                if changes2[0].collidepoint(event.pos):
                    self.board = Board() if changes2[1] else None
                    self.stage = changes2[2]

    def draw_board(self):
        """
        returns player object, draws background and cars after change by their speed factor
        """
        matrix = self.board.get_matrix()


        for i, car_row in enumerate(matrix):
            #if not a safe row
            if car_row != None:
                pygame.draw.rect(self.screen, (150,0,0), pygame.Rect(0,(15-i) * 50, self.WIDTH, self.HEIGHT / 16))
                #Draw each car in car row + edit location
                for rect in car_row.get_rects():
                    rect.left -= car_row.get_speed()
                    if rect.left < -150:
                        rect.left = 1350
                    if rect.left > 1350:
                        rect.left = -150
                    pygame.draw.rect(self.screen,(0, 0, 150), rect)
            #else draw safe green row
            else:
                pygame.draw.rect(self.screen, (0,100,0), pygame.Rect(0,(15-i) * 50, self.WIDTH, self.HEIGHT / 16))
        
        #Draw score in top left
        scoreFont = self.default_font.render(str(self.board.get_score()), True, (0,0,0))
        self.screen.blit(scoreFont, (0,0))

        #Draw and return player
        return pygame.draw.circle(self.screen, (123,123,123), (self.board.get_px() * 50 + 25, self.board.get_py() * 50 + 25), 20)

if __name__ == '__main__':   
    Game()