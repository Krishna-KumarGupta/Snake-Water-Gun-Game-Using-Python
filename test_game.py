import pytest
from game import gameWin  # Importing the function from your game script

@pytest.mark.parametrize("comp, you, expected", [
    ('s', 's', None),  # Tie case
    ('s', 'w', False),  # Snake beats Water (Comp wins)
    ('s', 'g', True),   # Gun beats Snake (You win)
    ('w', 'w', None),  # Tie case
    ('w', 'g', False),  # Water beats Gun (Comp wins)
    ('w', 's', True),   # Snake beats Water (You win)
    ('g', 'g', None),  # Tie case
    ('g', 's', False),  # Gun beats Snake (Comp wins)
    ('g', 'w', True)    # Water beats Gun (You win)
])
def test_gameWin(comp, you, expected):
    assert gameWin(comp, you) == expected
