from abc import ABC, abstractmethod
from copy import deepcopy
import random
import re
import pyvista as pv


class Cube(ABC):
    @property
    @abstractmethod
    def _SIZE_OF_CUBE(self) -> int:
        pass

    @abstractmethod
    def solve(self):
        pass

    def __init__(self):
        self._UP_ELEMENTS = []
        self._LEFT_ELEMENTS = []
        self._FRONT_ELEMENTS = []
        self._RIGHT_ELEMENTS = []
        self._BACK_ELEMENTS = []
        self._DOWN_ELEMENTS = []
        self._STATE_OF_CUBE = self.__generate_clear_state()
        self._MAX_NUM_LEN = len(str(self._STATE_OF_CUBE[-1][-1][-1]))
        self._SQUARE_LEN = 2 + self._MAX_NUM_LEN * self._SIZE_OF_CUBE + 2 * (self._SIZE_OF_CUBE - 1)
        self._MAX_LAYER = self._SIZE_OF_CUBE


    def __generate_clear_state(self):
        n = 1
        result = []
        total_number_of_elements = 6 * self._SIZE_OF_CUBE ** 2
        for face in range(6):
            result.append([])
            for row in range(self._SIZE_OF_CUBE):
                result[face].append([])
                for col in range(self._SIZE_OF_CUBE):
                    result[face][row].append(n)
                    n += 1
        sq = self._SIZE_OF_CUBE**2
        for element in range(1, total_number_of_elements+1):
            if element in range(1, sq+1):
                self._UP_ELEMENTS.append(element)
            elif element in range(sq+1, sq*2+1):
                self._LEFT_ELEMENTS.append(element)
            elif element in range(sq*2+1, sq*3+1):
                self._FRONT_ELEMENTS.append(element)
            elif element in range(sq*3+1, sq*4+1):
                self._RIGHT_ELEMENTS.append(element)
            elif element in range(sq*4+1, sq*5+1):
                self._BACK_ELEMENTS.append(element)
            elif element in range(sq*5+1, sq*6+1):
                self._DOWN_ELEMENTS.append(element)

        return result

    def f(self, clockwise=True, layer=1):
        if layer > self._MAX_LAYER or layer <= 0:
            raise Exception("Invalid layer!")
        if clockwise and layer == 1:
            self.__f_move_clockwise_external()
        elif clockwise and layer == self._SIZE_OF_CUBE:
            self.__b_move_anticlockwise_external()
        elif not clockwise and layer == self._SIZE_OF_CUBE:
            self.__b_move_clockwise_external()
        elif clockwise and layer > 1:
            self.__f_move_clockwise_internal(layer=layer)
        elif not clockwise and layer == 1:
            self.__f_move_anticlockwise_external()
        elif not clockwise and layer > 1:
            self.__f_move_anticlockwise_internal(layer=layer)

    def __clockwise_face_move(self, face_index, ORIGINAL_STATE):
        new_face = [[] for _ in range(self._SIZE_OF_CUBE)]
        row = 0
        for i in range(self._SIZE_OF_CUBE):
            for j in range(self._SIZE_OF_CUBE):
                new_face[row].append(ORIGINAL_STATE[face_index][self._SIZE_OF_CUBE - j - 1][i])
            row += 1
        self._STATE_OF_CUBE[face_index] = new_face

    def __anticlockwise_face_move(self, face_index, ORIGINAL_STATE):
        new_face = [[] for _ in range(self._SIZE_OF_CUBE)]
        row = 0
        for i in range(self._SIZE_OF_CUBE):
            for j in range(self._SIZE_OF_CUBE):
                new_face[row].append(ORIGINAL_STATE[face_index][j][self._SIZE_OF_CUBE - i - 1])
            row += 1
        self._STATE_OF_CUBE[face_index] = new_face

    def __f_move_clockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self.__clockwise_face_move(2, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[3][i][0] = ORIGINAL_STATE[0][-1][i]
            self._STATE_OF_CUBE[0][-1][i] = ORIGINAL_STATE[1][self._SIZE_OF_CUBE - i - 1][-1]
            self._STATE_OF_CUBE[5][0][i] = ORIGINAL_STATE[3][self._SIZE_OF_CUBE - i - 1][0]
            self._STATE_OF_CUBE[1][i][-1] = ORIGINAL_STATE[5][0][i]

    def __f_move_anticlockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self.__anticlockwise_face_move(2, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][-1][i] = ORIGINAL_STATE[3][i][0]
            self._STATE_OF_CUBE[3][i][0] = ORIGINAL_STATE[5][0][self._SIZE_OF_CUBE - i - 1]
            self._STATE_OF_CUBE[5][0][i] = ORIGINAL_STATE[1][i][-1]
            self._STATE_OF_CUBE[1][i][-1] = ORIGINAL_STATE[0][-1][self._SIZE_OF_CUBE - i - 1]

    def __f_move_clockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][-1 - layer][i] = ORIGINAL_STATE[1][self._SIZE_OF_CUBE - i - 1][-1 - layer]
            self._STATE_OF_CUBE[1][i][-1 - layer] = ORIGINAL_STATE[5][layer][i]
            self._STATE_OF_CUBE[3][i][layer] = ORIGINAL_STATE[0][-1 - layer][i]
            self._STATE_OF_CUBE[5][layer][i] = ORIGINAL_STATE[3][self._SIZE_OF_CUBE - i - 1][layer]

    def __f_move_anticlockwise_internal(self, layer):
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
            self.__u_move_clockwise_external()
        elif clockwise and layer == self._SIZE_OF_CUBE:
            self.__d_move_anticlockwise_external()
        elif not clockwise and layer == self._SIZE_OF_CUBE:
            self.__d_move_clockwise_external()
        elif clockwise and layer > 1:
            self.__u_move_clockwise_internal(layer=layer)
        elif not clockwise and layer == 1:
            self.__u_move_anticlockwise_external()
        elif not clockwise and layer > 1:
            self.__u_move_anticlockwise_internal(layer=layer)

    def __u_move_clockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self.__clockwise_face_move(0, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][0][i] = ORIGINAL_STATE[2][0][i]
            self._STATE_OF_CUBE[2][0][i] = ORIGINAL_STATE[3][0][i]
            self._STATE_OF_CUBE[3][0][i] = ORIGINAL_STATE[4][0][i]
            self._STATE_OF_CUBE[4][0][i] = ORIGINAL_STATE[1][0][i]

    def __u_move_anticlockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self.__anticlockwise_face_move(0, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][0][i] = ORIGINAL_STATE[4][0][i]
            self._STATE_OF_CUBE[2][0][i] = ORIGINAL_STATE[1][0][i]
            self._STATE_OF_CUBE[3][0][i] = ORIGINAL_STATE[2][0][i]
            self._STATE_OF_CUBE[4][0][i] = ORIGINAL_STATE[3][0][i]

    def __u_move_clockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][layer][i] = ORIGINAL_STATE[2][layer][i]
            self._STATE_OF_CUBE[2][layer][i] = ORIGINAL_STATE[3][layer][i]
            self._STATE_OF_CUBE[3][layer][i] = ORIGINAL_STATE[4][layer][i]
            self._STATE_OF_CUBE[4][layer][i] = ORIGINAL_STATE[1][layer][i]

    def __u_move_anticlockwise_internal(self, layer):
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
            self.__b_move_clockwise_external()
        elif clockwise and layer == self._SIZE_OF_CUBE:
            self.__f_move_anticlockwise_external()
        elif not clockwise and layer == self._SIZE_OF_CUBE:
            self.__f_move_clockwise_external()
        elif clockwise and layer > 1:
            self.__b_move_clockwise_internal(layer=layer)
        elif not clockwise and layer == 1:
            self.__b_move_anticlockwise_external()
        elif not clockwise and layer > 1:
            self.__b_move_anticlockwise_internal(layer=layer)

    def __b_move_clockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self.__clockwise_face_move(4, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][0][i] = ORIGINAL_STATE[3][i][-1]
            self._STATE_OF_CUBE[1][i][0] = ORIGINAL_STATE[0][0][self._SIZE_OF_CUBE - i - 1]
            self._STATE_OF_CUBE[3][i][-1] = ORIGINAL_STATE[5][-1][self._SIZE_OF_CUBE - i - 1]
            self._STATE_OF_CUBE[5][-1][i] = ORIGINAL_STATE[1][i][0]

    def __b_move_anticlockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self.__anticlockwise_face_move(4, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][0][i] = ORIGINAL_STATE[1][self._SIZE_OF_CUBE - i - 1][0]
            self._STATE_OF_CUBE[1][i][0] = ORIGINAL_STATE[5][-1][i]
            self._STATE_OF_CUBE[3][i][-1] = ORIGINAL_STATE[0][0][i]
            self._STATE_OF_CUBE[5][-1][i] = ORIGINAL_STATE[3][self._SIZE_OF_CUBE - i - 1][-1]

    def __b_move_clockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][layer][i] = ORIGINAL_STATE[3][i][-1 - layer]
            self._STATE_OF_CUBE[1][i][layer] = ORIGINAL_STATE[0][layer][self._SIZE_OF_CUBE - i - 1]
            self._STATE_OF_CUBE[3][i][-1 - layer] = ORIGINAL_STATE[5][-1 - layer][self._SIZE_OF_CUBE - i - 1]
            self._STATE_OF_CUBE[5][-1 - layer][i] = ORIGINAL_STATE[1][i][layer]

    def __b_move_anticlockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][layer][i] = ORIGINAL_STATE[1][self._SIZE_OF_CUBE - i - 1][layer]
            self._STATE_OF_CUBE[1][i][layer] = ORIGINAL_STATE[5][-1 - layer][i]
            self._STATE_OF_CUBE[3][i][-1 - layer] = ORIGINAL_STATE[0][layer][i]
            self._STATE_OF_CUBE[5][-1 - layer][i] = ORIGINAL_STATE[3][self._SIZE_OF_CUBE - i - 1][-1 - layer]

    def r(self, clockwise=True, layer=1):
        if layer > self._MAX_LAYER or layer <= 0:
            raise Exception("Invalid layer!")
        if clockwise and layer == 1:
            self.__r_move_clockwise_external()
        elif clockwise and layer == self._SIZE_OF_CUBE:
            self.__l_move_anticlockwise_external()
        elif not clockwise and layer == self._SIZE_OF_CUBE:
            self.__l_move_clockwise_external()
        elif clockwise and layer > 1:
            self.__r_move_clockwise_internal(layer=layer)
        elif not clockwise and layer == 1:
            self.__r_move_anticlockwise_external()
        elif not clockwise and layer > 1:
            self.__r_move_anticlockwise_internal(layer=layer)

    def __r_move_clockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self.__clockwise_face_move(3, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][-1] = ORIGINAL_STATE[2][i][-1]
            self._STATE_OF_CUBE[2][i][-1] = ORIGINAL_STATE[5][i][-1]
            self._STATE_OF_CUBE[4][i][0] = ORIGINAL_STATE[0][self._SIZE_OF_CUBE - i - 1][-1]
            self._STATE_OF_CUBE[5][i][-1] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][0]

    def __r_move_anticlockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self.__anticlockwise_face_move(3, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][-1] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][0]
            self._STATE_OF_CUBE[2][i][-1] = ORIGINAL_STATE[0][i][-1]
            self._STATE_OF_CUBE[4][i][0] = ORIGINAL_STATE[5][self._SIZE_OF_CUBE - i - 1][-1]
            self._STATE_OF_CUBE[5][i][-1] = ORIGINAL_STATE[2][i][-1]

    def __r_move_clockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][-1 - layer] = ORIGINAL_STATE[2][i][-1 - layer]
            self._STATE_OF_CUBE[2][i][-1 - layer] = ORIGINAL_STATE[5][i][-1 - layer]
            self._STATE_OF_CUBE[4][i][layer] = ORIGINAL_STATE[0][self._SIZE_OF_CUBE - i - 1][-1 - layer]
            self._STATE_OF_CUBE[5][i][-1 - layer] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][layer]

    def __r_move_anticlockwise_internal(self, layer):
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
            self.__l_move_clockwise_external()
        elif clockwise and layer == self._SIZE_OF_CUBE:
            self.__r_move_anticlockwise_external()
        elif not clockwise and layer == self._SIZE_OF_CUBE:
            self.__r_move_clockwise_external()
        elif clockwise and layer > 1:
            self.__l_move_clockwise_internal(layer=layer)
        elif not clockwise and layer == 1:
            self.__l_move_anticlockwise_external()
        elif not clockwise and layer > 1:
            self.__l_move_anticlockwise_internal(layer=layer)

    def __l_move_clockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self.__clockwise_face_move(1, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][0] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][-1]
            self._STATE_OF_CUBE[2][i][0] = ORIGINAL_STATE[0][i][0]
            self._STATE_OF_CUBE[4][i][-1] = ORIGINAL_STATE[5][self._SIZE_OF_CUBE - i - 1][0]
            self._STATE_OF_CUBE[5][i][0] = ORIGINAL_STATE[2][i][0]

    def __l_move_anticlockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self.__anticlockwise_face_move(1, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][0] = ORIGINAL_STATE[2][i][0]
            self._STATE_OF_CUBE[2][i][0] = ORIGINAL_STATE[5][i][0]
            self._STATE_OF_CUBE[4][i][-1] = ORIGINAL_STATE[0][self._SIZE_OF_CUBE - i - 1][0]
            self._STATE_OF_CUBE[5][i][0] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][-1]

    def __l_move_clockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[0][i][layer] = ORIGINAL_STATE[4][self._SIZE_OF_CUBE - i - 1][-1 - layer]
            self._STATE_OF_CUBE[2][i][layer] = ORIGINAL_STATE[0][i][layer]
            self._STATE_OF_CUBE[4][i][-1 - layer] = ORIGINAL_STATE[5][self._SIZE_OF_CUBE - i - 1][layer]
            self._STATE_OF_CUBE[5][i][layer] = ORIGINAL_STATE[2][i][layer]

    def __l_move_anticlockwise_internal(self, layer):
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
            self.__d_move_clockwise_external()
        elif clockwise and layer == self._SIZE_OF_CUBE:
            self.__u_move_anticlockwise_external()
        elif not clockwise and layer == self._SIZE_OF_CUBE:
            self.__u_move_clockwise_external()
        elif clockwise and layer > 1:
            self.__d_move_clockwise_internal(layer=layer)
        elif not clockwise and layer == 1:
            self.__d_move_anticlockwise_external()
        elif not clockwise and layer > 1:
            self.__d_move_anticlockwise_internal(layer=layer)

    def __d_move_clockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self.__clockwise_face_move(5, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][-1][i] = ORIGINAL_STATE[4][-1][i]
            self._STATE_OF_CUBE[2][-1][i] = ORIGINAL_STATE[1][-1][i]
            self._STATE_OF_CUBE[3][-1][i] = ORIGINAL_STATE[2][-1][i]
            self._STATE_OF_CUBE[4][-1][i] = ORIGINAL_STATE[3][-1][i]

    def __d_move_anticlockwise_external(self):
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        self.__anticlockwise_face_move(5, ORIGINAL_STATE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][-1][i] = ORIGINAL_STATE[2][-1][i]
            self._STATE_OF_CUBE[2][-1][i] = ORIGINAL_STATE[3][-1][i]
            self._STATE_OF_CUBE[3][-1][i] = ORIGINAL_STATE[4][-1][i]
            self._STATE_OF_CUBE[4][-1][i] = ORIGINAL_STATE[1][-1][i]

    def __d_move_clockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][-1 - layer][i] = ORIGINAL_STATE[4][-1 - layer][i]
            self._STATE_OF_CUBE[2][-1 - layer][i] = ORIGINAL_STATE[1][-1 - layer][i]
            self._STATE_OF_CUBE[3][-1 - layer][i] = ORIGINAL_STATE[2][-1 - layer][i]
            self._STATE_OF_CUBE[4][-1 - layer][i] = ORIGINAL_STATE[3][-1 - layer][i]

    def __d_move_anticlockwise_internal(self, layer):
        layer -= 1
        ORIGINAL_STATE = deepcopy(self._STATE_OF_CUBE)
        for i in range(self._SIZE_OF_CUBE):
            self._STATE_OF_CUBE[1][-1 - layer][i] = ORIGINAL_STATE[2][-1 - layer][i]
            self._STATE_OF_CUBE[2][-1 - layer][i] = ORIGINAL_STATE[3][-1 - layer][i]
            self._STATE_OF_CUBE[3][-1 - layer][i] = ORIGINAL_STATE[4][-1 - layer][i]
            self._STATE_OF_CUBE[4][-1 - layer][i] = ORIGINAL_STATE[1][-1 - layer][i]

    def show(self, colors=False, icons=True):
        if colors and icons:
            self.__show_with_colors(icons=True)
        elif colors and not icons:
            self.__show_with_colors(icons=False)
        else:
            self.__show_without_colors()

    # we acquire amount of spaces that should be placed before number, by subtracting length of current element from
    # length of maximum element(for better visual look)
    def __print_spaces(self, cube_element):
        return (self._MAX_NUM_LEN - len(str(cube_element))) * " "

    def __generate_top_face(self):
        print((self._SQUARE_LEN + 1) * " " + "+" + "-" * self._SQUARE_LEN + "+")
        for i in range(self._SIZE_OF_CUBE):
            print((self._SQUARE_LEN + 1) * " " + "| " +
                  self.__print_spaces(self._STATE_OF_CUBE[0][i][0]) +
                  str(self._STATE_OF_CUBE[0][i][0]) + "  ", end="")
            for j in range(self._SIZE_OF_CUBE - 2):
                print(self.__print_spaces(self._STATE_OF_CUBE[0][i][j + 1]) +
                      str(self._STATE_OF_CUBE[0][i][j + 1]) + "  ", end="")
            print(self.__print_spaces(self._STATE_OF_CUBE[0][i][-1]) +
                  str(self._STATE_OF_CUBE[0][i][-1]) + " |")

    def __generate_middle_faces(self):
        print("+" + self._SQUARE_LEN * "-" + "+" + self._SQUARE_LEN * "-" + "+" + self._SQUARE_LEN * "-" + "+" +
              self._SQUARE_LEN * "-" + "+")
        for i in range(self._SIZE_OF_CUBE):
            print("| ", end="")
            for j in range(4):
                for k in range(self._SIZE_OF_CUBE - 1):
                    print(self.__print_spaces(self._STATE_OF_CUBE[j + 1][i][k]) +
                          str(self._STATE_OF_CUBE[j + 1][i][k]) + "  ", end="")
                print(self.__print_spaces(self._STATE_OF_CUBE[j + 1][i][-1]) +
                      str(self._STATE_OF_CUBE[j + 1][i][-1]) + " | ", end="")
            print("")
        print("+" + "-" * self._SQUARE_LEN + "+" + "-" * self._SQUARE_LEN + "+" + "-" * self._SQUARE_LEN + "+" +
              "-" * self._SQUARE_LEN + "+")

    def __generate_bottom_face(self):
        for i in range(self._SIZE_OF_CUBE):
            print(" " * (self._SQUARE_LEN + 1) + "| " + self.__print_spaces(self._STATE_OF_CUBE[-1][i][0]) +
                  str(self._STATE_OF_CUBE[-1][i][0]) + "  ", end="")
            for j in range(self._SIZE_OF_CUBE - 2):
                print(self.__print_spaces(self._STATE_OF_CUBE[-1][i][j + 1]) +
                      str(self._STATE_OF_CUBE[-1][i][j + 1]) + "  ", end="")
            print(self.__print_spaces(self._STATE_OF_CUBE[-1][i][-1]) +
                  str(self._STATE_OF_CUBE[-1][i][-1]) + " |")
        print(" " * (self._SQUARE_LEN + 1) + "+" + "-" * self._SQUARE_LEN + "+")

    def __show_without_colors(self):
        self.__generate_top_face()
        self.__generate_middle_faces()
        self.__generate_bottom_face()

    def __show_with_colors(self, icons=True):
        color_icon_config = {
            "empty": "⬛",
            "U": "🟪",
            "L": "🟧",
            "F": "🟩",
            "R": "🟥",
            "B": "🟦",
            "D": "🟨"
        }

        color_text_config = {
            "empty": " ",
            "U": "W",
            "L": "O",
            "F": "G",
            "R": "R",
            "B": "B",
            "D": "Y"
        }
        for i in range(self._SIZE_OF_CUBE):
            for j in range(self._SIZE_OF_CUBE):
                if not icons:
                    print(color_text_config["empty"], end="")
                else:
                    print(color_icon_config["empty"], end="")
            print(" ", end="")
            for j in range(self._SIZE_OF_CUBE):
                face = self.__get_face_by_element(self._STATE_OF_CUBE[0][i][j])
                if not icons:
                    print(color_text_config[face], end="")
                else:
                    print(color_icon_config[face], end="")
            print("")
        print("")
        for i in range(self._SIZE_OF_CUBE):
            for j in range(1, 5):
                for k in range(self._SIZE_OF_CUBE):
                    face = self.__get_face_by_element(self._STATE_OF_CUBE[j][i][k])
                    if not icons:
                        print(color_text_config[face], end="")
                    else:
                        print(color_icon_config[face], end="")
                print(" ", end="")
            print("")
        print("")
        for i in range(self._SIZE_OF_CUBE):
            for j in range(self._SIZE_OF_CUBE):
                if not icons:
                    print(color_text_config["empty"], end="")
                else:
                    print(color_icon_config["empty"], end="")
            print(" ", end="")
            for j in range(self._SIZE_OF_CUBE):
                face = self.__get_face_by_element(self._STATE_OF_CUBE[5][i][j])
                if not icons:
                    print(color_text_config[face], end="")
                else:
                    print(color_icon_config[face], end="")
            print("")
        print("")
        print("")

    def __get_face_by_element(self, element):
        square = self._SIZE_OF_CUBE * self._SIZE_OF_CUBE
        if element in self._UP_ELEMENTS:
            return "U"
        elif element in self._LEFT_ELEMENTS:
            return "L"
        elif element in self._FRONT_ELEMENTS:
            return "F"
        elif element in self._RIGHT_ELEMENTS:
            return "R"
        elif element in self._BACK_ELEMENTS:
            return "B"
        elif element in self._DOWN_ELEMENTS:
            return "D"

    def move(self, moves):
        self.__match_moves(moves)

    def __get_layer_len_from_move(self, move):
        n = 0
        for i in move:
            if not i.isdigit():
                break
            n += 1
        return n

    def __match_moves(self, moves):
        moves = moves.strip().split(" ")
        moves_dict = {
            "R": self.r,
            "L": self.l,
            "F": self.f,
            "U": self.u,
            "B": self.b,
            "D": self.d
        }
        ext_move_double = re.compile(r"^[RLFUBD]2$")  # U2, F2, ...
        ext_move_prime = re.compile(r"^[RLFUBD]'$")  # U', F', ...
        ext_move_single = re.compile(r"^[RLFUBD]$")  # U, F, ...
        int_move_single = re.compile(r"^[0-9]+[RLFUBD]$")  # 2U, 3F, ...
        int_move_prime = re.compile(r"^[0-9]+[RLFUBD]'$")  # 2U', 3F', ...
        int_move_double = re.compile(r"^[0-9]+[RLFUBD]2$")  # 2U2, 3F2, ...
        wide_move_single = re.compile(r"^[RLFUBD]w$")  # Uw, Fw, ...
        wide_move_prime = re.compile(r"^[RLFUBD]w'$")  # Uw', Fw', ...
        wide_move_double = re.compile(r"^[RLFUBD]w2$")  # Uw2, Fw2, ...
        adv_wide_move_single = re.compile(r"^[0-9]+[RLFUBD]w$")  # 2Uw, 3Fw, ...
        adv_wide_move_prime = re.compile(r"^[0-9]+[RLFUBD]w'$")  # 2Uw', 3Fw', ...
        adv_wide_move_double = re.compile(r"^[0-9]+[RLFUBD]w2$")  # 2Uw2, 3Fw2, ...
        for move in moves:
            move_index = self.__get_layer_len_from_move(move)  # only for use in moves that start with digit
            # U2, F2, ...
            if re.search(ext_move_double, move):
                moves_dict[move[0]]()
                moves_dict[move[0]]()
            # U', F', ...
            elif re.search(ext_move_prime, move):
                moves_dict[move[0]](clockwise=False)
            # U, F, ...
            elif re.search(ext_move_single, move):
                moves_dict[move]()
            # 2U, 3F, ...
            elif re.search(int_move_single, move):
                moves_dict[move[move_index]](layer=int(move[0]))
            # 2U', 3F', ...
            elif re.search(int_move_prime, move):
                moves_dict[move[move_index]](clockwise=False, layer=int(move[0]))
            # 2U2, 3F2, ...
            elif re.search(int_move_double, move):
                moves_dict[move[move_index]](layer=int(move[0]))
                moves_dict[move[move_index]](layer=int(move[0]))
            # Uw, Fw, ...
            elif re.search(wide_move_single, move):
                moves_dict[move[0]](layer=1)
                moves_dict[move[0]](layer=2)
            # Uw', Fw', ...
            elif re.search(wide_move_prime, move):
                moves_dict[move[0]](clockwise=False, layer=1)
                moves_dict[move[0]](clockwise=False, layer=2)
            # Uw2, Fw2, ...
            elif re.search(wide_move_double, move):
                moves_dict[move[0]](clockwise=False, layer=1)
                moves_dict[move[0]](clockwise=False, layer=2)
                moves_dict[move[0]](clockwise=False, layer=1)
                moves_dict[move[0]](clockwise=False, layer=2)
            # 2Uw, 3Fw, ...
            elif re.search(adv_wide_move_single, move):
                for i in range(int(move[0:move_index])):
                    moves_dict[move[move_index]](layer=i + 1)
            # 2Uw', 3Fw', ...
            elif re.search(adv_wide_move_prime, move):
                for i in range(int(move[0:move_index])):
                    moves_dict[move[move_index]](clockwise=False, layer=i + 1)
            # 2Uw2, 3Fw2, ...
            elif re.search(adv_wide_move_double, move):
                for i in range(int(move[0:move_index])):
                    moves_dict[move[move_index]](layer=i + 1)
                    moves_dict[move[move_index]](layer=i + 1)
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
        self.__match_moves(scramble)
        return scramble

    def get_state(self):
        return self._STATE_OF_CUBE

    def set_state(self, state):
        self._STATE_OF_CUBE = state

    def define_state(self, cube_string):
        self._UP_ELEMENTS = []
        self._LEFT_ELEMENTS = []
        self._FRONT_ELEMENTS = []
        self._RIGHT_ELEMENTS = []
        self._BACK_ELEMENTS = []
        self._DOWN_ELEMENTS = []
        cube_string_index = 0
        if len(cube_string) != self._SIZE_OF_CUBE * self._SIZE_OF_CUBE * 6:
            raise Exception("Invalid number of elements!")
        for face in range(6):
            for row in range(self._SIZE_OF_CUBE):
                for col in range(self._SIZE_OF_CUBE):
                    element = self._STATE_OF_CUBE[face][row][col]
                    if cube_string[cube_string_index] == "W":
                        self._UP_ELEMENTS.append(element)
                    elif cube_string[cube_string_index] == "O":
                        self._LEFT_ELEMENTS.append(element)
                    elif cube_string[cube_string_index] == "G":
                        self._FRONT_ELEMENTS.append(element)
                    elif cube_string[cube_string_index] == "R":
                        self._RIGHT_ELEMENTS.append(element)
                    elif cube_string[cube_string_index] == "B":
                        self._BACK_ELEMENTS.append(element)
                    elif cube_string[cube_string_index] == "Y":
                        self._DOWN_ELEMENTS.append(element)
                    else:
                        raise Exception("Invalid element!")
                    cube_string_index += 1

    def reset(self):
        self._STATE_OF_CUBE = self.__generate_clear_state()

    def __add_plane(plotter, center: (float, float, float), direction: (float, float, float), color: str):
        if color is not None:
            plane = pv.Plane(center=(center[0], center[1], center[2]),
                             direction=(direction[0], direction[1], direction[2]),
                             i_size=0.85, j_size=0.85)
            plotter.add_mesh(plane, color=color)

    def __add_number(plotter, number: str, center: (float, float, float), direction: (float, float, float),
                     rotate_x=False):
        if number is not None:
            text = pv.Text3D(number, height=0.5, depth=0.0,
                             normal=(direction[0], direction[1], direction[2]),
                             center=(center[0], center[1], center[2]))
            if rotate_x:
                text = text.rotate_x(180)
            plotter.add_mesh(text)

    def __add_cubie(self, plotter, center: (float, float, float),
                    up_color=None, bottom_color=None,
                    left_color=None, right_color=None,
                    front_color=None, back_color=None,
                    up_number=None, bottom_number=None,
                    left_number=None, right_number=None,
                    front_number=None, back_number=None):
        x = center[0]
        y = center[1]
        z = center[2]
        plotter.add_mesh(pv.Cube(center=center), color="black")
        self.__add_plane(plotter, center=(x + 0.501, y, z), direction=(1, 0, 0), color=front_color)
        self.__add_number(plotter, number=front_number, center=(x + 0.502, y, z), direction=(1, 0, 0))
        self.__add_plane(plotter, center=(x - 0.501, y, z), direction=(1, 0, 0), color=back_color)
        self.__add_number(plotter, number=back_number, center=(x - 0.502, y, z), direction=(-1, 0, 0), rotate_x=True)
        self.__add_plane(plotter, center=(x, y + 0.501, z), direction=(0, 1, 0), color=right_color)
        self.__add_number(plotter, number=right_number, center=(x, y + 0.502, z), direction=(0, 1, 0))
        self.__add_plane(plotter, center=(x, y - 0.501, z), direction=(0, 1, 0), color=left_color)
        self.__add_number(plotter, number=left_number, center=(x, y - 0.502, z), direction=(0, -1, 0))
        self.__add_plane(plotter, center=(x, y, z + 0.501), direction=(0, 0, 1), color=up_color)
        self.__add_number(plotter, number=up_number, center=(x, y, z + 0.502), direction=(0, 0, 0.5))
        self.__add_plane(plotter, center=(x, y, z - 0.501), direction=(0, 0, 1), color=bottom_color)
        self.__add_number(plotter, number=bottom_number, center=(x, y, z - 0.502), direction=(0, 0, -1))




    def show_3d(self, numbers=False):
        GAP_SIZE = 0.1
        CENTER_CUBE_SIZE = (self._SIZE_OF_CUBE - 1) + GAP_SIZE * (self._SIZE_OF_CUBE - 1)
        plotter = pv.Plotter()
        center_cube = pv.Cube(x_length=CENTER_CUBE_SIZE, y_length=CENTER_CUBE_SIZE, z_length=CENTER_CUBE_SIZE)
        plotter.add_mesh(center_cube, color="black")
        plotter.show()

