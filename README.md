# Minimax Tic-Tac-Toe Simulation Suite

## Description: 

  * Executes any specified number of tic-tac-toe matches between agents of varying skill levels from random to optimal on a specified board size. 

  * Numerous statistics are collected for each simulation allowing for analysis of agent behavior patterns, as well as serving to test the efficiency
    of my algorithms.

  * Some agents utilize alpha-beta pruning resulting in significantly faster runtimes.

  * The sub-optimal agent is intended to mimic the behavior of a human player with the philosophy that a human player will occasionally make judgment
    errors due to sub-optimal foresight. To simulate the inability to consistently consider all scenarios, there is a 10% chance that this agent will
    make a sub-optimal move. This solution yields similar results to simply truncating the tree on 10% of moves.

## Note: This repository is a reupload. 
