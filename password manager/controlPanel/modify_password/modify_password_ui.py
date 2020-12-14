from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modifyPassword(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1064, 720)
        Dialog.setStyleSheet("background-color: rgb(85, 170, 255);")
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        Dialog.setWindowIcon(QtGui.QIcon('sources\window_icon.ico'))

        self.search_groupBox = QtWidgets.QGroupBox(Dialog)
        self.search_groupBox.setGeometry(QtCore.QRect(10, 10, 1041, 161))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.search_groupBox.setFont(font)
        self.search_groupBox.setObjectName("search_groupBox")

        self.searchBy_comboBox = QtWidgets.QComboBox(self.search_groupBox)
        self.searchBy_comboBox.setGeometry(QtCore.QRect(140, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchBy_comboBox.setFont(font)
        self.searchBy_comboBox.setObjectName("searchBy_comboBox")
        self.searchBy_comboBox.addItem("")
        self.searchBy_comboBox.addItem("")
        self.searchBy_comboBox.addItem("")

        self.searchBy_text = QtWidgets.QLabel(self.search_groupBox)
        self.searchBy_text.setGeometry(QtCore.QRect(30, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.searchBy_text.setFont(font)
        self.searchBy_text.setObjectName("searchBy_text")

        self.search_pushButton = QtWidgets.QPushButton(self.search_groupBox)
        self.search_pushButton.setGeometry(QtCore.QRect(910, 80, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_pushButton.setFont(font)
        self.search_pushButton.setObjectName("search_pushButton")

        self.search_feedback_label = QtWidgets.QLabel(self.search_groupBox)
        self.search_feedback_label.setGeometry(QtCore.QRect(330, 135, 651, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.search_feedback_label.setFont(font)
        self.search_feedback_label.setText("")
        self.search_feedback_label.setObjectName("search_feedback_label")

        self.search_lineEdit = QtWidgets.QLineEdit(self.search_groupBox)
        self.search_lineEdit.setGeometry(QtCore.QRect(330, 80, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_lineEdit.setFont(font)
        self.search_lineEdit.setText("")
        self.search_lineEdit.setObjectName("search_lineEdit")

        self.feedback_label = QtWidgets.QLabel(self.search_groupBox)
        self.feedback_label.setGeometry(QtCore.QRect(330, 120, 551, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.feedback_label.setFont(font)
        self.feedback_label.setText("")
        self.feedback_label.setObjectName("feedback_label")

        self.results_found_groupBox = QtWidgets.QGroupBox(Dialog)
        self.results_found_groupBox.setGeometry(QtCore.QRect(10, 500, 1051, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.results_found_groupBox.setFont(font)
        self.results_found_groupBox.setObjectName("results_found_groupBox")

        self.next_pushButton = QtWidgets.QPushButton(self.results_found_groupBox)
        self.next_pushButton.setGeometry(QtCore.QRect(530, 50, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setObjectName("next_pushButton")

        self.prev_pushButton = QtWidgets.QPushButton(self.results_found_groupBox)
        self.prev_pushButton.setGeometry(QtCore.QRect(342, 50, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.prev_pushButton.setFont(font)
        self.prev_pushButton.setObjectName("prev_pushButton")

        self.result_index_lcdScreen = QtWidgets.QLCDNumber(self.results_found_groupBox)
        self.result_index_lcdScreen.setGeometry(QtCore.QRect(430, 50, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result_index_lcdScreen.setFont(font)
        self.result_index_lcdScreen.setObjectName("result_index_lcdScreen")

        self.results_found_lcdScreen = QtWidgets.QLCDNumber(self.results_found_groupBox)
        self.results_found_lcdScreen.setGeometry(QtCore.QRect(30, 50, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.results_found_lcdScreen.setFont(font)
        self.results_found_lcdScreen.setObjectName("results_found_lcdScreen")

        self.search_result_groupBox = QtWidgets.QGroupBox(Dialog)
        self.search_result_groupBox.setGeometry(QtCore.QRect(10, 170, 1041, 311))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.search_result_groupBox.setFont(font)
        self.search_result_groupBox.setTitle("")
        self.search_result_groupBox.setObjectName("search_result_groupBox")

        self.username_text = QtWidgets.QLabel(self.search_result_groupBox)
        self.username_text.setGeometry(QtCore.QRect(10, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_text.setFont(font)
        self.username_text.setObjectName("username_text")

        self.username_lineEdit = QtWidgets.QLineEdit(self.search_result_groupBox)
        self.username_lineEdit.setGeometry(QtCore.QRect(10, 70, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setText("")
        self.username_lineEdit.setReadOnly(False)
        self.username_lineEdit.setObjectName("username_lineEdit")

        self.accountCreationDate_lineEdit = QtWidgets.QLineEdit(self.search_result_groupBox)
        self.accountCreationDate_lineEdit.setGeometry(QtCore.QRect(690, 70, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accountCreationDate_lineEdit.setFont(font)
        self.accountCreationDate_lineEdit.setText("")
        self.accountCreationDate_lineEdit.setReadOnly(True)
        self.accountCreationDate_lineEdit.setObjectName("accountCreationDate_lineEdit")

        self.password_text = QtWidgets.QLabel(self.search_result_groupBox)
        self.password_text.setGeometry(QtCore.QRect(560, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_text.setFont(font)
        self.password_text.setObjectName("password_text")

        self.appName_text = QtWidgets.QLabel(self.search_result_groupBox)
        self.appName_text.setGeometry(QtCore.QRect(350, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.appName_text.setFont(font)
        self.appName_text.setObjectName("appName_text")

        self.password_lineEdit = QtWidgets.QLineEdit(self.search_result_groupBox)
        self.password_lineEdit.setGeometry(QtCore.QRect(560, 180, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setText("")
        self.password_lineEdit.setReadOnly(False)
        self.password_lineEdit.setObjectName("password_lineEdit")

        self.appName_lineEdit = QtWidgets.QLineEdit(self.search_result_groupBox)
        self.appName_lineEdit.setGeometry(QtCore.QRect(350, 70, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.appName_lineEdit.setFont(font)
        self.appName_lineEdit.setText("")
        self.appName_lineEdit.setReadOnly(False)
        self.appName_lineEdit.setObjectName("appName_lineEdit")

        self.eMail_text = QtWidgets.QLabel(self.search_result_groupBox)
        self.eMail_text.setGeometry(QtCore.QRect(10, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eMail_text.setFont(font)
        self.eMail_text.setObjectName("eMail_text")

        self.email_lineEdit = QtWidgets.QLineEdit(self.search_result_groupBox)
        self.email_lineEdit.setGeometry(QtCore.QRect(10, 180, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setText("")
        self.email_lineEdit.setReadOnly(False)
        self.email_lineEdit.setObjectName("email_lineEdit")
        
        self.accountCreationDate_text = QtWidgets.QLabel(self.search_result_groupBox)
        self.accountCreationDate_text.setGeometry(QtCore.QRect(690, 40, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accountCreationDate_text.setFont(font)
        self.accountCreationDate_text.setObjectName("accountCreationDate_text")
        
        self.save_pushButton = QtWidgets.QPushButton(self.search_result_groupBox)
        self.save_pushButton.setGeometry(QtCore.QRect(140, 260, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.save_pushButton.setFont(font)
        self.save_pushButton.setObjectName("save_pushButton")

        self.delete_pushButton = QtWidgets.QPushButton(self.search_result_groupBox)
        self.delete_pushButton.setGeometry(QtCore.QRect(250, 260, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.delete_pushButton.setFont(font)
        self.delete_pushButton.setObjectName("delete_pushButton")

        font = QtGui.QFont()
        font.setPointSize(14)

        self.return_pushButton = QtWidgets.QPushButton(Dialog)
        self.return_pushButton.setGeometry(QtCore.QRect(10, 670, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.return_pushButton.setFont(font)
        self.return_pushButton.setObjectName("return_pushButton")

        self.lineEdit_lst = [self.username_lineEdit, self.email_lineEdit, self.appName_lineEdit, self.password_lineEdit, self.accountCreationDate_lineEdit]

        #run style function
        self.style()
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def style(self):
        self.search_groupBox.setStyleSheet("background-color: rgb(85, 170, 255); color: rgb(255, 255, 255);")
        self.searchBy_comboBox.setStyleSheet("color: rgb(0, 0, 0);  background-color: rgb(255, 255, 255);")
        self.search_pushButton.setStyleSheet("background-color: rgb(85, 85, 255); color: rgb(255, 255, 255);")
        self.search_feedback_label.setStyleSheet("color: rgb(234, 0, 0);")
        self.search_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.feedback_label.setStyleSheet("color: rgb(206, 0, 0);")
        self.next_pushButton.setStyleSheet("background-color: rgb(85, 85, 255); color: rgb(255, 255, 255);")
        self.prev_pushButton.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(85, 85, 255);")
        self.result_index_lcdScreen.setStyleSheet("color: rgb(0, 0, 0);")
        self.results_found_lcdScreen.setStyleSheet("background-color: rgb(85, 170, 255); color: rgb(0, 0, 0);")
        self.username_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.accountCreationDate_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.password_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.appName_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.email_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.save_pushButton.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 132, 97);")
        self.delete_pushButton.setStyleSheet("color: rgb(255, 255, 255);  background-color: rgb(212, 0, 0);")
        self.return_pushButton.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(85, 85, 255);")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Control Panel - Modify Passwords"))
        self.search_groupBox.setTitle(_translate("Dialog", "Search a Password"))
        self.searchBy_comboBox.setItemText(0, _translate("Dialog", "Username"))
        self.searchBy_comboBox.setItemText(1, _translate("Dialog", "e-mail"))
        self.searchBy_comboBox.setItemText(2, _translate("Dialog", "App name"))
        self.searchBy_text.setText(_translate("Dialog", "search by"))
        self.search_pushButton.setText(_translate("Dialog", "Search"))
        self.results_found_groupBox.setTitle(_translate("Dialog", "Results Found:"))
        self.next_pushButton.setText(_translate("Dialog", "Next"))
        self.prev_pushButton.setText(_translate("Dialog", "Prev."))
        self.username_text.setText(_translate("Dialog", "Username:"))
        self.password_text.setText(_translate("Dialog", "Password:"))
        self.appName_text.setText(_translate("Dialog", "App Name:"))
        self.eMail_text.setText(_translate("Dialog", "E-Mail:"))
        self.accountCreationDate_text.setText(_translate("Dialog", "Account Creation date:"))
        self.save_pushButton.setText(_translate("Dialog", "Save"))
        self.delete_pushButton.setText(_translate("Dialog", "delete"))
        self.return_pushButton.setText(_translate("Dialog", "return"))
