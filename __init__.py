__version__ = "1.0.0"
__author__ = "Muktadir"

# Code to run when the package is imported
print("I am constructor package")

# Importing the `calculate` function from module_1
from .module_1 import calculate
from .module_2 import calculate_area_of_triangle
from .module_3 import area_of_circle
