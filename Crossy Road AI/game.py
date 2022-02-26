import pygame
import sys
from stage import Stage

class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.HEIGHT = self.screen.get_height()
        self.WIDTH = self.screen.get_width()


        pygame.display.set_caption("Crossy Road")

        pygame.event.set_blocked(None)
        pygame.event.set_allowed((pygame.MOUSEBUTTONDOWN, pygame.QUIT))


        self.default_font = pygame.font.Font(None, 25)
        self.stage = Stage.HOME

        clock = pygame.time.Clock()
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


        play_button, leader_button = self.getTwoButtons("Play", "Leaderboard")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if play_button.collidepoint(event.pos):
                    self.stage = Stage.GAME

                if leader_button.collidepoint(event.pos):
                    self.stage = Stage.LEADERBOARD

        pygame.display.flip()

    def startgame(self):
        self.screen.fill((255,123,0))
        pygame.display.flip()


    def endgame(self):
        pass

    def leaderboard(self):
        self.screen.fill((155, 223, 23))

        play_button, home_button = self.getTwoButtons("Play", "Home")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if play_button.collidepoint(event.pos):
                    self.stage = Stage.GAME

                if home_button.collidepoint(event.pos):
                    self.stage = Stage.HOME

        pygame.display.flip()


    """
    ****THE END 4 GAME SCENES****
    """


    #****HELPER FUNCTIONS****
    def getTwoButtons(self, name1, name2):
        """
        Makes two buttons with names depending on curr stage
        :param name1: str
        :param name2: str
        """ 
        buttonName1 = self.default_font.render(name1, True, (15,236,246), (255,255,255))
        buttonName2 = self.default_font.render(name2, True, (124,245,23), (255,255,255))

        self.screen.blit(buttonName1,(100, 100))
        self.screen.blit(buttonName2, (500, 500))

        rect1, rect2 = buttonName1.get_rect(), buttonName2.get_rect()

        rect1.x, rect1.y = 100, 100
        rect2.x, rect2.y = 500, 500

        return rect1, rect2


if __name__ == '__main__':   
    Game()