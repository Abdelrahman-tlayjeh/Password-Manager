from login.signup_ui import Ui_signupDialog
from PyQt5 import QtWidgets
from database import database_script
import sys

#setup UI
app = QtWidgets.QApplication(sys.argv)
signupDialog = QtWidgets.QDialog()
ui = Ui_signupDialog()
ui.setupUi(signupDialog)

isPass1Hidden = True
isPass2Hidden = True


def run():
    signupDialog.exec_()
    signupDialog.close()


def signup():
    ui.feedback_label.setText("")

    entered_username = ui.username_lineEdit.text()
    entered_password1 = ui.password_lineEdit.text()
    entered_password2 = ui.password_lineEdit2.text()
    
    try:
        #check if there are input in each username and password lineEdit
        if entered_username and entered_password1:
            #check if the entered username is available
            if database_script.isUsernameAvailable(entered_username):
                #check if entered passwords (1 & 2) are the same
                if entered_password1 == entered_password2:
                    database_script.add_user(entered_username, entered_password1)
                    signupDialog.close()
                else:
                    ui.feedback_label.setText("Entered Passwords are differents!")
            else:
                ui.feedback_label.setText(f"'{entered_username}' is used! Please use another one...")
        else:
            ui.feedback_label.setText("Plese enter a username and a password!")
    #if entered username contain space
    except:
        ui.feedback_label.setText("Username cannot contains spaces!")
        ui.username_lineEdit.clear()
        ui.password_lineEdit.clear()
        ui.password_lineEdit2.clear()

#show/hide password 1
def hide_show_password1():
    global isPass1Hidden
    if isPass1Hidden:
        ui.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        isPass1Hidden = False
    else:
        ui.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        isPass1Hidden = True
#show/hide password 2
def hide_show_password2():
    global isPass2Hidden
    if isPass2Hidden:
        ui.password_lineEdit2.setEchoMode(QtWidgets.QLineEdit.Normal)
        isPass2Hidden = False
    else:
        ui.password_lineEdit2.setEchoMode(QtWidgets.QLineEdit.Password)
        isPass2Hidden = True

#buttons
ui.signup_pushButton.clicked.connect(signup)
ui.hide_show_password_pushButton.clicked.connect(hide_show_password1)
ui.hide_show_password_pushButton2.clicked.connect(hide_show_password2)