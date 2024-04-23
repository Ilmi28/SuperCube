from copy import deepcopy
import random
from supercube.RubiksCube import RubiksCube
from supercube.PocketCube import PocketCube
from supercube.NCube import NCube

cube = RubiksCube()
cube.show(colors=True)
cube.define_state("BYYBWGORORWBOOBGYYYWWRGGGOYBOGWRBRGWOGWOBWRYWRYBRYROBG")
print(cube.solve())