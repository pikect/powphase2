# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PointOnWaveConfigurator(object):
    def setupUi(self, PointOnWaveConfigurator):
        PointOnWaveConfigurator.setObjectName("PointOnWaveConfigurator")
        PointOnWaveConfigurator.resize(1042, 560)
        self.centralwidget = QtWidgets.QWidget(PointOnWaveConfigurator)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(260, 10, 771, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 350, 281, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(10, 20, 281, 20))
        self.label_17.setObjectName("label_17")
        self.text_main_fq = QtWidgets.QLineEdit(self.frame_2)
        self.text_main_fq.setGeometry(QtCore.QRect(10, 50, 81, 28))
        self.text_main_fq.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_main_fq.setObjectName("text_main_fq")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(400, 220, 281, 101))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 111, 20))
        self.label_16.setObjectName("label_16")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(10, 30, 62, 30))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(120, 30, 62, 30))
        self.label_15.setObjectName("label_15")
        self.text_close_angle = QtWidgets.QLineEdit(self.frame_3)
        self.text_close_angle.setGeometry(QtCore.QRect(120, 60, 81, 28))
        self.text_close_angle.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_close_angle.setObjectName("text_close_angle")
        self.text_open_angle = QtWidgets.QLineEdit(self.frame_3)
        self.text_open_angle.setGeometry(QtCore.QRect(10, 60, 81, 28))
        self.text_open_angle.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_open_angle.setObjectName("text_open_angle")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(19, 21, 281, 171))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(79, 45, 62, 20))
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(10, 46, 62, 20))
        self.label_4.setObjectName("label_4")
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setGeometry(QtCore.QRect(10, 16, 131, 20))
        self.label_18.setObjectName("label_18")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(189, 45, 62, 20))
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 70, 20, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.text_start_open_A = QtWidgets.QLineEdit(self.frame_4)
        self.text_start_open_A.setGeometry(QtCore.QRect(80, 70, 81, 28))
        self.text_start_open_A.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_start_open_A.setInputMask("00.00")
        self.text_start_open_A.setObjectName("text_start_open_A")
        self.text_start_close_A = QtWidgets.QLineEdit(self.frame_4)
        self.text_start_close_A.setGeometry(QtCore.QRect(190, 70, 81, 28))
        self.text_start_close_A.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_start_close_A.setObjectName("text_start_close_A")
        self.text_start_close_B = QtWidgets.QLineEdit(self.frame_4)
        self.text_start_close_B.setGeometry(QtCore.QRect(190, 100, 81, 28))
        self.text_start_close_B.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_start_close_B.setObjectName("text_start_close_b")
        self.text_start_open_B = QtWidgets.QLineEdit(self.frame_4)
        self.text_start_open_B.setGeometry(QtCore.QRect(80, 100, 81, 28))
        self.text_start_open_B.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_start_open_B.setObjectName("text_start_open_B")
        self.text_start_close_C = QtWidgets.QLineEdit(self.frame_4)
        self.text_start_close_C.setGeometry(QtCore.QRect(190, 130, 81, 28))
        self.text_start_close_C.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_start_close_C.setObjectName("text_start_close_C")
        self.text_start_open_C = QtWidgets.QLineEdit(self.frame_4)
        self.text_start_open_C.setGeometry(QtCore.QRect(80, 130, 81, 28))
        self.text_start_open_C.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_start_open_C.setObjectName("text_start_open_C")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(20, 220, 281, 101))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_22 = QtWidgets.QLabel(self.frame_5)
        self.label_22.setGeometry(QtCore.QRect(10, 10, 151, 20))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_5)
        self.label_23.setGeometry(QtCore.QRect(10, 30, 62, 30))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_5)
        self.label_24.setGeometry(QtCore.QRect(120, 30, 62, 30))
        self.label_24.setObjectName("label_24")
        self.text_open_impulse = QtWidgets.QLineEdit(self.frame_5)
        self.text_open_impulse.setGeometry(QtCore.QRect(10, 60, 81, 28))
        self.text_open_impulse.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_open_impulse.setObjectName("text_open_impulse")
        self.text_close_impulse = QtWidgets.QLineEdit(self.frame_5)
        self.text_close_impulse.setGeometry(QtCore.QRect(120, 60, 81, 28))
        self.text_close_impulse.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_close_impulse.setObjectName("text_close_impulse")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(400, 20, 281, 171))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setGeometry(QtCore.QRect(79, 45, 62, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setGeometry(QtCore.QRect(10, 46, 62, 20))
        self.label_11.setObjectName("label_11")
        self.label_20 = QtWidgets.QLabel(self.frame_6)
        self.label_20.setGeometry(QtCore.QRect(10, 16, 131, 20))
        self.label_20.setObjectName("label_20")
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        self.label_12.setGeometry(QtCore.QRect(189, 45, 62, 20))
        self.label_12.setObjectName("label_12")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_6)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 70, 20, 91))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_5.addWidget(self.label_21)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_5.addWidget(self.label_25)
        self.text_stop_open_A = QtWidgets.QLineEdit(self.frame_6)
        self.text_stop_open_A.setGeometry(QtCore.QRect(80, 70, 81, 28))
        self.text_stop_open_A.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_stop_open_A.setObjectName("text_stop_open_A")
        self.text_stop_close_A = QtWidgets.QLineEdit(self.frame_6)
        self.text_stop_close_A.setGeometry(QtCore.QRect(190, 70, 81, 28))
        self.text_stop_close_A.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_stop_close_A.setObjectName("text_stop_close_A")
        self.text_stop_close_B = QtWidgets.QLineEdit(self.frame_6)
        self.text_stop_close_B.setGeometry(QtCore.QRect(190, 100, 81, 28))
        self.text_stop_close_B.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_stop_close_B.setObjectName("text_stop_close_B")
        self.text_stop_open_B = QtWidgets.QLineEdit(self.frame_6)
        self.text_stop_open_B.setGeometry(QtCore.QRect(80, 100, 81, 28))
        self.text_stop_open_B.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_stop_open_B.setObjectName("text_stop_open_B")
        self.text_stop_close_C = QtWidgets.QLineEdit(self.frame_6)
        self.text_stop_close_C.setGeometry(QtCore.QRect(190, 130, 81, 28))
        self.text_stop_close_C.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_stop_close_C.setObjectName("text_stop_close_C")
        self.text_stop_open_C = QtWidgets.QLineEdit(self.frame_6)
        self.text_stop_open_C.setGeometry(QtCore.QRect(80, 130, 81, 28))
        self.text_stop_open_C.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_stop_open_C.setObjectName("text_stop_open_C")
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 240, 471))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.push_read_json = QtWidgets.QPushButton(self.layoutWidget1)
        self.push_read_json.setObjectName("push_read_json")
        self.verticalLayout.addWidget(self.push_read_json)
        self.push_write_json = QtWidgets.QPushButton(self.layoutWidget1)
        self.push_write_json.setObjectName("push_write_json")
        self.verticalLayout.addWidget(self.push_write_json)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.push_open_files = QtWidgets.QPushButton(self.layoutWidget1)
        self.push_open_files.setObjectName("push_open_files")
        self.verticalLayout_2.addWidget(self.push_open_files)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.push_restart_svc = QtWidgets.QPushButton(self.layoutWidget1)
        self.push_restart_svc.setObjectName("push_restart_svc")
        self.verticalLayout_2.addWidget(self.push_restart_svc)
        self.push_restart_fw = QtWidgets.QPushButton(self.layoutWidget1)
        self.push_restart_fw.setObjectName("push_restart_fw")
        self.verticalLayout_2.addWidget(self.push_restart_fw)
        self.push_reboot = QtWidgets.QPushButton(self.layoutWidget1)
        self.push_reboot.setObjectName("push_reboot")
        self.verticalLayout_2.addWidget(self.push_reboot)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        PointOnWaveConfigurator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PointOnWaveConfigurator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        PointOnWaveConfigurator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PointOnWaveConfigurator)
        self.statusbar.setObjectName("statusbar")
        PointOnWaveConfigurator.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(PointOnWaveConfigurator)
        self.actionClose.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(PointOnWaveConfigurator)
        QtCore.QMetaObject.connectSlotsByName(PointOnWaveConfigurator)

    def retranslateUi(self, PointOnWaveConfigurator):
        _translate = QtCore.QCoreApplication.translate
        PointOnWaveConfigurator.setWindowTitle(_translate("PointOnWaveConfigurator", "Point on wave configuration toolbox"))
        self.label_17.setText(_translate("PointOnWaveConfigurator", "Main Frequency [Hz]:"))
        self.text_main_fq.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.label_16.setText(_translate("PointOnWaveConfigurator", "Angle [degrees]"))
        self.label_14.setText(_translate("PointOnWaveConfigurator", "Open"))
        self.label_15.setText(_translate("PointOnWaveConfigurator", "Close"))
        self.text_close_angle.setInputMask(_translate("PointOnWaveConfigurator", "000.0"))
        self.text_open_angle.setInputMask(_translate("PointOnWaveConfigurator", "000.0"))
        self.label_8.setText(_translate("PointOnWaveConfigurator", "Open"))
        self.label_4.setText(_translate("PointOnWaveConfigurator", "Phase"))
        self.label_18.setText(_translate("PointOnWaveConfigurator", "Starting point [ms]"))
        self.label_9.setText(_translate("PointOnWaveConfigurator", "Close"))
        self.label_5.setText(_translate("PointOnWaveConfigurator", "A"))
        self.label_7.setText(_translate("PointOnWaveConfigurator", "B"))
        self.label_6.setText(_translate("PointOnWaveConfigurator", "C"))
        self.text_start_close_A.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.text_start_close_B.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.text_start_open_B.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.text_start_close_C.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.text_start_open_C.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.label_22.setText(_translate("PointOnWaveConfigurator", "Impulse duration [ms]"))
        self.label_23.setText(_translate("PointOnWaveConfigurator", "Open"))
        self.label_24.setText(_translate("PointOnWaveConfigurator", "Close"))
        self.text_open_impulse.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.text_close_impulse.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.label_10.setText(_translate("PointOnWaveConfigurator", "Open"))
        self.label_11.setText(_translate("PointOnWaveConfigurator", "Phase"))
        self.label_20.setText(_translate("PointOnWaveConfigurator", "Stop point [ms]"))
        self.label_12.setText(_translate("PointOnWaveConfigurator", "Close"))
        self.label_13.setText(_translate("PointOnWaveConfigurator", "A"))
        self.label_21.setText(_translate("PointOnWaveConfigurator", "B"))
        self.label_25.setText(_translate("PointOnWaveConfigurator", "C"))
        self.text_stop_open_A.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.text_stop_close_A.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.text_stop_close_B.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.text_stop_open_B.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.text_stop_close_C.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.text_stop_open_C.setInputMask(_translate("PointOnWaveConfigurator", "00.00"))
        self.label_2.setText(_translate("PointOnWaveConfigurator", "Configuration"))
        self.push_read_json.setText(_translate("PointOnWaveConfigurator", "Read configuration from the device"))
        self.push_write_json.setText(_translate("PointOnWaveConfigurator", "Write configuration to the device"))
        self.label_3.setText(_translate("PointOnWaveConfigurator", "Download .CSV file "))
        self.push_open_files.setText(_translate("PointOnWaveConfigurator", "Find remote files"))
        self.label.setText(_translate("PointOnWaveConfigurator", "Device Control"))
        self.push_restart_svc.setText(_translate("PointOnWaveConfigurator", "Restart PoW Service"))
        self.push_restart_fw.setText(_translate("PointOnWaveConfigurator", "Restart RT Firmware"))
        self.push_reboot.setText(_translate("PointOnWaveConfigurator", "Reboot"))
        self.menuFile.setTitle(_translate("PointOnWaveConfigurator", "File"))
        self.actionClose.setText(_translate("PointOnWaveConfigurator", "Close"))
