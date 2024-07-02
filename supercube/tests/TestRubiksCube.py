import unittest
from supercube.RubiksCube import RubiksCube
from copy import deepcopy
class TestRubiksCube(unittest.TestCase):
    def setUp(self):
        self.cube = RubiksCube()
        self.clean_state = [[[1,2,3],[4,5,6],[7,8,9]],
                             [[10,11,12],[13,14,15],[16,17,18]],
                             [[19,20,21],[22,23,24],[25,26,27]],
                             [[28,29,30],[31,32,33],[34,35,36]],
                             [[37,38,39],[40,41,42],[43,44,45]],
                             [[46,47,48],[49,50,51],[52,53,54]]]
        self.test_cases = [
            "U R F' U2 B' R2 F' D2 B2 D2 F' U2 R B2 L' D2 U L2 F2 U' R' U2 F2",
            "R F U2 L2 R2 F' U' L' R2 F2 L2 F2 R' D L F' U2 R F2 D' L2 D2 F2",
            "L' B2 U' R2 B2 L' D2 L D2 L2 B2 D F2 D F' U2 R U' B2 U2 B2 R' B2",
            "D' U' B2 F' L2 D2 U' R2 F2 L' F2 D2 L2 R D2 U2 R' B F2 L' D' U F2",
            "B' U' F' L2 D B' R' F L2 B L2 B2 D U' B D' L B L2 U2 F' R2 F2",
            "U R2 D B2 F D2 L2 R' U B2 D L B2 U2 F2 R2 D2 L B L' F2 D' R",
            "D R U' L' U B2 D R U' F2 D2 R2 F2 L2 F' U' F' U' F D F2 D2 U",
            "L2 R2 F' D B U2 B2 U' L2 U L2 U L2 D B2 R2 B2 D2 U2 B2 L' D' F'",
            "R U2 L2 U2 F2 U2 F D2 F D2 F R' D2 B D2 U L' U2 L2 F2 D2 U F2",
            "F' U R D' U' F' D2 U L2 B2 R U' F2 L2 D' B' R B' D2 B' D2 U2 R2",
            "U F2 L' U2 B2 D2 R' B' U2 B2 D2 F2 U2 F2 R' U R B2 D R2 D2 F2",
            "F L' R2 B2 D2 B2 R F2 L U2 L2 U2 B' U2 L' F2 U L2 R2 D B2 R",
            "B2 U F2 U2 R2 D R2 B U2 F' U F2 D2 U' B' U' L R B D2 L R2",
            "L2 D2 F' U L2 B' U' R2 B' F' D R2 D2 F2 D2 B' R2 U2 R' D2 F' R'",
            "D' F L U2 F' L' U B2 L2 B2 R' U R F2 U' R B' D B2 L2 F' R2",
            "U R2 F' U2 R2 D2 R' F U' F L' B' R2 D2 U' F2 U2 B R2 B2 U2 F2",
            "D L2 B2 U2 R2 D2 U' R2 D' U2 B2 D2 L R' B R B2 U L2 R D L'",
            "R2 U F2 D2 R2 F2 U2 B' D2 U R U B2 D2 L R' U' L' B2 U L2 D'",
            "U2 B' U2 B' R B2 R' U2 R D2 U' B2 R2 U' L2 F2 R' D' L2 B2 R2 D",
            "U F2 R2 U L2 U F2 L2 U F2 D' B2 U' F2 L' U2 R2 D2 B' L2 D2 R",
            "L B' F2 U R2 F L2 U B2 R2 F D L' D L' D2 R' U' B2 F' L R'",
            "D B2 L' D B2 L F2 L2 R2 B2 L2 B2 L2 F2 D U' R D F2 R' B' L",
            "D R2 U2 B R' F2 D L2 D' B2 U' R2 B2 U2 B' F' L2 R2 D' L F U'",
            "L D L2 U L2 U2 B2 U' B2 U' B2 D R2 B' R' F D L2 R2 D2 U' F'",
            "D' U2 R2 U R2 D F2 U' R2 B2 F2 R U L' D R2 F D2 B2 D R2",
            "B2 U' L2 F' D R2 U B2 R' U' R2 F2 U L2 U B2 R D2 F2 D2 L",
            "U' R' F2 U2 R2 B2 R2 F' R2 D' U' R B R2 U' L' B R2 D2 U2 L'",
            "U' L' B R2 D2 U2 R' F2 R2 U2 L2 U' R2 B D' B2 U' F2 R' B L",
            "L D' F U' R D B' F' D2 R2 D' B L' U R2 B2 D L2 F' U2 L2",
            "U2 L' D2 B' L2 B' D2 U2 B2 D2 L2 D U2 B2 R' B' F L2 B' L'",
            "R' U2 B2 D2 L2 F2 L' F2 U2 L2 R D B' L' D2 B' L2 F2 U2 L'",
            "L' F' R2 B2 L' F2 L F2 R2 U2 F2 L U L2 D' L2 B2 L2 R B2",
            "U2 R' B2 R U2 L F2 R' F2 R U2 B2 R2 D2 B L' U' R2 F' R2 F",
            "B2 D2 U2 L2 B2 L2 D R2 B2 U2 B' L D2 L' F2 L D2 R2 F' U F",
            "U' L2 F2 R2 F2 R U2 F2 U2 B' R D B2 R' D2 B' U R' B R' F2",
            "R D L2 B2 U L2 U' L2 B2 U R2 F' R2 D' L' F2 R D' R D' B2",
            "L2 R2 F2 L2 U2 L2 F2 U2 R2 D2 F' D' U R' U L B' D' F2 R2 B",
            "U2 R B L2 U' F2 L2 B' D2 B L2 U L2 F2 R' B' U2 R2 U' B' D'",
            "U2 R2 D' L2 U2 F' R' D2 B' L U' F2 L2 B R2 D2 L F' R' U R2",
            "U' B D F' R2 F2 D' B L2 D2 R2 U2 R' B L B2 R2 U' B' L2 D'",
            "D' L2 U2 B L D R2 F' R' B2 L D' F' R F' U' R' D' U2 F2 D",
            "L U2 L2 R2 D2 R U2 B' U2 R' F R B L R B' R2 U F2 R'",
            "F' R' U2 L' U B2 F' R2 D' U R' U' R' D' R' F2 L2 F2 R' U",
            "U2 R' B' L2 U' R2 D' R2 F2 R' F2 U B' R B' R2 U' R' B2 L2 F2",
            "U2 B L2 D2 B' R2 F' U' L2 F L2 D B D2 L2 R' U2 R2 F' U2 B2",
            "D2 L2 F2 R' F2 D2 B' R2 F2 L2 U2 L2 R2 B2 D R2 B L R2 B' R' F",
            "D2 U2 L2 B2 D2 L' R2 D B' R D2 U2 F R2 U2 L2 D2 R' B' L' F2",
            "U' R2 B' R2 F' L2 F2 U B2 U' R2 D2 U' F' U' R' B2 F2 D' L' R'",
            "D2 F R' B D F2 U B2 L D2 R F2 U L2 U' L2 U2 R U R' B2",
            "F R' B2 L2 D L' U R' F2 L2 B2 U2 B2 R2 F U2 F R' U' B D'"
        ]

    def test_initial_state(self):
        self.assertEqual(self.cube.get_state(), [[[1,2,3],[4,5,6],[7,8,9]],
                                                 [[10,11,12],[13,14,15],[16,17,18]],
                                                 [[19,20,21],[22,23,24],[25,26,27]],
                                                 [[28,29,30],[31,32,33],[34,35,36]],
                                                 [[37,38,39],[40,41,42],[43,44,45]],
                                                 [[46,47,48],[49,50,51],[52,53,54]]])

    def _get_opposite_sequence(self, scramble):
        opposite = ""
        sequence = scramble.strip().split(" ")[::-1]
        for move in sequence:
            if move[-1] == "'":
                opposite += move[0:-1] + " "
            elif move[-1] != "'" and move[-1] != "2":
                opposite += move + "' "
            else:
                opposite += move + " "
        return opposite.strip()

    def test_moves(self):
        for i, scramble in enumerate(self.test_cases):
            with self.subTest(test_number=i):
                print(scramble)
                self.cube.move(scramble)
                print(self._get_opposite_sequence(scramble))
                self.cube.move(self._get_opposite_sequence(scramble))
                self.assertEqual(self.cube.get_state(), self.clean_state)
            self.cube.reset()


