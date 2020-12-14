from PyQt5 import QtWidgets
from login.login_ui import Ui_loginWindow
from login import signup_script
from database import database_script
from scripts import inf
import sys

#setup UI
App = QtWidgets.QApplication(sys.argv)
loginDialog = QtWidgets.QDialog()
ui = Ui_loginWindow()
ui.setupUi(loginDialog)

attempts = 3

isLogin = False
passwordIsHidden = True

#functions
def run():
    loginDialog.exec_()
    loginDialog.close()

#exit the app if attempts finished
def forceStop():
    inf.attemptsEnds = True
    loginDialog.close()

#main login function
def try_login():
    global attempts, isLogin, UserName, password
    entered_usn = ui.username_lineEdit.text()
    entered_pswd = ui.password_lineEdit.text()

    result = database_script.search_user(entered_usn)

    if result and result[1 :3] == (entered_usn, entered_pswd):
        isLogin = True
        #save username and password in inf.py 
        inf.Username = entered_usn
        inf.password = entered_pswd
        close()
    else:
        attempts -= 1
        forceStop() if not attempts else ui.login_feedback_label.setText(f"incorrect username or password! {attempts} attempt(s)...")

#hide/show entered password
def hide_show_password():
    global passwordIsHidden
    if passwordIsHidden:
        ui.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        passwordIsHidden = False
    else:
        ui.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        passwordIsHidden = True

#open signup window
def open_signup():
    signup_script.run()
    ui.username_lineEdit.clear()
    ui.password_lineEdit.clear()
    ui.login_feedback_label.clear()

#close login window
def close():
    loginDialog.close()


#setup Buttons
ui.login_pushButton.clicked.connect(try_login)
ui.hideShow_password_pushButton.clicked.connect(hide_show_password)
ui.createNewAccount_pushButton.clicked.connect(open_signup)