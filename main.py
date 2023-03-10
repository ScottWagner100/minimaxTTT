
import numpy as np

from tic_tac_toe.game import Player, Game
from tic_tac_toe.agents.console_input_agent import ConsoleInputAgent
from tic_tac_toe.agents.random_agent import RandomAgent
from tic_tac_toe.agents.dfs_agent import DFSAgent
from tic_tac_toe.agents.ab_pruning_agent import ABPruningAgent
from tic_tac_toe.agents.sub_opt_agent import SubOptAgent
import timeit

AGENTS = [
    ("Human", ConsoleInputAgent),
    ("Random Agent", RandomAgent),
    ("DFS Agent", DFSAgent),
    ("Alpha-Beta Pruning Agent", ABPruningAgent),
    ("Sub-Optimal Agent", SubOptAgent)
]


def _pick_agent(player):
    def _try_pick():
        try:
            list_of_agents = "\n".join(
                map(lambda x: "\t{} - {}".format(x[0], x[1][0]),
                    enumerate(AGENTS)))
            agent = int(
                input("Available agents: \n{}\nPick an agent [0-{}]: ".format(
                    list_of_agents, len(AGENTS) - 1)))
            return agent
        except ValueError:
            return None

    agent = _try_pick()

    while agent is None:
        print("Incorrect selection, try again.")
        agent = _try_pick()

    return AGENTS[agent][1](player)


def main():
    print("Choosing player X...")
    player_x = _pick_agent(Player.X)

    print("Choosing player O...")
    player_o = _pick_agent(Player.O)
    play = "y"

    #while play == "y":

    x_wins = 0
    o_wins = 0
    draw_count = 0

    game_count = input("Number of games: ")
    game_count = int(game_count)

    random_start_input = input("Random Starting State? y/n")
    if random_start_input == "y":
        is_random_state = True
    else:
        is_random_state = False

    board_size = int(input("Enter a Board Size >= 3: "))
    if board_size <= 3:
        board_size = 3

    start_time = timeit.default_timer()

    time_data = []


    for x in range(game_count):
        sub_start_time = timeit.default_timer()
        game = Game(player_x, player_o, board_size)
        temp_score = game.play(is_random_state)

        if temp_score == 0:
            x_wins += 1
        if temp_score == 1:
            o_wins += 1
        if temp_score == 2:
            draw_count += 1

        sub_stop_time = timeit.default_timer()
        sub_total_time = sub_stop_time - sub_start_time
        time_data.append(sub_total_time)


    stop_time = timeit.default_timer()

    run_time = stop_time - start_time
    run_time_per_game = run_time / game_count
    standard_error_time = np.std(time_data) / np.sqrt(np.size(time_data))

    print("\nRun time at " + str(game_count) + " is " + str(round(run_time, 8)))
    print("Run time per game: " + str(round(run_time_per_game, 8)))
    print("Standard Error: " + str(standard_error_time))

     #   play = input("Play again? y/[n]: ")

    print("x Wins: " + str(x_wins) + "\no wins: " + str(o_wins) + "\nDraws: " + str(draw_count))

if __name__ == "__main__":
    main()

quit(0)