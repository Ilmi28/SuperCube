from abc import ABC, abstractmethod
from copy import deepcopy
import random

class Cube(ABC):
    @property
    @abstractmethod
    def _SIZE_OF_CUBE(self) -> int:
        pass

    def __init__(self):
        self._STATE_OF_CUBE = self._generate_clear_state()
        self._MAX_NUM_LEN = len(str(self._STATE_OF_CUBE[-1][-1][-1]))
        self._SQUARE_LEN = 2 + self._MAX_NUM_LEN * self._SIZE_OF_CUBE + 2 * (self._SIZE_OF_CUBE - 1)
        self._MAX_LAYER = self._SIZE_OF_CUBE

    def _generate_clear_state(self):
        n = 1
        result = []
        for face in range(6):
            result.append([])
            for row in range(self._SIZE_OF_CUBE):
                result[face].append([])
                for col in range(self._SIZE_OF_CUBE):
                    result[face][row].append(n)
                    n += 1
        return result

    def f(self, clockwise=True, layer=1):
        if layer > self._MAX_LAYER or layer <= 0:
            raise Exception("Invalid layer!")
        if clockwise and layer == 1:
            self._f_move_clockwise_external()
        elif clockwise and layer > 1:
            self._f_move_clockwise_internal(layer=layer)
        elif not clockwise and layer == 1:
            self._f_move_anticlockwise_external()
        elif not clockwise and layer > 1:
            self._f_move_anticlockwise_internal(layer=layer)

    def _clockwise_face_move(self, face_index, ORIGINAL_STATE):
        new_face = [[] for _ in range(self._SIZE_OF_CUBE)]
        row = 0
        for i in range(self._SIZE_OF_CUBE):
            for j in range(self._SIZE_OF_CUBE):
                new_face[row].append(ORIGINAL_STATE[face_index][self._SIZE_OF_CUBE - j - 1][i])
            row += 1
        self._STATE_OF_CUBE[face_index] = new_face

    def _anticlockwise_face_move(self, face_index, ORIGINAL_STATE):
        new_face = [[] for _ in range(self._SIZE_OF_CUBE)]
        row = 0
        for i in range(self._SIZE_OF_CUBE):
            for j in range(self._SIZE_OF_CUBE):
                new_face[row].append(ORIGINAL_STATE[face_index][j][self._SIZE_OF_CUBE - i - 1])
            row += 1
        self._STATE_OF_CUBE[face_index] = new_face

    def _f_move_clockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self._clockwise_face_move(2, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[3][i][0] = ORIGINAL_STATE[0][-1][i]
            self._STATE_OF_CUBE[0][-1][i] = ORIGINAL_STATE[1][self._SIZE_OF_CUBE - i - 1][-1]
            self._STATE_OF_CUBE[5][0][i] = ORIGINAL_STATE[3][self._SIZE_OF_CUBE - i - 1][0]
            self._STATE_OF_CUBE[1][i][-1] = ORIGINAL_STATE[5][0][i]

    def _f_move_anticlockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self._anticlockwise_face_move(2, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][-1][i] = ORIGINAL_STATE[3][i][0]
            self._STATE_OF_CUBE[3][i][0] = ORIGINAL_STATE[5][0][self._SIZE_OF_CUBE - i - 1]
            self._STATE_OF_CUBE[5][0][i] = ORIGINAL_STATE[1][i][-1]
            self._STATE_OF_CUBE[1][i][-1] = ORIGINAL_STATE[0][-1][self._SIZE_OF_CUBE - i - 1]

    def _f_move_clockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][-1 - layer][i] = ORIGINAL_STATE[1][self._SIZE_OF_CUBE - i - 1][-1 - layer]
            self._STATE_OF_CUBE[1][i][-1 - layer] = ORIGINAL_STATE[5][layer][i]
            self._STATE_OF_CUBE[3][i][layer] = ORIGINAL_STATE[0][-1 - layer][i]
            self._STATE_OF_CUBE[5][layer][i] = ORIGINAL_STATE[3][self._SIZE_OF_CUBE - i - 1][layer]

    def _f_move_anticlockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][-1 - layer][i] = ORIGINAL_STATE[3][i][layer]
            self._STATE_OF_CUBE[1][i][-1 - layer] = ORIGINAL_STATE[0][-1 - layer][self._SIZE_OF_CUBE - i - 1]
            self._STATE_OF_CUBE[3][i][layer] = ORIGINAL_STATE[5][layer][self._SIZE_OF_CUBE - i - 1]
            self._STATE_OF_CUBE[5][layer][i] = ORIGINAL_STATE[1][i][-1 - layer]

    def u(self, clockwise=True, layer=1):
        if layer > self._MAX_LAYER or layer <= 0:
            raise Exception("Invalid layer!")
        if clockwise and layer == 1:
            self._u_move_clockwise_external()
        elif clockwise and layer > 1:
            self._u_move_clockwise_internal(layer=layer)
        elif not clockwise and layer == 1:
            self._u_move_anticlockwise_external()
        elif not clockwise and layer > 1:
            self._u_move_anticlockwise_internal(layer=layer)

    def _u_move_clockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self._clockwise_face_move(0, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][0][i] = ORIGINAL_STATE[2][0][i]
            self._STATE_OF_CUBE[2][0][i] = ORIGINAL_STATE[3][0][i]
            self._STATE_OF_CUBE[3][0][i] = ORIGINAL_STATE[4][0][i]
            self._STATE_OF_CUBE[4][0][i] = ORIGINAL_STATE[1][0][i]

    def _u_move_anticlockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self._anticlockwise_face_move(0, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][0][i] = ORIGINAL_STATE[4][0][i]
            self._STATE_OF_CUBE[2][0][i] = ORIGINAL_STATE[1][0][i]
            self._STATE_OF_CUBE[3][0][i] = ORIGINAL_STATE[2][0][i]
            self._STATE_OF_CUBE[4][0][i] = ORIGINAL_STATE[3][0][i]

    def _u_move_clockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][layer][i] = ORIGINAL_STATE[2][layer][i]
            self._STATE_OF_CUBE[2][layer][i] = ORIGINAL_STATE[3][layer][i]
            self._STATE_OF_CUBE[3][layer][i] = ORIGINAL_STATE[4][layer][i]
            self._STATE_OF_CUBE[4][layer][i] = ORIGINAL_STATE[1][layer][i]

    def _u_move_anticlockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][layer][i] = ORIGINAL_STATE[4][layer][i]
            self._STATE_OF_CUBE[2][layer][i] = ORIGINAL_STATE[1][layer][i]
            self._STATE_OF_CUBE[3][layer][i] = ORIGINAL_STATE[2][layer][i]
            self._STATE_OF_CUBE[4][layer][i] = ORIGINAL_STATE[3][layer][i]

    def b(self, clockwise=True, layer=1):
        if layer > self._MAX_LAYER or layer <= 0:
            raise Exception("Invalid layer!")
        if clockwise and layer == 1:
            self._b_move_clockwise_external()
        elif clockwise and layer > 1:
            self._b_move_clockwise_internal(layer=layer)
        elif not clockwise and layer == 1:
            self._b_move_anticlockwise_external()
        elif not clockwise and layer > 1:
            self._b_move_anticlockwise_internal(layer=layer)

    def _b_move_clockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self._clockwise_face_move(4, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][0][i] = ORIGINAL_STATE[3][i][-1]
            self._STATE_OF_CUBE[1][i][0] = ORIGINAL_STATE[0][0][self._SIZE_OF_CUBE - i - 1]
            self._STATE_OF_CUBE[3][i][-1] = ORIGINAL_STATE[5][-1][self._SIZE_OF_CUBE - i - 1]
            self._STATE_OF_CUBE[5][-1][i] = ORIGINAL_STATE[1][i][0]

    def _b_move_anticlockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self._anticlockwise_face_move(4, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][0][i] = ORIGINAL_STATE[1][self._SIZE_OF_CUBE - i - 1][0]
            self._STATE_OF_CUBE[1][i][0] = ORIGINAL_STATE[5][-1][i]
            self._STATE_OF_CUBE[3][i][-1] = ORIGINAL_STATE[0][0][i]
            self._STATE_OF_CUBE[5][-1][i] = ORIGINAL_STATE[3][self._SIZE_OF_CUBE - i - 1][-1]

    def _b_move_clockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][layer][i] = ORIGINAL_STATE[3][i][-1 - layer]
            self._STATE_OF_CUBE[1][i][layer] = ORIGINAL_STATE[0][layer][self._SIZE_OF_CUBE - i - 1]
            self._STATE_OF_CUBE[3][i][-1 - layer] = ORIGINAL_STATE[5][-1 - layer][self._SIZE_OF_CUBE - i - 1]
            self._STATE_OF_CUBE[5][-1 - layer][i] = ORIGINAL_STATE[1][i][layer]

    def _b_move_anticlockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][layer][i] = ORIGINAL_STATE[1][self._SIZE_OF_CUBE - i - 1][layer]
            self._STATE_OF_CUBE[1][i][layer] = ORIGINAL_STATE[5][layer][i]
            self._STATE_OF_CUBE[3][i][-1 - layer] = ORIGINAL_STATE[0][layer][i]
            self._STATE_OF_CUBE[5][-1 - layer][i] = ORIGINAL_STATE[3][self._SIZE_OF_CUBE - i - 1][-1 - layer]

    def r(self, clockwise=True, layer=1):
        if layer > self._MAX_LAYER or layer <= 0:
            raise Exception("Invalid layer!")
        if clockwise and layer == 1:
            self._r_move_clockwise_external()
        elif clockwise and layer > 1:
            self._r_move_clockwise_internal(layer=layer)
        elif not clockwise and layer == 1:
            self._r_move_anticlockwise_external()
        elif not clockwise and layer > 1:
            self._r_move_anticlockwise_internal(layer=layer)

    def _r_move_clockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self._clockwise_face_move(3, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][-1] = ORIGINAL_STATE[2][i][-1]
            self._STATE_OF_CUBE[2][i][-1] = ORIGINAL_STATE[5][i][-1]
            self._STATE_OF_CUBE[4][i][0] = ORIGINAL_STATE[0][self._SIZE_OF_CUBE - i - 1][-1]
            self._STATE_OF_CUBE[5][i][-1] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][0]

    def _r_move_anticlockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self._anticlockwise_face_move(3, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][-1] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][0]
            self._STATE_OF_CUBE[2][i][-1] = ORIGINAL_STATE[0][i][-1]
            self._STATE_OF_CUBE[4][i][0] = ORIGINAL_STATE[5][self._SIZE_OF_CUBE - i - 1][-1]
            self._STATE_OF_CUBE[5][i][-1] = ORIGINAL_STATE[2][i][-1]

    def _r_move_clockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][-1 - layer] = ORIGINAL_STATE[2][i][-1 - layer]
            self._STATE_OF_CUBE[2][i][-1 - layer] = ORIGINAL_STATE[5][i][-1 - layer]
            self._STATE_OF_CUBE[4][i][layer] = ORIGINAL_STATE[0][self._SIZE_OF_CUBE - i - 1][-1 - layer]
            self._STATE_OF_CUBE[5][i][-1 - layer] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][layer]

    def _r_move_anticlockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][-1 - layer] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][layer]
            self._STATE_OF_CUBE[2][i][-1 - layer] = ORIGINAL_STATE[0][i][-1 - layer]
            self._STATE_OF_CUBE[4][i][layer] = ORIGINAL_STATE[5][self._SIZE_OF_CUBE - i - 1][-1 - layer]
            self._STATE_OF_CUBE[5][i][-1 - layer] = ORIGINAL_STATE[2][i][-1 - layer]

    def l(self, clockwise=True, layer=1):
        if layer > self._MAX_LAYER or layer <= 0:
            raise Exception("Invalid layer!")
        if clockwise and layer == 1:
            self._l_move_clockwise_external()
        elif clockwise and layer > 1:
            self._l_move_clockwise_internal(layer=layer)
        elif not clockwise and layer == 1:
            self._l_move_anticlockwise_external()
        elif not clockwise and layer > 1:
            self._l_move_anticlockwise_internal(layer=layer)

    def _l_move_clockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self._clockwise_face_move(1, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][0] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][-1]
            self._STATE_OF_CUBE[2][i][0] = ORIGINAL_STATE[0][i][0]
            self._STATE_OF_CUBE[4][i][-1] = ORIGINAL_STATE[5][self._SIZE_OF_CUBE - i - 1][0]
            self._STATE_OF_CUBE[5][i][0] = ORIGINAL_STATE[2][i][0]

    def _l_move_anticlockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self._anticlockwise_face_move(1, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][0] = ORIGINAL_STATE[2][i][0]
            self._STATE_OF_CUBE[2][i][0] = ORIGINAL_STATE[5][i][0]
            self._STATE_OF_CUBE[4][i][-1] = ORIGINAL_STATE[0][self._SIZE_OF_CUBE - i - 1][0]
            self._STATE_OF_CUBE[5][i][0] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][-1]

    def _l_move_clockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][layer] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][-1 - layer]
            self._STATE_OF_CUBE[2][i][layer] = ORIGINAL_STATE[0][i][layer]
            self._STATE_OF_CUBE[4][i][-1 - layer] = ORIGINAL_STATE[5][self._SIZE_OF_CUBE - i - 1][layer]
            self._STATE_OF_CUBE[5][i][layer] = ORIGINAL_STATE[2][i][layer]

    def _l_move_anticlockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][layer] = ORIGINAL_STATE[2][i][layer]
            self._STATE_OF_CUBE[2][i][layer] = ORIGINAL_STATE[5][i][layer]
            self._STATE_OF_CUBE[4][i][-1 - layer] = ORIGINAL_STATE[0][self._SIZE_OF_CUBE - i - 1][layer]
            self._STATE_OF_CUBE[5][i][layer] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][-1 - layer]

    def d(self, clockwise=True, layer=1):
        if layer > self._MAX_LAYER or layer <= 0:
            raise Exception("Invalid layer!")
        if clockwise and layer == 1:
            self._d_move_clockwise_external()
        elif clockwise and layer > 1:
            self._d_move_clockwise_internal(layer=layer)
        elif not clockwise and layer == 1:
            self._d_move_anticlockwise_external()
        elif not clockwise and layer > 1:
            self._d_move_anticlockwise_internal(layer=layer)

    def _d_move_clockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self._clockwise_face_move(5, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][-1][i] = ORIGINAL_STATE[4][-1][i]
            self._STATE_OF_CUBE[2][-1][i] = ORIGINAL_STATE[1][-1][i]
            self._STATE_OF_CUBE[3][-1][i] = ORIGINAL_STATE[2][-1][i]
            self._STATE_OF_CUBE[4][-1][i] = ORIGINAL_STATE[3][-1][i]

    def _d_move_anticlockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self._anticlockwise_face_move(5, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][-1][i] = ORIGINAL_STATE[2][-1][i]
            self._STATE_OF_CUBE[2][-1][i] = ORIGINAL_STATE[3][-1][i]
            self._STATE_OF_CUBE[3][-1][i] = ORIGINAL_STATE[4][-1][i]
            self._STATE_OF_CUBE[4][-1][i] = ORIGINAL_STATE[1][-1][i]

    def _d_move_clockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][-1 - layer][i] = ORIGINAL_STATE[4][-1 - layer][i]
            self._STATE_OF_CUBE[2][-1 - layer][i] = ORIGINAL_STATE[1][-1 - layer][i]
            self._STATE_OF_CUBE[3][-1 - layer][i] = ORIGINAL_STATE[2][-1 - layer][i]
            self._STATE_OF_CUBE[4][-1 - layer][i] = ORIGINAL_STATE[3][-1 - layer][i]

    def _d_move_anticlockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][-1 - layer][i] = ORIGINAL_STATE[2][-1 - layer][i]
            self._STATE_OF_CUBE[2][-1 - layer][i] = ORIGINAL_STATE[3][-1 - layer][i]
            self._STATE_OF_CUBE[3][-1 - layer][i] = ORIGINAL_STATE[4][-1 - layer][i]
            self._STATE_OF_CUBE[4][-1 - layer][i] = ORIGINAL_STATE[1][-1 - layer][i]

    def show(self, colors=False):
        if colors:
            self._show_with_colors()
        else:
            self._show_without_colors()

    # we acquire amount of spaces that should be placed before number, by subtracting length of current element from
    # length of maximum element(for better visual look)
    def _print_spaces(self, cube_element):
        return (self._MAX_NUM_LEN - len(str(cube_element))) * " "

    def _generate_top_face(self):
        print((self._SQUARE_LEN + 1) * " " + "┌" + "─" * self._SQUARE_LEN + "┐")
        for i in range(self._SIZE_OF_CUBE):
            print((self._SQUARE_LEN + 1) * " " + "│ " +
                  self._print_spaces(self._STATE_OF_CUBE[0][i][0]) +
                  str(self._STATE_OF_CUBE[0][i][0]) + "  ", end="")
            for j in range(self._SIZE_OF_CUBE - 2):
                print(self._print_spaces(self._STATE_OF_CUBE[0][i][j + 1]) +
                      str(self._STATE_OF_CUBE[0][i][j + 1]) + "  ", end="")
            print(self._print_spaces(self._STATE_OF_CUBE[0][i][-1]) +
                  str(self._STATE_OF_CUBE[0][i][-1]) + " │")

    def _generate_middle_faces(self):
        print("┌" + self._SQUARE_LEN * "─" + "┼" + self._SQUARE_LEN * "─" + "┼" + self._SQUARE_LEN * "─" + "┬" +
              self._SQUARE_LEN * "─" + "┐")
        for i in range(self._SIZE_OF_CUBE):
            print("│ ", end="")
            for j in range(4):
                for k in range(self._SIZE_OF_CUBE - 1):
                    print(self._print_spaces(self._STATE_OF_CUBE[j + 1][i][k]) +
                          str(self._STATE_OF_CUBE[j+1][i][k]) + "  ", end="")
                print(self._print_spaces(self._STATE_OF_CUBE[j + 1][i][-1]) +
                      str(self._STATE_OF_CUBE[j+1][i][-1]) + " │ ", end="")
            print("")
        print("└" + "─" * self._SQUARE_LEN + "┼" + "─" * self._SQUARE_LEN + "┼" + "─" * self._SQUARE_LEN + "┴" +
              "─" * self._SQUARE_LEN + "┘")

    def _generate_bottom_face(self):
        for i in range(self._SIZE_OF_CUBE):
            print(" " * (self._SQUARE_LEN + 1) + "│ " + self._print_spaces(self._STATE_OF_CUBE[-1][i][0]) +
                  str(self._STATE_OF_CUBE[-1][i][0]) + "  ", end="")
            for j in range(self._SIZE_OF_CUBE - 2):
                print(self._print_spaces(self._STATE_OF_CUBE[-1][i][j + 1]) +
                      str(self._STATE_OF_CUBE[-1][i][j + 1]) + "  ", end="")
            print(self._print_spaces(self._STATE_OF_CUBE[-1][i][-1]) +
                  str(self._STATE_OF_CUBE[-1][i][-1]) + " │")
        print(" " * (self._SQUARE_LEN + 1) + "└" + "─" * self._SQUARE_LEN + "┘")

    def _show_without_colors(self):
        self._generate_top_face()
        self._generate_middle_faces()
        self._generate_bottom_face()

    def _show_with_colors(self):
        color_config = {
            "top": "🟪",
            "left": "🟧",
            "front": "🟩",
            "right": "🟥",
            "rear": "🟦",
            "bottom": "🟨"
        }
        for i in range(self._SIZE_OF_CUBE):
            for j in range(self._SIZE_OF_CUBE):
                print("⬛", end="")
            print(" ", end="")
            for j in range(self._SIZE_OF_CUBE):
                element = self._STATE_OF_CUBE[0][i][j]
                face = self._get_face_by_element(self._STATE_OF_CUBE[0][i][j])
                print(color_config[face], end="")
            print("")
        print("")
        for i in range(self._SIZE_OF_CUBE):
            for j in range(1, 5):
                for k in range(self._SIZE_OF_CUBE):
                    face = self._get_face_by_element(self._STATE_OF_CUBE[j][i][k])
                    print(color_config[face], end="")
                print(" ", end="")
            print("")
        print("")
        for i in range(self._SIZE_OF_CUBE):
            for j in range(self._SIZE_OF_CUBE):
                print("⬛", end="")
            print(" ", end="")
            for j in range(self._SIZE_OF_CUBE):
                face = self._get_face_by_element(self._STATE_OF_CUBE[5][i][j])
                print(color_config[face], end="")
            print("")
        print("")
        print("")

    def _get_face_by_element(self, element):
        square = self._SIZE_OF_CUBE * self._SIZE_OF_CUBE
        if 0 < element <= square:
            return "top"
        elif square < element <= square * 2:
            return "left"
        elif square * 2 < element <= square * 3:
            return "front"
        elif square * 3 < element <= square * 4:
            return "right"
        elif square * 4 < element <= square * 5:
            return "rear"
        elif square * 5 < element <= square * 6:
            return "bottom"


    def move(self, moves):
        self._match_moves(moves)

    def _match_moves(self, moves):
        moves = moves.strip().split(" ")
        moves_dict = {
            "R": self.r,
            "L": self.l,
            "F": self.f,
            "U": self.u,
            "B": self.b,
            "D": self.d
        }
        for move in moves:
            # U2, F2, ...
            if len(move) == 2 and move[-1] == "2" and move[0] in moves_dict:
                moves_dict[move[0]]()
                moves_dict[move[0]]()
            # U', F', ...
            elif len(move) == 2 and move[-1] == "'" and move[0] in moves_dict:
                moves_dict[move[0]](clockwise=False)
            # U, F, ...
            elif len(move) == 1 and move in moves_dict:
                moves_dict[move]()
            # 2U, 3F, ...
            elif len(move) == 2 and move[0].isdigit() and move[-1] in moves_dict:
                moves_dict[move[1]](layer=int(move[0]))
            # 2U', 3F', ...
            elif len(move) == 3 and move[0].isdigit() and move[-1] == "'" and move[1] in moves_dict:
                moves_dict[move[1]](clockwise=False, layer=int(move[0]))
            # 2U2, 3F2, ...
            elif len(move) == 3 and move[0].isdigit() and move[-1] == "2" and move[1] in moves_dict:
                moves_dict[move[1]](layer=int(move[0]))
                moves_dict[move[1]](layer=int(move[0]))
            # Uw, Fw, ...
            elif len(move) == 2 and move[-1] == "w" and move[0] in moves_dict:
                moves_dict[move[0]](layer=1)
                moves_dict[move[0]](layer=2)
            # Uw', Fw', ...
            elif len(move) == 3 and move[-2] == "w" and move[-1] == "'" and move[0] in moves_dict:
                moves_dict[move[0]](clockwise=False, layer=1)
                moves_dict[move[0]](clockwise=False, layer=2)
            # Uw2, Fw2, ...
            elif len(move) == 3 and move[-2] == "w" and move[-1] == "2" and move[0] in moves_dict:
                moves_dict[move[0]](clockwise=False, layer=1)
                moves_dict[move[0]](clockwise=False, layer=2)
                moves_dict[move[0]](clockwise=False, layer=1)
                moves_dict[move[0]](clockwise=False, layer=2)
            # 2Uw, 3Fw, ...
            elif len(move) == 3 and move[0].isdigit() and move[-1] == "w" and move[1] in moves_dict:
                for i in range(int(move[0])):
                    moves_dict[move[1]](layer=i+1)
            # 2Uw', 3Fw', ...
            elif len(move) == 4 and move[0].isdigit() and move[-2] == "w" and move[-1] == "'" and move[1] in moves_dict:
                for i in range(int(move[0])):
                    moves_dict[move[1]](clockwise=False, layer=i+1)
            # 2Uw2, 3Fw2, ...
            elif len(move) == 4 and move[0].isdigit() and move[-2] == "w" and move[-1] == "2" and move[1] in moves_dict:
                for i in range(int(move[0])):
                    moves_dict[move[1]](layer=i+1)
                    moves_dict[move[1]](layer=i+1)
            else:
                raise Exception("Invalid move!")

    def scramble(self, number_of_moves=30):
        scramble = ""
        moves = ["R", "L", "U", "D", "B", "F"]
        basic_moves = deepcopy(moves)
        for move in basic_moves:
            for i in range(1, self._SIZE_OF_CUBE // 2):
                moves.append(str(i + 1) + move + "w")
                moves.append(str(i + 1) + move)
        for i in range(number_of_moves):
            random_move = random.choice(moves)
            move_instance = random.randint(1, 3)
            if move_instance == 1:
                scramble += random_move + " "
            elif move_instance == 2:
                scramble += random_move + "' "
            elif move_instance == 3:
                scramble += random_move + "2 "
            else:
                raise Exception("Invalid instance of move!")
        self._match_moves(scramble)
        return scramble

    def get_state(self):
        return self._STATE_OF_CUBE

    def set_state(self, state):
        self._STATE_OF_CUBE = state

