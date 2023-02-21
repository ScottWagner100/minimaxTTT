import random

from .base_agent import Agent, Move

class RandomAgent(Agent):
    def __init__(self, player):
        super().__init__(player)

    def next_move(self, board):
        player = self._player
        empty_cells = board.empty_cells
        random_index = random.randint(0, len(empty_cells)-1)
        try:
            index_row = empty_cells[random_index][0]
            index_col = empty_cells[random_index][1]
        except:
            print(len(empty_cells), random_index)
            pass
        return Move(player, index_row, index_col)