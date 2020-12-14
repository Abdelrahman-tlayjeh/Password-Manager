from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_controlDialog(object):
    def setupUi(self, controlDialog):
        controlDialog.setObjectName("controlDialog")
        controlDialog.setFixedSize(800, 603)
        controlDialog.setStyleSheet("background-color: rgb(85, 170, 255); color: rgb(255, 255, 255);")
        controlDialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        controlDialog.setWindowIcon(QtGui.QIcon('sources\window_icon.ico'))

        self.control_panel_text = QtWidgets.QLabel(controlDialog)
        self.control_panel_text.setGeometry(QtCore.QRect(10, 10, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.control_panel_text.setFont(font)
        self.control_panel_text.setStyleSheet("font-weight: bold; font:  35pt \"Yu Gothic UI Semibold\";")
        self.control_panel_text.setObjectName("control_panel_text")

        self.line = QtWidgets.QFrame(controlDialog)
        self.line.setGeometry(QtCore.QRect(380, 60, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.change_delete_commandLinkButton = QtWidgets.QCommandLinkButton(controlDialog)
        self.change_delete_commandLinkButton.setGeometry(QtCore.QRect(20, 180, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.change_delete_commandLinkButton.setFont(font)
        self.change_delete_commandLinkButton.setStyleSheet("background-color: rgb(70, 141, 211);")
        self.change_delete_commandLinkButton.setIconSize(QtCore.QSize(30, 30))
        self.change_delete_commandLinkButton.setObjectName("change_delete_commandLinkButton")

        self.view_all_commandLinkButton = QtWidgets.QCommandLinkButton(controlDialog)
        self.view_all_commandLinkButton.setGeometry(QtCore.QRect(20, 280, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.view_all_commandLinkButton.setFont(font)
        self.view_all_commandLinkButton.setStyleSheet("background-color: rgb(70, 141, 211);")
        self.view_all_commandLinkButton.setIconSize(QtCore.QSize(30, 30))
        self.view_all_commandLinkButton.setObjectName("view_all_commandLinkButton")

        self.clear_all_data_commandLinkButton = QtWidgets.QCommandLinkButton(controlDialog)
        self.clear_all_data_commandLinkButton.setGeometry(QtCore.QRect(20, 380, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.clear_all_data_commandLinkButton.setFont(font)
        self.clear_all_data_commandLinkButton.setStyleSheet("background-color: rgb(70, 141, 211);")
        self.clear_all_data_commandLinkButton.setIconSize(QtCore.QSize(30, 30))
        self.clear_all_data_commandLinkButton.setObjectName("clear_all_data_commandLinkButton")

        self.line_2 = QtWidgets.QFrame(controlDialog)
        self.line_2.setGeometry(QtCore.QRect(0, 100, 371, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.return_pushButton = QtWidgets.QPushButton(controlDialog)
        self.return_pushButton.setGeometry(QtCore.QRect(10, 550, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.return_pushButton.setFont(font)
        self.return_pushButton.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.return_pushButton.setObjectName("return_pushButton")

        #remove focus
        self.change_delete_commandLinkButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.view_all_commandLinkButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_all_data_commandLinkButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.return_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)

        self.retranslateUi(controlDialog)
        QtCore.QMetaObject.connectSlotsByName(controlDialog)

    def retranslateUi(self, controlDialog):
        _translate = QtCore.QCoreApplication.translate
        controlDialog.setWindowTitle(_translate("controlDialog", "Password Manager - Control panel"))
        self.control_panel_text.setText(_translate("controlDialog", "Control Panel"))
        self.change_delete_commandLinkButton.setText(_translate("controlDialog", "Change/delete Password"))
        self.view_all_commandLinkButton.setText(_translate("controlDialog", "view all saved passwords"))
        self.clear_all_data_commandLinkButton.setText(_translate("controlDialog", "Clear data"))
        self.return_pushButton.setText(_translate("controlDialog", "return"))
