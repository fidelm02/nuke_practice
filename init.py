#
# Copyright (c) Nneex enterprise
# Nuke tools for VFX
#
# Dev. Fidel Moreno Miranda
# fidelm02@gmail.com
#

# Built-in modules
import os
import sys

# Third-party modules
import nuke


# Adding python folder to nuke plugin paths
NUKE_PRACTICE_PATH = os.path.dirname(__file__)

# p = "D:\Fidel\Documents\Trabajo\Nneex\nuke_practice\python"
# nuke.pluginAddPath(p)

nuke.pluginAddPath(os.path.join(NUKE_PRACTICE_PATH, "resources"))
nuke.pluginAddPath(os.path.join(NUKE_PRACTICE_PATH, "python"))

if not NUKE_PRACTICE_PATH in sys.path:
    sys.path.append(NUKE_PRACTICE_PATH)
    sys.path.append(os.path.join(NUKE_PRACTICE_PATH, "python"))
