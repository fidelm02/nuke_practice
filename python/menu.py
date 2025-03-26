#
# Copyright (c) Nneex enterprise
# Nuke tools for VFX
#
# Dev. Fidel Moreno Miranda
# fidelm02@gmail.com
#


# Built-in modules
import os

# Third-party modules
import nuke


# Constants
ROOT_MENU_NAME = "Nneex"
DEEPHOLDOUT_PATH = os.path.dirname(
    os.path.abspath(__file__)).replace('\\', '/')


def main():
    """
    Main function to create the custom Deepholdout menu entry in Nuke.

    This function checks if a menu named ROOT_MENU_NAME exists in the 
    Nuke Nodes toolbar. If it doesn't exist, it creates the menu and adds
    a command to paste a deepHoldout node from a specified file path.
    """
    # Access the Nodes toolbar in Nuke
    nodes_toolbar = nuke.toolbar("Nodes") # type: nuke.ToolBar
    
    # Find the custom menu by its name
    root_menu = nodes_toolbar.findItem(ROOT_MENU_NAME) # type: nuke.Menu

    # If the menu does not exist, create it
    if root_menu is None:
        root_menu = nodes_toolbar.addMenu(ROOT_MENU_NAME) # type: nuke.MenuItem

    # Add a command to the menu to paste the deepHoldout node
    root_menu.addCommand(
        "Nnex node search",
        "import nx_node_search.nnx_node_search_presenter as nnx_search; "\
        "nnx_search.NodeSearchPresenter().show()")

main()