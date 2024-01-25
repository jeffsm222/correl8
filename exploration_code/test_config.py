# -----------------------------------
# set the sys path for functions
# -----------------------------------
import sys
import os

# Add the directory containing the configs.py to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'configs')))
# -----------------------------------
# -----------------------------------

# -----------------------------------
# Set the other libaries
# -----------------------------------

# Attempt to import configs
import configs

# -----------------------------------
# -----------------------------------
print(configs.get_folder("data"))
