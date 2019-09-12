"""
Creator: Kristina Kolibab
Date: 9/5/19

Implementing Conway's Game of Life
Execution: python .\\devday.py [n] [l]
n - integer for NxN grid
l - life cycles the grid must run through
"""

import numpy as np
import random as rand
import sys
from copy import copy, deepcopy

# Generates the new matrices
def generate(matrix, l):
    for x in range(l):
        print("ROUND " + str(x+1))
        # Deep copy of matrix, used for background updates
        tmp_matrix = matrix[:] 
        # You update the matrix with the tmp only after a full sweep of each cell
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                # Grab the amount of alive neighbors
                neighbors = find_neighbors(matrix, i, j)
                # Depending on cell state, either keep/change alive/dead state
                if(matrix[i][j]):
                    live_cell(neighbors, tmp_matrix, i, j)
                else:
                    dead_cell(neighbors, tmp_matrix, i, j)
        
        # Update matrix with tmp_matrix
        # if I print both matrices here, they are the same ... don't know why
        matrix = deepcopy(tmp_matrix)   
        print("New Neighbors...")
        print_matrix(matrix)

# Helper function, returns the number of live cells surrounding the current cell
def find_neighbors(matrix, i, j):
    # initialize cell
    alive = 0
   
    # rows i, columns j
    #   i   i   i   i           N
    #   i   0   i   i       W --|-- E
    #   i   i   i   i           S
    #   i   i   i   i 

    # somethings wrong: 0 1 1 1 0 --> 0 0 0 0 0
    # the middle one should have survived

    # North
    if(i-1 >= 0):
        if(matrix[i-1][j]):
            alive+=1
        # North West
        if(j-1 >= 0):
            if(matrix[i-1][j-1]):
                alive+=1
        # North East
        if(j+1 < len(matrix)):
            if(matrix[i-1][j+1]):
                alive+=1
    # South
    if(i+1 < len(matrix)):
        if(matrix[i+1][j]):
            alive+=1
        # South West
        if(j-1 >= 0):
            if(matrix[i+1][j-1]):
                alive+=1
        # South East
        if(j+1 < len(matrix)):
            if(matrix[i+1][j+1]):
                alive+=1
    # East
    if(j+1 < len(matrix)):
        if(matrix[i][j+1]):
            alive+=1
    # West
    if(j-1 >= 0):
        if(matrix[i][j-1]):
            alive+=1

    return alive
    
# Helper function, checks if current live cell should stay alive or die
# n - number of alive neighbors, tmp - tmp_matrix
def live_cell(n, tmp, i, j):
    if(n <= 1 or n >= 4):
        # live cell dies
        tmp[i][j] = 0

# Helper function , checks if current dead cell should stay dead or come alive
# n - number of alive neighbors, tmp - tmp_matrix
def dead_cell(n, tmp, i, j):
    if(n == 3):
        # dead cell lives
        tmp[i][j] = 1

# Generates 2D matrix
def gen_matrix(n): 
    matrix = [[np.random.randint(2) for i in range(n)] for j in range(n)]
    return matrix

# Prints the matrix row by row
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Main method
def main():
    n, l = int(sys.argv[1]), int(sys.argv[2])
    matrix = gen_matrix(n)
    print("Initial Neighbors...")
    print_matrix(matrix)
    print('\n')

    # The magic happens here
    generate(matrix, l)

main()