
import pytest 
from ..app.api.endpoints.nreinas import solve_n_queens

@pytest.mark.parametrize("n, expected_count", [
    (1, 1),
    (4, 2),
    (5, 10),
    (6, 4),
    (7, 40),
    (8, 92),
    (9, 352),
    (10, 724),
    (11, 2680),
    (12, 14200),
    #(13, 73712),  11 passed in 27.65s
    #(14, 365596), 12 passed in 175.99s (0:02:55)
])
def test_solve_n_queens(n, expected_count):
    solutions = solve_n_queens(n)
    assert len(solutions) == expected_count