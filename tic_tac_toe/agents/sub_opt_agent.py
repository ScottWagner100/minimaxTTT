import math
import random

from sys import setrecursionlimit
from .base_agent import Agent, Move

class SubOptAgent(Agent):
    def __init__(self, player):
        super().__init__(player)
        setrecursionlimit(20_000) # Total possible TTT states

    counter = 0

    def simulate_misjudgement(self):
        temp_random = random.randint(0, 99) # 10% chance of judgement error
        if temp_random >= 89:
            return True
        else:
            return False

    def minimax(self, board, player, alpha, beta):

        self.counter += 1

        max_player = self._player

        if player == 0:
            other_player = 1
        else:
            other_player = 0

        if board.winner == other_player: # assigns utility value and returns board if there is a winner
            if other_player == max_player:
                return {'board': None, 'utility': 1 * (len(board.empty_cells) + 1)}
            else:
                return {'board': None, 'utility': -1 * (len(board.empty_cells) + 1)}
        elif len(board.empty_cells) == 0:
            return {'board': None, 'utility': 0}

        if player == max_player: # sets floor and ceiling
            best_move = {'board': None, 'utility': -math.inf}
        else:
            best_move = {'board': None, 'utility': math.inf}

        for moves in board.empty_cells: # loops through and simulates all possible moves
            for i in range(len(board.empty_cells)):
                moves = board.empty_cells[i]
                board.set_cell(player, *moves)
                minimax_value = self.minimax(board, other_player, alpha, beta)

                # Remove simulated move
                board.set_cell(-1, *moves)
                minimax_value['board'] = moves

                if self.simulate_misjudgement():
                    minimax_value['utility'] = 0

                if player == max_player: # reassigns best move if current simulated move has higher utility value
                    if minimax_value['utility'] > best_move['utility']:
                        best_move = minimax_value
                    alpha = max(best_move['utility'], alpha)
                    if alpha >= beta:
                        break
                else:
                    if minimax_value['utility'] < best_move['utility']:
                        best_move = minimax_value
                    beta = min(best_move['utility'], beta)
                    if alpha >= beta:
                        break

            return best_move

    def next_move(self, board):

        player = self._player
        empty_cells = board.empty_cells
        random_index = random.randint(0, len(empty_cells)-1)

        if (board.is_empty()): # plays random first move
            try:
                index_row = empty_cells[random_index][0]
                index_col = empty_cells[random_index][1]
            except:
                print(len(empty_cells), random_index)
                pass
            return Move(player, index_row, index_col)

        minimax_move = self.minimax(board, player, -math.inf, math.inf)['board']

        print("Pruning Agent: ", self._player, " # of states ", self.counter)

        return Move(player, minimax_move[0], minimax_move[1])


