#
# Copyright (c) Nneex enterprise
# Nuke tools for VFX
#
# Dev. Fidel Moreno Miranda
# fidelm02@gmail.com
#


# standard library
import os
import sys

# third-party modules
import nuke
from PySide2 import QtCore, QtGui, QtWidgets

# Nneex modules
from nx_node_search.nnex_node_search_view import Ui_NNxNodeSearch
from nx_node_search.nnex_node_search_model import NodeSearchModel

class NodeSearchPresenter(QtWidgets.QDialog):
    def __init__(self):
        super(NodeSearchPresenter, self).__init__()
        self.view = Ui_NNxNodeSearch()
        self.view.setupUi(self)
        self.core = NodeSearchModel()
        self.found_nodes = []
        self.__connect_actions()

    def __connect_actions(self):
        """
        Connect actions
        """
        self.view.ui.btn_search.clicked.connect(self.search_nodes)
        self.view.ui.btn_delete.clicked.connect(self.delete_nodes)


    def launch(self):
        """
        """
        self.view.show()


    def search_nodes(self):
        """
        Search nodes in the script
        """
        recurse_search = self.view.ui.chk_recursive.isChecked()
        node_type = self.view.ui.cmb_type.currentText()
        self.found_nodes = self.core.search_nodes(node_type, recurse_search)
        self.view.ui.textEdit.clear()
        self.view.ui.textEdit.append("Nodes found: {}".format(len(self.found_nodes)))
        self.view.ui.textEdit.append("")
        for node in self.found_nodes:
            self.view.ui.textEdit.append(node.fullName())
        

    def delete_nodes(self):
        """
        Delete nodes in the script
        """
        nodes_to_delete = len(self.found_nodes)

        if not nodes_to_delete:
            nuke.message("No nodes to delete")
        
        for node in self.found_nodes:
            nuke.delete(node)

        nuke.message("Nodes deleted: {}".format(nodes_to_delete))

    