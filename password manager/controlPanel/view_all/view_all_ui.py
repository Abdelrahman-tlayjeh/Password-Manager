from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_viewAllDialog(object):
    def setupUi(self, viewAllDialog):
        viewAllDialog.setObjectName("viewAllDialog")
        viewAllDialog.setFixedSize(1202, 672)
        font = QtGui.QFont()
        font.setPointSize(16)
        viewAllDialog.setFont(font)
        viewAllDialog.setStyleSheet("background-color: rgb(85, 170, 255); color: rgb(255, 255, 255);")
        viewAllDialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        viewAllDialog.setWindowIcon(QtGui.QIcon('sources\window_icon.ico'))

        self.view_all_pushButton = QtWidgets.QPushButton(viewAllDialog)
        self.view_all_pushButton.setGeometry(QtCore.QRect(10, 10, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_all_pushButton.setFont(font)
        self.view_all_pushButton.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.view_all_pushButton.setObjectName("view_all_pushButton")

        self.or_text = QtWidgets.QLabel(viewAllDialog)
        self.or_text.setGeometry(QtCore.QRect(120, 20, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.or_text.setFont(font)
        self.or_text.setStyleSheet("")
        self.or_text.setObjectName("or_text")

        self.view_specific_pushButton = QtWidgets.QPushButton(viewAllDialog)
        self.view_specific_pushButton.setGeometry(QtCore.QRect(160, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_specific_pushButton.setFont(font)
        self.view_specific_pushButton.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.view_specific_pushButton.setObjectName("view_specific_pushButton")

        self.search_groupBox = QtWidgets.QGroupBox(viewAllDialog)
        self.search_groupBox.setEnabled(True)
        self.search_groupBox.setGeometry(QtCore.QRect(340, 20, 881, 91))
        self.search_groupBox.setStyleSheet("border: 1px solid rgb(85, 170, 255);")
        self.search_groupBox.setTitle("")
        self.search_groupBox.setObjectName("search_groupBox")
        #hide search
        self.search_groupBox.hide()

        self.search_by_text = QtWidgets.QLabel(self.search_groupBox)
        self.search_by_text.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.search_by_text.setFont(font)
        self.search_by_text.setObjectName("search_by_text")

        self.search_by_comboBox = QtWidgets.QComboBox(self.search_groupBox)
        self.search_by_comboBox.setGeometry(QtCore.QRect(10, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_by_comboBox.setFont(font)
        self.search_by_comboBox.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); border: 1px solid rgb(0, 0, 0);")
        self.search_by_comboBox.setObjectName("search_by_comboBox")
        self.search_by_comboBox.addItem("")
        self.search_by_comboBox.addItem("")
        self.search_by_comboBox.addItem("")
        self.search_by_comboBox.addItem("")
        self.search_by_comboBox.addItem("")
        self.search_by_comboBox.addItem("")

        self.search_lineEdit = QtWidgets.QLineEdit(self.search_groupBox)
        self.search_lineEdit.setGeometry(QtCore.QRect(200, 40, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_lineEdit.setFont(font)
        self.search_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); border: 1px solid rgb(0, 0, 0);")
        self.search_lineEdit.setText("")
        self.search_lineEdit.setObjectName("search_lineEdit")

        self.view_pushButton = QtWidgets.QPushButton(self.search_groupBox)
        self.view_pushButton.setGeometry(QtCore.QRect(780, 40, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_pushButton.setFont(font)
        self.view_pushButton.setStyleSheet("""
        QPushButton{
            background-color: rgb(85, 85, 255);
            border: 1px solid rgb(0, 0, 0);
        }
        QPushButton::pressed{
            border: 2px solid rgb(0, 0, 0);
        }
        """)
        self.view_pushButton.setObjectName("view_pushButton")

        self.results_textBrowser = QtWidgets.QTextBrowser(viewAllDialog)
        self.results_textBrowser.setGeometry(QtCore.QRect(10, 190, 1181, 421))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.results_textBrowser.setFont(font)
        self.results_textBrowser.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.results_textBrowser.setObjectName("results_textBrowser")

        self.format_description_text = QtWidgets.QLabel(viewAllDialog)
        self.format_description_text.setGeometry(QtCore.QRect(120, 150, 841, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.format_description_text.setFont(font)
        self.format_description_text.setObjectName("format_description_text")

        
        self.return_pushButton = QtWidgets.QPushButton(viewAllDialog)
        self.return_pushButton.setGeometry(QtCore.QRect(10, 620, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.return_pushButton.setFont(font)
        self.return_pushButton.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.return_pushButton.setObjectName("return_pushButton")

        self.retranslateUi(viewAllDialog)
        QtCore.QMetaObject.connectSlotsByName(viewAllDialog)

    def retranslateUi(self, viewAllDialog):
        _translate = QtCore.QCoreApplication.translate
        viewAllDialog.setWindowTitle(_translate("viewAllDialog", "Control Panel - View all Passwords"))
        self.results_textBrowser.setHtml(_translate("viewAllDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.format_description_text.setText(_translate("viewAllDialog", "display format: (id, username, e-mail, app name, password, account creation date)"))
        self.view_all_pushButton.setText(_translate("viewAllDialog", "view all"))
        self.or_text.setText(_translate("viewAllDialog", "or"))
        self.view_specific_pushButton.setText(_translate("viewAllDialog", "view specific"))
        self.search_by_comboBox.setItemText(0, _translate("viewAllDialog", "All"))
        self.search_by_comboBox.setItemText(1, _translate("viewAllDialog", "Username"))
        self.search_by_comboBox.setItemText(2, _translate("viewAllDialog", "e-mail"))
        self.search_by_comboBox.setItemText(3, _translate("viewAllDialog", "App name"))
        self.search_by_comboBox.setItemText(4, _translate("viewAllDialog", "Password"))
        self.search_by_comboBox.setItemText(5, _translate("viewAllDialog", "Creation date"))
        self.view_pushButton.setText(_translate("viewAllDialog", "view"))
        self.search_by_text.setText(_translate("viewAllDialog", "search by:"))
        self.return_pushButton.setText(_translate("viewAllDialog", "return"))
