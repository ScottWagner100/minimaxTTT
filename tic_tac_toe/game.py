from copy import deepcopy

from .board import Board, CellState
from .player import Player, PLAYER_NAMES
import random


class Game(object):
    def __init__(self, player_x, player_o, size, num_to_win=None,
                 starting_board=None):
        self._player_x = player_x
        self._player_o = player_o

        self._current_player = (Player.X, self._player_x)
        self._next_player = (Player.O, self._player_o)

        if starting_board is None:
            self._board = Board(size=size, num_to_win=num_to_win)
        else:
            self._board = starting_board

        self._num_rounds = self._board.size ** 2 - len(self._board.empty_cells)

    def random_start(self):
        turn = 2
        state_depth = 5 # random.randint(0, (len(self._board.empty_cells) - 1)) # Number of moves in start state.

        for i in range(state_depth):
            rand_empty_cell = random.randrange(len(self._board.empty_cells))
            move_to_pick = self._board.empty_cells[rand_empty_cell]

            if (turn % 2) == 0: # Alternates player turn
                self._board.set_cell(0, *move_to_pick)
            else:
                self._board.set_cell(1, *move_to_pick)

            turn += 1

        return 0 # Arbitrary


    def play(self, is_random_state):
        if is_random_state:
            self.random_start()

        while (self._board.winner is None
               and self._num_rounds < self._board.size ** 2):
            self._show_board()
            if len(self._board.empty_cells) != 0:
                self._make_next_move()
            self._current_player, self._next_player = \
                self._next_player, self._current_player
            self._num_rounds = self._num_rounds + 1

        self._show_board()
        if self._board.winner is None:
            print("It's a draw!")
            return 2

        else:
            print("Congratulations, {} won!".format(
                PLAYER_NAMES[self._board.winner]))

            if self._board.winner == 0:
                return 0
            if self._board.winner == 1:
                return 1


    def _show_board(self):
        print(self._board)
        print("")

    def _make_next_move(self):
        move = self._current_player[1].next_move(deepcopy(self._board))

        assert move.player == self._current_player[0]
        assert self._board.cell(move.row, move.col) == CellState.EMPTY

        self._board.set_cell(move.player, move.row, move.col)
