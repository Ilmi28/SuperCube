from supercube.cube import Cube


class NCube(Cube):

    def _SIZE_OF_CUBE(self) -> int:
        pass

    def __init__(self, size_of_cube):
        self._SIZE_OF_CUBE = size_of_cube
        super().__init__()