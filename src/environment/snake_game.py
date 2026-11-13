"""
This environment is a game engine.

It's responsibility is to answer four question:

   1. Where is the snake?
   2. Where is the food?
   3. What happens when the snake takes an action?
   4. Has the game ended?

It should not know:

    . What a neural network is
    . What Q-learning is
    . How rewards are used for training
    . How the game is displayed
        
"""
import numpy as np
from collections import deque
from typing import Tuple, Deque, Dict, Any, Optional

# Direction constants
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

# Move vectors: a tuple of four (dx, dy) pairs, indexed by direction
MOVE_VECTORS = (
    (0, -1),  # UP (0)
    (1, 0),   # RIGHT (1)
    (0, 1),   # DOWN (2)
    (-1, 0),  # LEFT (3)
)

# Action constants
STRAIGHT, TURN_RIGHT, TURN_LEFT = 0, 1, 2

def turn(direction: int, action: int) -> int:
    """
    Inputs:
          - a direction in {0, 1, 2, 3}
          - an action in {0, 1, 2}
    
    Outputs:
         the new direction in {0, 1, 2, 3}
    
    Raises ValueError if an action is invalid, and if direction is invalid
    """
    if direction not in {0, 1, 2, 3}:
        raise ValueError(f"Invalid direction: {direction}")
    
    if action == STRAIGHT:
        offset = 0

    elif action == TURN_RIGHT:
        offset = 1

    elif action == TURN_LEFT:
        offset = -1

    else:
        raise ValueError(f"Invalid action: {action}")

    return (direction + offset) % len(MOVE_VECTORS)
    

