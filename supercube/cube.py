from abc import ABC, abstractmethod


class Cube(ABC):
    @property
    @abstractmethod
    def _size_of_cube(self) -> int:
        pass

    @staticmethod
    def _generate_clear_state(size_of_cube: int):
        n = 1
        result = []
        for face in range(6):
            result.append([])
            for row in range(size_of_cube):
                result[face].append([])
                for col in range(size_of_cube):
                    result[face][row].append(n)
                    n += 1
        return result

    def __init__(self):
        self._STATE_OF_CUBE = self._generate_clear_state(self._size_of_cube)

    def u(self, opposite=False):
        pass

    def f(self, opposite=False):
        pass

    def b(self, opposite=False):
        pass

    def r(self, opposite=False):
        pass

    def l(self, opposite=False):
        pass

    def d(self, opposite=False):
        pass

    def show(self, colors=False):
        self._show_without_colors()

    def _generate_top_face(self):
        max_len_num = len(str(self._STATE_OF_CUBE[-1][-1][-1]))
        square_len = 2 + max_len_num * self._size_of_cube + 2 * (self._size_of_cube - 1)
        calculate_spaces = lambda num: max_len_num - len(str(num))
        print((square_len + 1) * " " + "┌" + "─" * square_len + "┐")
        for i in range(self._size_of_cube):
            print((square_len + 1) * " " + "│ " +
                  calculate_spaces(self._STATE_OF_CUBE[0][i][0]) * " " +
                  str(self._STATE_OF_CUBE[0][i][0]) + "  ", end="")
            for j in range(self._size_of_cube - 2):
                print(calculate_spaces(self._STATE_OF_CUBE[0][i][j + 1]) * " " +
                      str(self._STATE_OF_CUBE[0][i][j + 1]) + "  ", end="")
            print(calculate_spaces(self._STATE_OF_CUBE[0][i][-1]) * " " +
                  str(self._STATE_OF_CUBE[0][i][-1]) + " │")

    def _generate_middle_faces(self):
        max_len_num = len(str(self._STATE_OF_CUBE[-1][-1][-1]))
        square_len = 2 + max_len_num * self._size_of_cube + 2 * (self._size_of_cube - 1)
        calculate_spaces = lambda num: max_len_num - len(str(num))
        print("┌" + square_len * "─" + "┼" + square_len * "─" + "┼" + square_len * "─" + "┬" + square_len * "─" + "┐")
        for i in range(self._size_of_cube):
            print("│ ", end="")
            for j in range(4):
                for k in range(self._size_of_cube-1):
                    print(calculate_spaces(self._STATE_OF_CUBE[j+1][i][k]) * " " +
                          str(self._STATE_OF_CUBE[j+1][i][k]) + "  ", end="")
                print(calculate_spaces(self._STATE_OF_CUBE[j+1][i][-1]) * " " +
                      str(self._STATE_OF_CUBE[j+1][i][-1]) + " │ ", end="")
            print("")
        print("└" + "─" * square_len + "┼" + "─" * square_len + "┼" + "─" * square_len + "┴" + "─" * square_len + "┘")

    def _show_without_colors(self):
        self._generate_top_face()
        self._generate_middle_faces()

    def _show_with_colors(self):
        pass
