from PyQt5 import QtWidgets
from controlPanel.clear_data.clear_all_data_ui import Ui_clearAllDataDialog
from database import database_script
from scripts import inf
import time
import sys

#setup UI
app = QtWidgets.QApplication(sys.argv)
clearAllDataDialog = QtWidgets.QDialog()
ui = Ui_clearAllDataDialog()
ui.setupUi(clearAllDataDialog)

isPasswordHidden = True

def run():
    clearAllDataDialog.exec_()
    enable_login()
    clearAllDataDialog.close()

#show login confirmation (after pressing continue button)
def continue_to_clear():
    ui.attention_groupBox.hide()
    ui.main_groupBox.show()
    ui.clear_all_data_pushButton.hide()

#before successful login confirmation
def enable_login():
    for elem in (ui.username_lineEdit, ui.password_lineEdit):
        elem.setDisabled(False)
        elem.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
    ui.sheck_pushButton.setDisabled(False)
    ui.sheck_pushButton.setStyleSheet("background-color: rgb(85, 85, 255); border: solid rgb(0, 0, 0);")
    ui.login_feedback_label.clear()

#after successful login confirmation
def disable_login():
    for elem in (ui.username_lineEdit, ui.password_lineEdit, ui.sheck_pushButton):
        elem.setDisabled(True)
        elem.setStyleSheet("background-color: rgb(0, 0, 0);")

#confirm login to go to the final step
def confirm_login():
    ui.login_feedback_label.clear()
    if ui.username_lineEdit.text() == inf.Username and ui.password_lineEdit.text() == inf.password:
        ui.login_feedback_label.setStyleSheet("color: rgb(0, 134, 0);")
        ui.login_feedback_label.setText("Login Confirmed...")
        disable_login()
        ui.clear_all_data_pushButton.show()
    else:
        ui.login_feedback_label.setStyleSheet("color: rgb(170, 0, 0);")
        ui.login_feedback_label.setText("Incorrect Username or Password...")
    
#clear all data and close window
def clear_all_data():
    ui.clear_data_feedback_label.setText("Done!")
    database_script.clear_user_info(inf.Username)
    time.sleep(2)
    clearAllDataDialog.close()

#hide/show password
def hide_show_password():
    global isPasswordHidden
    if isPasswordHidden:
        ui.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        isPasswordHidden = False
    else:
        ui.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        isPasswordHidden = True
    

#setup buttons
ui.continue_pushButton.clicked.connect(continue_to_clear)
ui.sheck_pushButton.clicked.connect(confirm_login)
ui.clear_all_data_pushButton.clicked.connect(clear_all_data)
ui.hide_show_password_pushButton.clicked.connect(hide_show_password)