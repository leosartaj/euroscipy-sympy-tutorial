#!/usr/bin/env python

from sys import exit
from subprocess import check_output

error = False

try:
    from pkg_resources import parse_version
except ImportError:
    print("Setuptools must be installed for the tutorial.")
    error = True

try:
    import numpy
except ImportError:
    print("NumPy is required for the tutorial")
    error = True

try:
    import sympy
except ImportError:
    print("SymPy must be installed for the tutorial")
    error = True
else:
    if parse_version(sympy.__version__) < parse_version('1.1'):
        print("SymPy >= 1.1 is required for the tutorial.")

try:
    import matplotlib
except ImportError:
    print("matplotlib is required for the tutorial")
    error = True

try:
    import notebook
except ImportError:
    print("notebook (jupyter notebook) is required for the tutorial")
    error = True

exit(error)
