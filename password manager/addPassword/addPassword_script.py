from addPassword.add_password_ui import Ui_addPasswordDialog
from PyQt5 import QtWidgets, QtCore
from database.database_script import add_info
from scripts import inf
from datetime import date
import sys

#setup UI
app = QtWidgets.QApplication(sys.argv)
addPasswordDialog = QtWidgets.QDialog()
ui = Ui_addPasswordDialog()
ui.setupUi(addPasswordDialog)

#some vars
isSaved = False
isDateDisable = False

def run():
    set_dateEdit()
    addPasswordDialog.exec_()
    addPasswordDialog.close()
    #clear all lineEdits and reset dateEdit when closing
    clear()     
    if isDateDisable:
        enable_disable_date()

#helper: change all "" elements of list to "-"
def removeEmpty(lst):
    lst_without_empty = []
    for elem in lst:
        if not elem.strip():
            lst_without_empty.append("-")
        else:
            lst_without_empty.append(elem)
    return lst_without_empty

#save informations in user info database
def save_info():
    global isSaved
    if not isSaved:
        entered_usn = ui.username_lineEdit.text()
        entered_email = ui.email_lineEdit.text()
        entered_appname = ui.appName_lineEdit.text()
        entered_pass = ui.password_lineEdit.text()
        entered_date = "" if isDateDisable else ui.creation_date_dateEdit.text()

        #check if at least one of (username, email, app name) and password is entered
        if any([entered_usn, entered_email, entered_appname]) and entered_pass:
            usn, email, appname, pswd, date = removeEmpty([entered_usn, entered_email, entered_appname,entered_pass, entered_date])
            add_info(inf.Username, usn, email, appname, pswd, date)
            ui.feedback_label.setStyleSheet("color: rgb(69, 138, 0);")
            ui.feedback_label.setText("Successfuly Saved!")
            isSaved = True
            ui.clear_pushButton.show()
        else:
            ui.feedback_label.setStyleSheet("color: rgb(226, 0, 0);")
            ui.feedback_label.setText("Please enter at least one of (username, e-mail, app name) and a password.")

#clear all lineEdits and hide clear button 
def clear():
    global isSaved
    for scr in [ui.username_lineEdit, ui.email_lineEdit, ui.appName_lineEdit, ui.password_lineEdit, ui.feedback_label]:
        scr.setText("")
    isSaved = False
    ui.clear_pushButton.hide()

#helper: set date & max date = today date
def set_dateEdit():
    ui.creation_date_dateEdit.setDate(QtCore.QDate.currentDate())
    ui.creation_date_dateEdit.setMaximumDate(QtCore.QDate.currentDate())
    
#enable/disable date dateEdit
def enable_disable_date():
    global isDateDisable
    #enable
    if isDateDisable:
        ui.creation_date_dateEdit.setDisabled(False)
        ui.enable_disable_dare_pushButton.setText("X")
        ui.creation_date_dateEdit.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        ui.enable_disable_dare_pushButton.setStyleSheet("background-color: rgb(226, 0, 0);")
        isDateDisable = False
    #disable
    else:
        ui.creation_date_dateEdit.setDisabled(True)
        ui.enable_disable_dare_pushButton.setText("✔️")
        ui.creation_date_dateEdit.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0, 0, 0);")
        ui.enable_disable_dare_pushButton.setStyleSheet("background-color: rgb(55, 170, 55);")
        isDateDisable = True

#close dialog, clear all info and back to main window
def back_to_main():
    addPasswordDialog.close()


#setup buttons
ui.save_pushButton.clicked.connect(save_info)
ui.clear_pushButton.clicked.connect(clear)
ui.return_pushButton.clicked.connect(back_to_main)
ui.enable_disable_dare_pushButton.clicked.connect(enable_disable_date)