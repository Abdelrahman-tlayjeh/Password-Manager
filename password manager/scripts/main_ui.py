from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(85, 170, 255);")
        MainWindow.setWindowIcon(QtGui.QIcon('sources\window_icon.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.passwordManager_text = QtWidgets.QLabel(self.centralwidget)
        self.passwordManager_text.setGeometry(QtCore.QRect(10, 10, 800, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.passwordManager_text.setFont(font)
        self.passwordManager_text.setObjectName("passwordManager_text")

        self.start_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.start_pushButton.setGeometry(QtCore.QRect(230, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.start_pushButton.setFont(font)
        self.start_pushButton.setObjectName("start_pushButton")

        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(690, 70, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BlkCn BT")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.welcome_label.setFont(font)
        self.welcome_label.setText("")
        self.welcome_label.setObjectName("welcome_label")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 120, 1041, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
#Search section
        self.searchApassword_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.searchApassword_groupBox.setGeometry(QtCore.QRect(0, 130, 1041, 565))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.searchApassword_groupBox.setFont(font)
        self.searchApassword_groupBox.setObjectName("searchApassword_groupBox")

        self.searchBy_text = QtWidgets.QLabel(self.searchApassword_groupBox)
        self.searchBy_text.setGeometry(QtCore.QRect(30, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.searchBy_text.setFont(font)
        self.searchBy_text.setObjectName("searchBy_text")

        self.searchBy_comboBox = QtWidgets.QComboBox(self.searchApassword_groupBox)
        self.searchBy_comboBox.setGeometry(QtCore.QRect(140, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchBy_comboBox.setFont(font)
        self.searchBy_comboBox.setObjectName("searchBy_comboBox")
        self.searchBy_comboBox.addItem("")
        self.searchBy_comboBox.addItem("")
        self.searchBy_comboBox.addItem("")

        self.search_feedback_label = QtWidgets.QLabel(self.searchApassword_groupBox)
        self.search_feedback_label.setGeometry(QtCore.QRect(330, 120, 651, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.search_feedback_label.setFont(font)
        self.search_feedback_label.setStyleSheet("color: rgb(226, 0, 0);")
        self.search_feedback_label.setText("")
        self.search_feedback_label.setObjectName("search_feedback_label")

        self.search_lineEdit = QtWidgets.QLineEdit(self.searchApassword_groupBox)
        self.search_lineEdit.setGeometry(QtCore.QRect(330, 80, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_lineEdit.setFont(font)
        self.search_lineEdit.setText("")
        self.search_lineEdit.setObjectName("search_lineEdit")

        self.search_pushButton = QtWidgets.QPushButton(self.searchApassword_groupBox)
        self.search_pushButton.setGeometry(QtCore.QRect(910, 80, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_pushButton.setFont(font)
        self.search_pushButton.setObjectName("search_pushButton")

#LineEdit of display results
        self.search_result_groupBox = QtWidgets.QGroupBox(self.searchApassword_groupBox)
        self.search_result_groupBox.setGeometry(QtCore.QRect(0, 150, 1041, 411))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.search_result_groupBox.setFont(font)
        self.search_result_groupBox.setTitle("")
        self.search_result_groupBox.setObjectName("search_result_groupBox")

        self.username_lineEdit = QtWidgets.QLineEdit(self.searchApassword_groupBox)
        self.username_lineEdit.setGeometry(QtCore.QRect(10, 230, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setText("")
        self.username_lineEdit.setReadOnly(True)
        self.username_lineEdit.setObjectName("username_lineEdit")

        self.email_lineEdit = QtWidgets.QLineEdit(self.searchApassword_groupBox)
        self.email_lineEdit.setGeometry(QtCore.QRect(10, 340, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setText("")
        self.email_lineEdit.setReadOnly(True)
        self.email_lineEdit.setObjectName("email_lineEdit")

        self.appName_lineEdit = QtWidgets.QLineEdit(self.searchApassword_groupBox)
        self.appName_lineEdit.setGeometry(QtCore.QRect(350, 230, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.appName_lineEdit.setFont(font)
        self.appName_lineEdit.setText("")
        self.appName_lineEdit.setReadOnly(True)
        self.appName_lineEdit.setObjectName("appName_lineEdit")

        self.password_lineEdit = QtWidgets.QLineEdit(self.searchApassword_groupBox)
        self.password_lineEdit.setGeometry(QtCore.QRect(560, 340, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setText("")
        self.password_lineEdit.setReadOnly(True)
        self.password_lineEdit.setObjectName("password_lineEdit")

        self.accountCreationDate_lineEdit = QtWidgets.QLineEdit(self.searchApassword_groupBox)
        self.accountCreationDate_lineEdit.setGeometry(QtCore.QRect(690, 230, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accountCreationDate_lineEdit.setFont(font)
        self.accountCreationDate_lineEdit.setText("")
        self.accountCreationDate_lineEdit.setReadOnly(True)
        self.accountCreationDate_lineEdit.setObjectName("accountCreationDate_lineEdit")
        #Results founds GroupBox and elements
        self.results_found_groupBox = QtWidgets.QGroupBox(self.search_result_groupBox)
        self.results_found_groupBox.setGeometry(QtCore.QRect(-10, 290, 1051, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.results_found_groupBox.setFont(font)
        self.results_found_groupBox.setObjectName("results_found_groupBox")

        self.results_found_lcdScreen = QtWidgets.QLCDNumber(self.results_found_groupBox)
        self.results_found_lcdScreen.setGeometry(QtCore.QRect(30, 50, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.results_found_lcdScreen.setFont(font)
        self.results_found_lcdScreen.setStyleSheet("color: rgb(255, 255, 255);")
        self.results_found_lcdScreen.setObjectName("results_found_lcdScreen")

        self.result_index_lcdScreen = QtWidgets.QLCDNumber(self.results_found_groupBox)
        self.result_index_lcdScreen.setGeometry(QtCore.QRect(430, 50, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result_index_lcdScreen.setFont(font)
        self.result_index_lcdScreen.setStyleSheet("color: rgb(255, 255, 255);")
        self.result_index_lcdScreen.setObjectName("result_index_lcdScreen")

        self.next_pushButton = QtWidgets.QPushButton(self.results_found_groupBox)
        self.next_pushButton.setGeometry(QtCore.QRect(530, 50, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("background-color: rgb(85, 85, 255); color: rgb(255, 255, 255); border: 10px solid rgb(0, 0, 0)")
        self.next_pushButton.setObjectName("next_pushButton")

        self.prev_pushButton = QtWidgets.QPushButton(self.results_found_groupBox)
        self.prev_pushButton.setGeometry(QtCore.QRect(342, 50, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.prev_pushButton.setFont(font)
        self.prev_pushButton.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(85, 85, 255);")
        self.prev_pushButton.setObjectName("prev_pushButton")

        #some text (labels)
        self.username_text = QtWidgets.QLabel(self.searchApassword_groupBox)
        self.username_text.setGeometry(QtCore.QRect(10, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_text.setFont(font)
        self.username_text.setObjectName("username_text")
        self.appName_text = QtWidgets.QLabel(self.searchApassword_groupBox)
        self.appName_text.setGeometry(QtCore.QRect(350, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.appName_text.setFont(font)
        self.appName_text.setObjectName("appName_text")
        self.password_text = QtWidgets.QLabel(self.searchApassword_groupBox)
        self.password_text.setGeometry(QtCore.QRect(560, 310, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_text.setFont(font)
        self.password_text.setObjectName("password_text")
        self.eMail_text = QtWidgets.QLabel(self.searchApassword_groupBox)
        self.eMail_text.setGeometry(QtCore.QRect(10, 310, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eMail_text.setFont(font)
        self.eMail_text.setObjectName("eMail_text")
        self.accountCreationDate_text = QtWidgets.QLabel(self.searchApassword_groupBox)
        self.accountCreationDate_text.setGeometry(QtCore.QRect(690, 200, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accountCreationDate_text.setFont(font)
        self.accountCreationDate_text.setObjectName("accountCreationDate_text")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1208, 40))
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setStyleSheet("background-color: rgb(0, 255, 255); color: rgb(0, 0, 0);")
        MainWindow.setMenuBar(self.menuBar)

        self.addModifyInfo_action = QtWidgets.QAction(self.menuBar)
        self.controlPanel_action = QtWidgets.QAction(self.menuBar)

        self.menuBar.addAction(self.addModifyInfo_action)
        self.menuBar.addAction(self.controlPanel_action)

        #run style function
        self.style()
        
        #all lineEdits that display results
        self.lineEdit_lst = [self.username_lineEdit, self.email_lineEdit, self.appName_lineEdit, self.password_lineEdit, self.accountCreationDate_lineEdit]

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #setup elements order
        MainWindow.setTabOrder(self.start_pushButton, self.search_lineEdit)
        MainWindow.setTabOrder(self.search_lineEdit, self.searchBy_comboBox)
        MainWindow.setTabOrder(self.searchBy_comboBox, self.search_pushButton)
        MainWindow.setTabOrder(self.search_pushButton, self.username_lineEdit)
        MainWindow.setTabOrder(self.username_lineEdit, self.appName_lineEdit)
        MainWindow.setTabOrder(self.appName_lineEdit, self.accountCreationDate_lineEdit)
        MainWindow.setTabOrder(self.accountCreationDate_lineEdit, self.email_lineEdit)
        MainWindow.setTabOrder(self.email_lineEdit, self.password_lineEdit)
        MainWindow.setTabOrder(self.password_lineEdit, self.prev_pushButton)
        MainWindow.setTabOrder(self.prev_pushButton, self.next_pushButton)

    def style(self):
        self.passwordManager_text.setStyleSheet("font: 81 30pt \"Rockwell Extra Bold\"; font-weight: bold;")
        self.start_pushButton.setStyleSheet("background-color: rgb(55, 170, 55);")
        self.welcome_label.setStyleSheet("color: rgb(255, 255, 255); font-weight: bold;")
        self.searchBy_comboBox.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255)")
        self.search_lineEdit.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.search_pushButton.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.username_lineEdit.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.email_lineEdit.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.appName_lineEdit.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.password_lineEdit.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.accountCreationDate_lineEdit.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.next_pushButton.setStyleSheet("background-color: rgb(55, 170, 55);")
        self.prev_pushButton.setStyleSheet("background-color: rgb(55, 170, 55);")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager - Main"))
        self.passwordManager_text.setText(_translate("MainWindow", "Password Manager"))
        self.start_pushButton.setText(_translate("MainWindow", "Login"))
        self.searchApassword_groupBox.setTitle(_translate("MainWindow", "Search a Password"))
        self.searchBy_comboBox.setItemText(0, _translate("MainWindow", "Username"))
        self.searchBy_comboBox.setItemText(1, _translate("MainWindow", "e-mail"))
        self.searchBy_comboBox.setItemText(2, _translate("MainWindow", "App name"))
        self.searchBy_text.setText(_translate("MainWindow", "search by"))
        self.search_pushButton.setText(_translate("MainWindow", "Search"))
        self.results_found_groupBox.setTitle(_translate("MainWindow", "Results Found:"))
        self.next_pushButton.setText(_translate("MainWindow", "Next"))
        self.prev_pushButton.setText(_translate("MainWindow", "Prev."))
        self.username_text.setText(_translate("MainWindow", "Username:"))
        self.appName_text.setText(_translate("MainWindow", "App Name:"))
        self.password_text.setText(_translate("MainWindow", "Password:"))
        self.eMail_text.setText(_translate("MainWindow", "E-Mail:"))
        self.accountCreationDate_text.setText(_translate("MainWindow", "Account Creation date:"))
        self.addModifyInfo_action.setText(_translate("MainWindow", "add a password"))
        self.controlPanel_action.setText(_translate("MainWindow", "control panel"))
