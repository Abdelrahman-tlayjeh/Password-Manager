from PyQt5 import QtWidgets
from controlPanel.modify_password.modify_password_ui import Ui_modifyPassword
from scripts import search_scipt
from scripts import inf
from database import database_script
from addPassword.addPassword_script import removeEmpty
import sys


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_modifyPassword()
ui.setupUi(Dialog)

def run():
    Dialog.exec_()
    Dialog.close()

#search functions---------------------------------------------------------->

def enable_next_button():
    ui.next_pushButton.setDisabled(False)
    ui.next_pushButton.setStyleSheet("background-color: rgb(55, 170, 55);")
def disable_next_button():
    ui.next_pushButton.setDisabled(True)
    ui.next_pushButton.setStyleSheet("background-color: rgb(0, 0, 0);")
def enable_prev_button():
    ui.prev_pushButton.setDisabled(False)
    ui.prev_pushButton.setStyleSheet("background-color: rgb(55, 170, 55);")
def disable_prev_button():
    ui.prev_pushButton.setDisabled(True)
    ui.prev_pushButton.setStyleSheet("background-color: rgb(0, 0, 0);")

#reset result section
def clear_display():
    ui.results_found_groupBox.show()
    for scr in ui.lineEdit_lst:
        scr.clear()
    ui.search_feedback_label.clear()
    ui.results_found_lcdScreen.display(0)
    ui.result_index_lcdScreen.display(0)
    disable_next_button()
    disable_prev_button()

#update the result shown in lineEdits and sheck if (next, prev) buttons are required or not
def update_display(index, result_lst):
    ui.result_index_lcdScreen.display(index + 1)
    for scr, inf in zip(ui.lineEdit_lst, result_lst[index]):
        scr.clear()
        scr.setText(inf)
    #enable/disable next, prev buttons
    if index > 0:
        enable_prev_button()
    if index == 0:
        disable_prev_button()
    if index < len(results) - 1:
        enable_next_button()
    if index == len(results) - 1:
        disable_next_button()

#search for information
def search_info():
    clear_display()
    global results      #list contain all results as list// e.g: results[[result1], [result2], ...]
    results = search_scipt.search(inf.Username, ui.searchBy_comboBox.currentText(), ui.search_lineEdit.text())
    if not results:
        ui.search_feedback_label.setText("No results found!")
    else:
        global index    #index of shown result
        index = 0       
        ui.results_found_lcdScreen.display(len(results))    #nb of all results
        update_display(index, results)

#switch to the next result and update_display()
def next_result():
    global index, results
    index += 1
    update_display(index, results)

#switch to the previous result and update_display()
def prev_result():
    global index, results
    index -= 1
    update_display(index, results)

#delete & save changes functions-------------------------------->

#delete selected info
def delete():
    info_lst = [elem.text() for elem in ui.lineEdit_lst]
    if all(info_lst):
        database_script.delete_info(inf.Username, info_lst)
        search_info()

#save changes
def save_changes():
    old_info_lst = results[index]
    new_info_lst = [elem.text() for elem in ui.lineEdit_lst]
    if all(new_info_lst):
        database_script.update_info(inf.Username, old_info_lst, new_info_lst)
        search_info()


#close and reset window 
def back_to_main():
    Dialog.close()
    clear_display()


#setup buttons
ui.search_pushButton.clicked.connect(search_info)
ui.next_pushButton.clicked.connect(next_result)
ui.prev_pushButton.clicked.connect(prev_result)

ui.save_pushButton.clicked.connect(save_changes)
ui.delete_pushButton.clicked.connect(delete)

ui.return_pushButton.clicked.connect(back_to_main)