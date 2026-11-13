import pytest
from src.environment.snake_game import turn

# 1. test all 12 combinations
@pytest.mark.parametrize(
    "direction, action, expected",
    [
        (0, 0, 0),
        (0, 1, 1),
        (0, 2, 3),
        (1, 0, 1),
        (1, 1, 2),
        (1, 2, 0),
        (2, 0, 2),
        (2, 1, 3),
        (2, 2, 1),
        (3, 0, 3),
        (3, 1, 0),
        (3, 2, 2),
    ]
)
def test_turn(direction, action, expected):

    result = turn(direction, action)

    assert result == expected


# 2. test invalid actions
@pytest.mark.parametrize("action", [-1, 3])
def test_invalid_actions_raises_value_error(action):
    with pytest.raises(ValueError):
        turn(0, action)


# 3. test invalid directions
@pytest.mark.parametrize("direction", [-1, 4])
def test_invalid_directions_raises_value_error(direction):
    with pytest.raises(ValueError):
        turn(direction, 0)

# 4. test inverse-turn property
@pytest.mark.parametrize("direction", [0, 1, 2, 3])
def test_inverse_turn_property(direction):
    x1 = turn(turn(direction, 1), 2)
    x2 = turn(turn(direction, 2), 1)
    # Right followed by left restores the original direction
    assert x1 == direction
    # Left followed by right restores the original direction
    assert x2 == direction
