# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_csv.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileDialog(object):
    def setupUi(self, FileDialog):
        FileDialog.setObjectName("FileDialog")
        FileDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        FileDialog.resize(790, 479)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileDialog.sizePolicy().hasHeightForWidth())
        FileDialog.setSizePolicy(sizePolicy)
        FileDialog.setModal(True)
        self.listView = QtWidgets.QListView(FileDialog)
        self.listView.setGeometry(QtCore.QRect(110, 60, 661, 381))
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setProperty("showDropIndicator", False)
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listView.setObjectName("listView")
        self.layoutWidget = QtWidgets.QWidget(FileDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 100, 107))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.push_list_files = QtWidgets.QPushButton(self.layoutWidget)
        self.push_list_files.setObjectName("push_list_files")
        self.verticalLayout.addWidget(self.push_list_files)
        self.push_plot_file = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_plot_file.sizePolicy().hasHeightForWidth())
        self.push_plot_file.setSizePolicy(sizePolicy)
        self.push_plot_file.setObjectName("push_plot_file")
        self.verticalLayout.addWidget(self.push_plot_file)
        self.push_save_file = QtWidgets.QPushButton(self.layoutWidget)
        self.push_save_file.setObjectName("push_save_file")
        self.verticalLayout.addWidget(self.push_save_file)
        self.label = QtWidgets.QLabel(FileDialog)
        self.label.setGeometry(QtCore.QRect(110, 40, 62, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FileDialog)
        self.label_2.setGeometry(QtCore.QRect(510, 40, 62, 20))
        self.label_2.setObjectName("label_2")
        self.push_delete_file = QtWidgets.QPushButton(FileDialog)
        self.push_delete_file.setGeometry(QtCore.QRect(10, 410, 89, 28))
        self.push_delete_file.setObjectName("push_delete_file")

        self.retranslateUi(FileDialog)
        QtCore.QMetaObject.connectSlotsByName(FileDialog)

    def retranslateUi(self, FileDialog):
        _translate = QtCore.QCoreApplication.translate
        FileDialog.setWindowTitle(_translate("FileDialog", "File Dialog"))
        self.push_list_files.setText(_translate("FileDialog", "List Files"))
        self.push_plot_file.setText(_translate("FileDialog", "Plot File"))
        self.push_save_file.setText(_translate("FileDialog", "Save File"))
        self.label.setText(_translate("FileDialog", "Name:"))
        self.label_2.setText(_translate("FileDialog", "Size:"))
        self.push_delete_file.setText(_translate("FileDialog", "Delete Files"))
