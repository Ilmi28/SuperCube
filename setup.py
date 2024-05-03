from setuptools import setup, find_packages
import codecs

VERSION='0.0.1'
DESCRIPTION="Library for simulating rubik's cubes of different sizes (N x N), and for solving 2 x 2 and 3 x 3 cubes with kociemba algorithm."

setup(
    name="super_rubik_cube",
    VERSION=VERSION,
    author="Ilmi28",
    author_email="<ilmialiev28@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'rubik', 'cube', 'solve', '3x3', '2x2', "rubik's cube", 'pocket cube', 'NxN', 'kociemba', 'supercube']
)