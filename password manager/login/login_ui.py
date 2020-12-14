from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_loginWindow(object):
    def __init__(self):
        self.theme = "default"

    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.setFixedSize(494, 528)
        loginWindow.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(85, 170, 255);")
        loginWindow.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        loginWindow.setWindowIcon(QtGui.QIcon('sources\window_icon.ico'))

        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.login_text = QtWidgets.QLabel(self.centralwidget)
        self.login_text.setGeometry(QtCore.QRect(20, 0, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.login_text.setFont(font)
        self.login_text.setObjectName("login_text")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 430, 511, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.username_text = QtWidgets.QLabel(self.centralwidget)
        self.username_text.setGeometry(QtCore.QRect(90, 120, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_text.setFont(font)
        self.username_text.setObjectName("username_text")

        self.login_feedback_label = QtWidgets.QLabel(self.centralwidget)
        self.login_feedback_label.setGeometry(QtCore.QRect(30, 380, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_feedback_label.setFont(font)
        self.login_feedback_label.setText("")
        self.login_feedback_label.setObjectName("login_feedback_label")

        self.login_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.login_pushButton.setGeometry(QtCore.QRect(90, 330, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.login_pushButton.setFont(font)
        self.login_pushButton.setObjectName("login_pushButton")

        self.password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(90, 240, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setText("")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.username_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_lineEdit.setGeometry(QtCore.QRect(90, 150, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setText("")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.username_lineEdit.setFocus()

        self.password_text = QtWidgets.QLabel(self.centralwidget)
        self.password_text.setGeometry(QtCore.QRect(90, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_text.setFont(font)
        self.password_text.setObjectName("password_text")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 90, 491, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.hideShow_password_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.hideShow_password_pushButton.setGeometry(QtCore.QRect(360, 250, 31, 31))
        self.hideShow_password_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"sources\hide_eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hideShow_password_pushButton.setIcon(icon)
        self.hideShow_password_pushButton.setIconSize(QtCore.QSize(23, 20))
        self.hideShow_password_pushButton.setObjectName("hideShow_password_pushButton")

        
        self.createNewAccount_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.createNewAccount_pushButton.setGeometry(QtCore.QRect(90, 450, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.createNewAccount_pushButton.setFont(font)
        self.createNewAccount_pushButton.setObjectName("createNewAccount_pushButton")

        self.statusbar = QtWidgets.QStatusBar(loginWindow)
        self.statusbar.setObjectName("statusbar")

        #run style function
        self.style()

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    
    def style(self):
        self.login_text.setStyleSheet("font-weight: bold;")
        self.login_feedback_label.setStyleSheet("color: rgb(226, 0, 0);")
        self.login_pushButton.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.password_lineEdit.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.username_lineEdit.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.hideShow_password_pushButton.setStyleSheet("background-color: rgb(255, 255, 255); border: 0;")
        self.createNewAccount_pushButton.setStyleSheet("background-color: rgb(55, 170, 55);")


    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Password Manager - Login"))
        self.login_text.setText(_translate("loginWindow", "Login"))
        self.createNewAccount_pushButton.setText(_translate("loginWindow", "Create new account"))
        self.username_text.setText(_translate("loginWindow", "Username:"))
        self.login_pushButton.setText(_translate("loginWindow", "Login"))
        self.password_text.setText(_translate("loginWindow", "Password:"))
