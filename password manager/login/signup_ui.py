from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signupDialog(object):
    def setupUi(self, signupDialog):
        signupDialog.setObjectName("signupDialog")
        signupDialog.setFixedSize(523, 531)
        signupDialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)    #hide "?" button
        signupDialog.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(85, 170, 255);")
        signupDialog.setWindowIcon(QtGui.QIcon('sources\window_icon.ico'))

        self.signup_text = QtWidgets.QLabel(signupDialog)
        self.signup_text.setGeometry(QtCore.QRect(10, 20, 201, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(32)
        self.signup_text.setFont(font)
        self.signup_text.setObjectName("signup_text")

        self.username_lineEdit = QtWidgets.QLineEdit(signupDialog)
        self.username_lineEdit.setGeometry(QtCore.QRect(20, 160, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setText("")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.username_lineEdit.setFocus()

        self.password_lineEdit = QtWidgets.QLineEdit(signupDialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(20, 250, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setText("")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")

        self.password_lineEdit2 = QtWidgets.QLineEdit(signupDialog)
        self.password_lineEdit2.setGeometry(QtCore.QRect(20, 340, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_lineEdit2.setFont(font)
        self.password_lineEdit2.setText("")
        self.password_lineEdit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit2.setObjectName("password_lineEdit2")

        self.username_text = QtWidgets.QLabel(signupDialog)
        self.username_text.setGeometry(QtCore.QRect(20, 125, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.username_text.setFont(font)
        self.username_text.setObjectName("username_text")

        self.password_text = QtWidgets.QLabel(signupDialog)
        self.password_text.setGeometry(QtCore.QRect(20, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_text.setFont(font)
        self.password_text.setObjectName("password_text")

        self.renterPassword_text = QtWidgets.QLabel(signupDialog)
        self.renterPassword_text.setGeometry(QtCore.QRect(20, 310, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.renterPassword_text.setFont(font)
        self.renterPassword_text.setObjectName("renterPassword_text")

        self.hide_show_password_pushButton = QtWidgets.QPushButton(signupDialog)
        self.hide_show_password_pushButton.setGeometry(QtCore.QRect(430, 260, 31, 28))
        self.hide_show_password_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sources\hide_eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hide_show_password_pushButton.setIcon(icon)
        self.hide_show_password_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.hide_show_password_pushButton.setObjectName("hide_show_password_pushButton")

        self.hide_show_password_pushButton2 = QtWidgets.QPushButton(signupDialog)
        self.hide_show_password_pushButton2.setGeometry(QtCore.QRect(430, 350, 31, 28))
        self.hide_show_password_pushButton2.setText("")
        self.hide_show_password_pushButton2.setIcon(icon)
        self.hide_show_password_pushButton2.setIconSize(QtCore.QSize(25, 25))
        self.hide_show_password_pushButton2.setObjectName("hide_show_password_pushButton2")

        self.signup_pushButton = QtWidgets.QPushButton(signupDialog)
        self.signup_pushButton.setGeometry(QtCore.QRect(20, 440, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.signup_pushButton.setFont(font)
        self.signup_pushButton.setObjectName("signup_pushButton")

        self.feedback_label = QtWidgets.QLabel(signupDialog)
        self.feedback_label.setGeometry(QtCore.QRect(20, 400, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.feedback_label.setFont(font)
        self.feedback_label.setText("")
        self.feedback_label.setObjectName("feedback_label")

        self.line = QtWidgets.QFrame(signupDialog)
        self.line.setGeometry(QtCore.QRect(0, 100, 521, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        #run style function
        self.style()

        self.retranslateUi(signupDialog)
        QtCore.QMetaObject.connectSlotsByName(signupDialog)

    def style(self):
        self.signup_text.setStyleSheet("color: rgb(255, 255, 255); font-weight: bold;")
        self.username_lineEdit.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.password_lineEdit.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.password_lineEdit2.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.hide_show_password_pushButton.setStyleSheet("background-color: rgb(255, 255, 255); border: 0;")
        self.hide_show_password_pushButton2.setStyleSheet("background-color: rgb(255, 255, 255); border: 0;")
        self.signup_pushButton.setStyleSheet("background-color: rgb(55, 170, 55);")
        self.feedback_label.setStyleSheet("color: rgb(220, 0, 0);")

    def retranslateUi(self, signupDialog):
        _translate = QtCore.QCoreApplication.translate
        signupDialog.setWindowTitle(_translate("signupDialog", "PasswordManager - Sign Up"))
        self.signup_text.setText(_translate("signupDialog", "SignUp"))
        self.username_text.setText(_translate("signupDialog", "Username:"))
        self.password_text.setText(_translate("signupDialog", "Password:"))
        self.renterPassword_text.setText(_translate("signupDialog", "Renter password:"))
        self.signup_pushButton.setText(_translate("signupDialog", "signup"))
