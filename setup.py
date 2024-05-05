from setuptools import setup, find_packages

DESCRIPTION="Library for simulating rubik's cubes of different sizes (N x N), and for solving 2 x 2 and 3 x 3 cubes with kociemba algorithm."
LONG_DESCRIPTION = open("README.md", encoding="utf8").read()
project_urls = {
    "Homepage": "https://github.com/Ilmi28/SuperCube"
}


setup(
    name="super-rubik-cube",
    version="1.0.3",
    author="Ilmi28",
    author_email="<ilmialiev28@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    package_data={'supercube': ['kociemba/pykociemba/prunetables/*']},
    packages=find_packages(),
    keywords=['python', 'rubik', 'cube', 'solve', '3x3', '2x2', "rubik's cube", 'pocket cube', 'NxN', 'kociemba', 'supercube', 'solver'],
    project_urls=project_urls,
    license='GPL-3.0'
)
