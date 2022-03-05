import pygame
import sys

from stage import Stage
from board import Board
from user import User

class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Wanand's Way")


        self.board = None
        self.default_font = pygame.font.Font(None, 25)
        self.stage = Stage.LOGIN_OR_REGISTER
        self.user = User()


        clock = pygame.time.Clock()

        #Main Game Loop
        while True:
            clock.tick(60)

            if self.stage is Stage.LOGIN_OR_REGISTER:
                self.login_or_register()

            if self.stage is Stage.LPASSWORD or self.stage is Stage.RPASSWORD:
                self.put_password()

            if self.stage is Stage.MENU:
                self.menupage()

            if self.stage is Stage.GAME:
                self.startgame()

            if self.stage is Stage.ENDGAME:
                self.endgame()

            if self.stage is Stage.LEADERBOARD:
                self.leaderboard()



    """
    ****THE 6 GAME SCENES****
    :method login_or_register: prompts user login or register
    :method put_password: prompts user to put password + username and enter into menupage
    :method menupage: 2 buttons-start game, check leaderboard
    :method startgame: Playing actual game 
    :method endgame: Screen after death in game
    :method leaderboard: Leaderboard of top scores
    """

    def login_or_register(self):
        self.screen.fill((0,0,0))
        login_button, register_button = self.create_text("Login", 300, 300), self.create_text("Register", 600, 600)      
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_button_collision(event, login_button, Stage.LPASSWORD)
                self.is_button_collision(event, register_button, Stage.RPASSWORD)

        pygame.display.flip()

    def put_password(self):
        self.screen.fill((100, 0, 100))
        
        username_input_box, password_input_box = self.create_textbox((100, 100, 0), 100, 200, 500, 100), self.create_textbox((100, 100, 0), 100, 500, 500, 100)
        
        button_name = "Login" if self.stage is Stage.LPASSWORD else "Register"
        enter_button = self.create_text(button_name, 900, 600)


        #Blit user inputted username, password
        user_name_text = self.default_font.render(self.user.get_user_name(), True, (0,0,0))
        center_of_user_box = user_name_text.get_rect(center=username_input_box.center)
        self.screen.blit(user_name_text, center_of_user_box)
        
        password_text = self.default_font.render(self.user.get_password(), True, (0,0,0))
        center_of_password_box = password_text.get_rect(center=password_input_box.center)
        self.screen.blit(password_text, center_of_password_box)

        #Adds error message, username label and password label
        self.create_text(self.user.get_error_message(), 700, 200)
        self.create_text("Username:", 100, 175)
        self.create_text("Password:", 100, 475)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if username_input_box.collidepoint(event.pos):
                    self.user.change_mode(1)
                elif password_input_box.collidepoint(event.pos):
                    self.user.change_mode(2)
                else:
                    self.user.change_mode(0)
                    if enter_button.collidepoint(event.pos):
                        if self.user.connect_account(self.stage):
                            self.stage = Stage.MENU
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_TAB and event.key != pygame.K_RETURN and event.key != pygame.K_ESCAPE:
                    self.user.edit_active(event.unicode)
        
        pygame.display.flip()

    def menupage(self):
        self.screen.fill((0,0,0))

        game_button, leader_button = self.create_text("Play", 100, 100), self.create_text("Leaderboard", 500, 500)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_button_collision(event, game_button, Stage.GAME, Board())
                self.is_button_collision(event, leader_button, Stage.LEADERBOARD)

        pygame.display.flip()


    def startgame(self):

        #Draws background and Cars
        player = self.draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #Moves Player
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.board.move_upward()

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.board.move_horizontal(-1)

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if not self.board.move_backward():
                        self.stage = Stage.ENDGAME
                        return

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.board.move_horizontal(1)
        
        #Checks Collision
        if self.board.get_matrix()[self.board.get_py()] != None:
            for rect in self.board.get_matrix()[self.board.get_py()].get_rects():
                if rect.colliderect(player):
                    self.stage = Stage.ENDGAME
                    return

        pygame.display.flip()


    def endgame(self):
        self.screen.fill((0,0,0))
        
        game_button, menu_button, leaderboard_button =  self.create_text("Play", 100, 100), self.create_text("Home", 500, 500), self.create_text("Leaderboard", 600, 700)

        scoreFont = self.default_font.render(str(self.board.get_score()), True, (0,255,0))
        self.screen.blit(scoreFont, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_button_collision(event, game_button, Stage.GAME, Board())
                self.is_button_collision(event, menu_button, Stage.MENU)
                self.is_button_collision(event, leaderboard_button, Stage.LEADERBOARD)

        pygame.display.flip()


    def leaderboard(self):
        self.screen.fill((123,12,242))


        game_button, menu_button =  self.create_text("Play", 100, 100), self.create_text("Home", 500, 500)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_button_collision(event, game_button, Stage.GAME, Board())
                self.is_button_collision(event, menu_button, Stage.MENU)

        pygame.display.flip()

    """
    ****THE END 4 GAME SCENES****
    """


    #****HELPER FUNCTIONS****
    def create_text(self, name, x, y):
        """
        Generates text with name and location where name shall reside
        :param name: str
        :param x: int
        :param y: int
        """
        surface = self.default_font.render(name, True, (15,236,246), (255,255,255))

        self.screen.blit(surface,(x, y))

        rect = surface.get_rect()
        rect.x, rect.y = x, y
        return rect


    def create_textbox(self, color, x, y, width, height):
        """
        Creates textbox at specified location
        :param color: Tuple (int, int, int)
        :param x: int
        :param y: int
        :param width: width of textbox
        :param height: height of textbox
        """
        return pygame.draw.rect(self.screen, color, pygame.Rect(x,y,width,height))


    def is_button_collision(self, event, button, newStage, board_cleanup=None):
        """
        Checks if button is clicked, sets new stage, cleans up Board or makes board
        :param event: pygame.event
        :param button: Rect
        :param newStage: Stage
        :param(OPTIONAL) cleanup: Board
        """
        if button.collidepoint(event.pos):
            self.stage = newStage
            self.board = board_cleanup

    def draw_board(self):
        """
        returns player object, draws background and cars after change by their speed factor
        """
        matrix = self.board.get_matrix()


        for i, car_row in enumerate(matrix):
            #if not a safe row
            if car_row != None:
                pygame.draw.rect(self.screen, (150,0,0), pygame.Rect(0,i*50,1200,50))

                #Move cars in each row
                car_row.move_cars()

                #Draw each car in car row
                for rect in car_row.get_rects():
                    pygame.draw.rect(self.screen,(0,0,150), rect)
            #else draw safe green row
            else:
                pygame.draw.rect(self.screen, (0,100,0), pygame.Rect(0,i*50,1200,50))
        
        #Draw score in top left
        scoreFont = self.default_font.render(str(self.board.get_score()), True, (0,0,0))
        self.screen.blit(scoreFont, (0,0))

        #Draw and return player
        return pygame.draw.circle(self.screen, (123,123,123), (self.board.get_px() * 50 + 25, self.board.get_py() * 50 + 25), 20)
if __name__ == '__main__':   
    Game()