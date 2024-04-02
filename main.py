from supercube.RubiksCube import RubiksCube
from supercube.PocketCube import PocketCube

cube = PocketCube()
cube.show(colors=True)
cube.scramble(number_of_moves=50)
cube.show()
print(cube.solve())
cube.show(colors=True)
