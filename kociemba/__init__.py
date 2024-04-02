import kociemba
from .pykociemba import search

def _solve(cube, pattern, max_depth=24):
    errors = {
        'Error 1': 'There is not exactly one facelet of each colour',
        'Error 2': 'Not all 12 edges exist exactly once',
        'Error 3': 'Flip error: One edge has to be flipped',
        'Error 4': 'Not all corners exist exactly once',
        'Error 5': 'Twist error: One corner has to be twisted',
        'Error 6': 'Parity error: Two corners or two edges have to be exchanged',
        'Error 7': 'No solution exists for the given maxDepth',
        'Error 8': 'Timeout, no solution within given time'
    }
    if pattern is not None:
        cube = search.patternize(cube, pattern)
    res = search.Search().solution(cube, max_depth, 1000, False).strip()
    if res in errors:
        raise ValueError(errors[res])
    else:
        return res

def solve(cubestring, patternstring=None, max_depth=24):
    """
    Solve a Rubik's cube using two-phase algorithm.

    >>> solve("BBURUDBFUFFFRRFUUFLULUFUDLRRDBBDBDBLUDDFLLRRBRLLLBRDDF")
    "B U' L' D' R' D' L2 D' L F' L' D F2 R2 U R2 B2 U2 L2 F2 D'"

    >>> kociemba.solve('FLBUULFFLFDURRDBUBUUDDFFBRDDBLRDRFLLRLRULFUDRRBDBBBUFL', 'BBURUDBFUFFFRRFUUFLULUFUDLRRDBBDBDBLUDDFLLRRBRLLLBRDDF')
    u"R' D2 R' U2 R F2 D B2 U' R F' U R2 D L2 D' B2 R2 B2 U' B2"
    """

    return _solve(cubestring, patternstring, max_depth)

__all__ = ['solve']
