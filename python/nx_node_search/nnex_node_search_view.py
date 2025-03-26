# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'types_browserCcCcoD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NNxNodeSearch(object):
    def setupUi(self, NNxNodeSearch):
        
        
        if not NNxNodeSearch.objectName():
            NNxNodeSearch.setObjectName(u"NNxNodeSearch")
        NNxNodeSearch.resize(400, 300)
        self.horizontalLayout_2 = QHBoxLayout(NNxNodeSearch)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(NNxNodeSearch)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.cmb_type = QComboBox(self.frame_2)
        self.cmb_type.addItem("")
        self.cmb_type.addItem("")
        self.cmb_type.addItem("")
        self.cmb_type.setObjectName(u"cmb_type")

        self.horizontalLayout.addWidget(self.cmb_type)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.chk_recursive = QCheckBox(self.frame_3)
        self.chk_recursive.setObjectName(u"chk_recursive")

        self.verticalLayout_2.addWidget(self.chk_recursive)

        self.textEdit = QTextEdit(self.frame_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame = QFrame(NNxNodeSearch)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(120, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")

        self.verticalLayout.addWidget(self.btn_search)

        self.btn_delete = QPushButton(self.frame)
        self.btn_delete.setObjectName(u"btn_delete")

        self.verticalLayout.addWidget(self.btn_delete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(NNxNodeSearch)

        QMetaObject.connectSlotsByName(NNxNodeSearch)
    # setupUi

    def retranslateUi(self, NNxNodeSearch):
        NNxNodeSearch.setWindowTitle(QCoreApplication.translate("NNxNodeSearch", u"Nodes search", None))
        self.label.setText(QCoreApplication.translate("NNxNodeSearch", u"Type", None))
        self.cmb_type.setItemText(0, QCoreApplication.translate("NNxNodeSearch", u"Viewer", None))
        self.cmb_type.setItemText(1, QCoreApplication.translate("NNxNodeSearch", u"Read", None))
        self.cmb_type.setItemText(2, QCoreApplication.translate("NNxNodeSearch", u"Transform", None))

        self.chk_recursive.setText(QCoreApplication.translate("NNxNodeSearch", u"Recursive search", None))
        self.btn_search.setText(QCoreApplication.translate("NNxNodeSearch", u"Search", None))
        self.btn_delete.setText(QCoreApplication.translate("NNxNodeSearch", u"Delete", None))
    # retranslateUi

