import unittest
from supercube.NCube import NCube
from copy import deepcopy

class TestBigCube(unittest.TestCase):
    def setUp(self):
        self.cube = NCube(19)
        self.clean_state = deepcopy(self.cube.get_state())
        self.test_cases = [
            "7Fw 5Bw' 5Dw' 2Fw2 6R",
            "4Dw 6U 6D' 2D' 3Rw 3Lw' 2Rw 9Bw' 7L' 6D B' B 2F2 7Fw' 5L 2Rw2 8F' 2R 9D2 7Bw2 3D' 7Lw2 3F2 6Uw 5Lw2 6Uw 4Uw' 7Bw'",
            "4Dw2 7F2 4Dw' 7Rw2 2Lw' 2Bw 6Lw2 2Lw' B 2F 8Rw' 5Bw2 9D2 4Fw 2Bw 9Lw' 8Lw2 7L 6B 9F2 9D2",
            "8Uw 7R' U' 8Fw' R2 8Uw 5L' 5F2 2Dw' 4L2 2Lw2 9Lw 5Uw 4B' 7D 3R' 3Lw2 8U2 6Dw' 6Bw' 5Rw2 3U2 F2 2Rw2 4Dw2 2Fw",
            "7Rw 9B2 9Bw2 7Lw2 6L2 2Dw 7Rw 3F' 2B R 6F 3F2 3L 7R' 9Rw' D 9Rw2 7D2 5F2 8R' 6B 4R 7U2 4Bw' F' 5Fw 9B2 7B",
            "4Fw 6D 2Rw2 2D 9D 5R' 2Uw 5Dw' 5R 6Fw 6Bw 3D 3Bw' 8Rw' 8F2 D 4U' 8U' 8U 6B' 4R 3R 7Bw",
            "L2 4U' 7L2 8R' 2B2 3D 9Fw L' 5Dw2 7D2 4Rw 7B' 2B B 5Rw 2F' 9Lw2 3Dw2 2Fw' 3L2 5B2 6B2 9Bw' 6B2 8D 4R2 2Bw2 3Bw 9Dw' 9Lw'",
            "6Lw 6Fw2 4Bw2 5R 9Fw2 9B2 3Fw2 2Fw 8Dw' 6Fw' 5Rw' 7R' 6L2 6D 3L 7Lw' 7Rw' 3B' R' 3Bw' 3Rw2 6Lw2 2Dw2 5Bw 5Lw' 8Uw'",
            "7U' 9Dw 3Bw' 5R2 5Bw2 6Uw' 6Lw2 3Fw 2D' 3R' 7L2 4B2 8L2 8Lw' F' 4Rw2 8Rw' 6R 3Uw' 6Fw 7F' 9Dw' 5Uw2",
            "9B 9F2 9Bw' 5Fw2 4Lw 4Bw2 R 9R2 4U2 8B 3F 3Fw' D2 5B' 7Rw2 5Lw 3F2 8Uw2 5Bw' 8Lw'",
            "4D' 5R D' 2Bw 2D2 3L' 7R' 5Bw' 4Rw 9Dw 9Bw 9Bw' 6L2 9B2 5B' 5Lw' 5Lw2 5U 4B2 8Uw 4L' 6B2 2R2 B' 5L2 5D'",
            "8Rw' 3R2 7U' D 9Dw 5F 2Fw' 2B 7Uw 3F2 9Rw 5Uw2 8L 4R 9B B' 8Fw' 5D' 6Rw' 5Dw2 4D 6Rw2 2R2 2L 7Rw2 7D 2B 8D2 4F 5L2",
            "9F2 2L2 3U2 9Uw' 6Dw 8L 6Rw' 8D' 6B2 9B2 R 5U 6Dw' 6U2 7F 7B' 9R2 6Bw' B2 9Bw 5Dw' 6L2 5L 9Rw' D' 9L 2Bw' 6Dw 8F 2L2",
            "2D' F2 2Dw 7Dw' 6Uw' 8Lw' 6Lw' 8R U2 5L2 8Uw' 7L 5Bw 5D' 8B2 U 4Rw' 7Bw 7Rw2 7F2 4L' 9Fw' 9F2 4F' 3D' 3Bw 8B 9Uw' 2U'",
            "8Dw' L 7R 2Lw2 8Dw2 5R' 3Dw2 2U2 U' 6D' 8D2 2L2 3Uw' R 8D2 3B 9Fw' 3L2 4F2 3U 6B' B' 9F2",
            "5Fw' 7B 3U2 2U 3Fw 4Lw 5Bw 6Rw2 5D 5Lw' 5U' 5Bw 2Lw' 3L 6Fw 2B' 7B' 2Dw 8Lw 6Fw",
            "4Bw 8Dw' 5Bw2 7Uw' L2 8U2 9U' 7Uw2 5B' 5Uw' R' 5Uw 6Fw U2 6Rw 4Fw 4Uw 6Rw 8Dw2 6Bw 2Dw 9Bw 9Lw2 4R2 7Fw' 9B2 2U2 5Bw",
            "4Uw2 3B2 F' 2L 4Fw' 4D' 3L' 4Dw' 3U' 4Lw2 5D' 2B' B2 B 6L' L2 6B2 3D2 5B2 5Fw2 L2 6Rw2 4Uw 8D' 8Lw2",
            "6Uw 2F 2L2 8Rw 8Dw' 3R' 6B 7D2 2B' 19Dw 8R2 U 4Fw' 6U 9F 7Rw' 3L 6R' 3D2 6Lw2 4Rw 5R2",
            "5F2 8U' 4B 9Bw 5F' 6B2 3Dw' 9Fw' 4Uw2 6Fw' 3B2 8Lw2 8R 7D 4Dw2 7Dw 8Lw' 9Rw' 5Uw 3R' 7Bw 3U 6Uw'",
            "4Dw' 8L 8U' 4R2 2Lw' 9Uw2 7Lw2 10Lw 6Lw' 2L2 5Rw' 9Uw 3Dw2 3Uw' 4Fw' 9Bw' 8Fw U2 6F2 7R2 4F 2L 5Fw2 3Bw' 7Uw 3Uw 3Dw 4Lw2 7Bw' 6Lw2 2Dw'",
            "8Bw2 7L 5F 7U2 R' 6Dw 6F2 6Fw2 2Uw2 4L 7Rw' 2R B 5Rw' 5Fw' 9L2 5D2 4L2 2D 2Rw' 4B' 3U' 9U2 4R2 9U 2Bw' 9D",
            "4Lw2 F2 4Dw2 2Fw2 7U' 5U2 5F2 3Lw' 4Bw 6Fw 2B 6Lw 4R 4Dw 5L2 2F 5Bw 9Bw' 5Rw' 4Rw 9L2 5D' 9Dw 8Lw' 3Dw2 4Lw' 8Lw2",
            "8F 9Fw 2R2 6L2 4Rw' 8F' 4Bw 3D' 5U' 6Dw2 2B2 6Dw2 8Rw 2Lw' 7B' 7B' 3D2 3Dw' 4Rw2 6Uw 7L 7Lw2 4U2 B 2U 4Rw2 2F2 6Dw'",
            "2Bw2 U 9L 9R 4F 2B2 3Uw2 8Fw2 4Rw2 4D2 3Bw' 19Uw 8F 9Uw 4Fw 6U D2 2U2 2L' 9Uw' 8F' 4F' 7Uw2 4D'",
            "3B 6L' 6F' 3R' 9Rw 4Dw' F' 4U' 3B 2B' 3Fw2 4Uw2 7Lw2 5B' 7Uw 8D' 9Bw2 2Rw' 8Uw 6Lw' 8Rw2 9Dw2 2Rw 3Dw 3Lw2 4L2 2Bw2 4Fw' 5Uw'",
            "3F2 5Uw2 5L' 4R2 8Uw' 4L2 6Rw 4Fw' 2U2 3Rw 8F2 6F' 2Bw2 2Rw' 8D' 8B2 4Uw2 6L 7D' 7Fw2 6Dw2 3D 3Dw 8Uw2 9Dw' 6U2",
            "7U 7R 7Rw' 2Lw' 9Uw 2U2 3Bw2 5L 4F 9Lw 4Rw' 9R 6Rw2 7Uw' 6D2 9Bw2 5U' 4Dw 3Dw' 3Uw 3Lw' 3Dw 8D' 4Uw2 7D' 3B' 2U'",
            "7Uw 3D 8Dw' 4F' 7Uw 9Bw2 8B 6Rw 3Lw' 2B' 9Fw 9Rw2 3F' 9Fw2 3Dw 2U2 6Uw' 6L2 9Bw 9Uw 4Dw' 7Lw2 7Dw 4D 7Dw 5Bw 4Bw2 8Bw2 6F' 4Fw'",
            "2R' 3Uw 8Bw2 4Lw2 8Lw2 3Bw2 4Uw' 3Dw' 5Bw' 3R' 6Dw' 5F2 9D' 7Fw 6L2 7Rw' 3U' 9L2 3Lw2 9Uw' 3Lw2 9Uw2 7F' 6R' 3Uw2 2L' 3Fw' 7Bw 3R2",
            "5Fw' 6Bw2 2F' 6Uw2 2Dw 2Uw2 9U' 7B 9Fw2 2Lw2 9Dw 7Fw' 2Uw' 5Uw' 6U 3L2 2Lw' 8R' 8Uw' 9R 7Uw 8Fw2 8Rw2 9R2 6Dw 3Dw 6Lw2 4L2 9F2 7Fw2",
            "7F 8Bw 6Rw2 4R' 5L' 6Bw2 8Uw' 7Rw2 2U 5F 4Bw 5Lw2 8Fw' 8F 4B 6F2 8L2 2B2 3Fw2 3R' 4Rw 2Uw' 2L2 2Rw' 6Lw' 8Uw 9Uw 6Fw 6Lw'",
            "6U 3Rw' 7Rw 7Bw' 6Rw' 6Bw' 7Rw 9Fw2 5Lw 6Rw 9Lw2 4Lw2 8Lw2 3Bw' 3B 4B 8Lw' 7Fw2 5F' 5F' 6Fw 5L' 3Uw' 6Lw' 8Uw2 4Dw2 4Fw2 4Dw2",
            "3F2 9R 7Bw 6Rw2 8Fw' 6Uw2 6Bw2 9Uw2 8Lw2 7Bw2 3Dw 4Lw' 6L2 4R' 5Dw2 4L 7Dw' 4D 8Rw' 9Rw 4Uw 3R2 3Dw 2Bw 9Dw' 4Rw' 6Dw 7Lw 8U' 4Uw'",
            "6Rw' 7Lw 3Bw' 8Uw' 4Lw 7Fw' 2Uw 6U' 6Fw' 9B' 5Lw' 9B' 5Bw' 4Uw 5Lw 3Uw' 4Fw' 6Uw 7Uw 9Bw2 7Dw 2Fw' 3Dw' 5Fw2 9Fw' 5Rw2 5Fw2 8Dw2 7Uw'",
            "3Dw' 8Fw' 3L' 3B 8R' 8B' 3Uw2 9Rw2 4Bw 6Fw2 3L 4Dw2 9Rw 4Rw2 2Fw2 4Dw2 9Fw2 8Uw' 8Rw2 5Lw 2Bw2 4B' 5R' 5B' 7F' 5U' 3Dw2 5U' 7Dw'",
            "3Dw2 3Uw' 2Bw2 4Uw2 3Lw2 9Dw' 2Uw2 8Fw2 4Bw2 8Bw2 2Fw' 9Rw2 7Fw' 9Uw2 3Dw2 7Rw' 4Rw 9Lw' 3Uw' 4Lw 8Dw' 8Uw' 5Rw2 3Rw2 5Bw2 6Uw2 4Uw' 5Uw'",
            "3Bw2 3Lw' 9Uw 8Uw2 4Rw2 3Dw2 7Lw 2Rw' 7Fw 6Rw' 6Rw2 4Lw2 5Fw2 6Uw' 5Uw 9Dw 9Fw 7Uw2 8Rw2 7Uw' 7Fw2 2Uw2 7Dw 7Bw' 7Fw2 8Uw2 4Uw' 7Rw' 3Uw2",
            "9Lw 5Lw2 2Uw' 6Lw2 6Fw2 5Bw2 2Dw' 7Fw2 7Fw' 7Uw' 6Uw 5Lw' 7Dw2 6Dw2 4Lw' 5Bw2 7Dw' 4Uw' 5Bw2 4Uw' 4Dw2 6Lw' 4Fw2 2Dw2 9Bw 8Fw2 5Uw' 3Fw2 5Uw'",
            "4Fw 8Lw2 8Rw' 2Dw 6Fw2 4Uw2 5Lw' 3Rw2 8Fw2 8Fw' 3Bw 4Bw' 7Dw' 9Lw' 8Uw2 7Uw 2Uw' 6Uw2 3Uw2 5Dw2 6Bw' 9Dw2 4Lw2 5Uw2 3Dw2 8Dw2 2Bw2 5Uw 8Uw2",
            "9Bw 9Bw 8Rw' 8Fw2 6Fw2 7Bw2 8Fw2 2Fw2 3Uw' 9Lw 3Fw' 5Bw 9Rw2 6Uw' 7Rw 6Dw 3Dw' 2Uw2 7Bw2 2Bw2 7Lw' 9Dw2 7Rw' 9Fw 2Bw2 5Dw' 6Dw2 5Lw' 5Uw2",
            "4Uw2 6Rw' 4Lw' 3Uw2 6Dw 3Uw 7Uw' 3Uw 5Uw2 3Uw2 2Uw2 6Lw2 3Uw' 5Dw' 5Dw' 4Dw2 7Uw2 3Uw' 7Uw 5Uw 5Dw' 8Dw' 6Uw2 5Dw' 5Dw' 4Dw2 4Uw' 3Uw2 6Dw2",
            "2Uw 4Lw' 3Uw' 4Uw' 7Lw' 7Lw2 4Uw' 4Uw2 8Lw 2Uw2 8Lw2 3Uw2 8Lw2 2Uw' 2Uw' 3Uw' 8Lw' 8Lw2 7Lw' 2Uw2 8Lw2 7Lw 2Uw 4Uw 7Lw2 8Lw 2Uw2 8Lw2 7Lw2 8Lw'",
            "4Fw' 7Rw 7Fw2 2Dw' 5Lw' 2Uw 8Uw 6Fw 7Fw2 3Dw 6Lw2 2Fw2 8Fw' 8Fw' 9Bw' 7Rw 6Dw' 3Fw 7Dw2 3Dw2 4Rw' 3Fw2 9Bw2 7Uw 5Lw' 6Uw 2Uw' 9Fw 7Uw'",
            "5Dw 6Rw2 3Dw 5Rw 3Uw2 8Dw' 6Fw2 6Dw' 5Rw 5Fw2 7Dw2 8Fw2 3Uw 7Dw2 2Uw 9Bw 3Fw2 4Dw2 9Bw' 6Dw2 9Rw2 6Dw' 9Uw2 4Fw 8Lw' 4Dw2 3Dw 9Bw2 6Uw'",
            "7Rw2 2Lw 8Bw2 6Fw' 3Bw 7Lw2 4Bw' 2Lw2 4Fw2 4Rw2 9Bw2 8Bw' 5Fw 3Fw 3Rw' 9Dw2 2Lw' 7Uw 4Fw2 5Rw 9Fw' 5Lw' 6Bw2 4Uw 2Fw2 9Uw 8Lw 8Dw2 8Dw2 "]

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
                self.cube.move(scramble)
                self.cube.move(self._get_opposite_sequence(scramble))
                self.assertEqual(self.cube.get_state(), self.clean_state)
            self.cube.reset()