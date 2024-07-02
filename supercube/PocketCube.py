from supercube.cube import Cube
from supercube.kociemba_2x2 import solver
import os

class PocketCube(Cube):
    _SIZE_OF_CUBE = 2

    def solve(self):
        kociemba_state = ""

        for i in range(2):
            for j in range(2):
                kociemba_state += self.__get_face_by_element(self._STATE_OF_CUBE[0][i][j])
        for i in range(2):
            for j in range(2):
                kociemba_state += self.__get_face_by_element(self._STATE_OF_CUBE[3][i][j])
        for i in range(2):
            for j in range(2):
                kociemba_state += self.__get_face_by_element(self._STATE_OF_CUBE[2][i][j])
        for i in range(2):
            for j in range(2):
                kociemba_state += self.__get_face_by_element(self._STATE_OF_CUBE[5][i][j])
        for i in range(2):
            for j in range(2):
                kociemba_state += self.__get_face_by_element(self._STATE_OF_CUBE[1][i][j])
        for i in range(2):
            for j in range(2):
                kociemba_state += self.__get_face_by_element(self._STATE_OF_CUBE[4][i][j])
        kociemba_moves = solver.solve(kociemba_state)
        self.move(kociemba_moves)
        return kociemba_moves