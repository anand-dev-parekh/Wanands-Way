from enum import Enum, auto

class Stage(Enum):
    """
    Values to represent which stage/state the game is in
    """
    LOGIN_OR_REGISTER = auto()
    LPASSWORD = auto()
    RPASSWORD = auto()
    MENU = auto()
    GAME = auto()
    LEADERBOARD = auto()
    ENDGAME = auto()