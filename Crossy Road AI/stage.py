from enum import Enum, auto

class Stage(Enum):
    """
    Values to represent which stage/state the game is in
    """
    HOME = auto()
    GAME = auto()
    LEADERBOARD = auto()
    ENDGAME = auto()

