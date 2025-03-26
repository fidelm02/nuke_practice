#
# Copyright (c) Nneex enterprise
# Nuke tools for VFX
#
# Dev. Fidel Moreno Miranda
# fidelm02@gmail.com
#


# standard library

# third-party modules
import nuke

class NodeSearchModel:
    def search_nodes(self, type_node, recurse_node):
        """
        Search nodes in the script

        :param type_node: type of node to search
        :param recurse_node: recursive search

        :return: list, nodes found
        """
        nodes = nuke.allNodes(recurseGroups=recurse_node)
        nodes = [node for node in nodes if node.Class() == type_node]

        return nodes

    