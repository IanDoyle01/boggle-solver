from string import ascii_uppercase #alphabet
from random import choice #random choice

def make_grid(width, height):
    """
    Creates a grid that will hold all of the tiles
    for a Boggle game
    """
    return {(row, col): choice(ascii_uppercase) 
        for row in range(height)
        for col in range(width)}
    