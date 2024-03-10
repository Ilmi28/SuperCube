import supercube.rubikscube as rubik

cube = rubik.RubiksCube()
cube.move("F B L' U' 2R 2U 2F D D' R R' 2U 2B U B B' 2R 2F 2B 2D U L B' B 2B 2R 2U B' L' F")
cube.show()