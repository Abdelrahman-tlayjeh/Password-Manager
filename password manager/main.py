from PyQt5 import QtWidgets
from scripts.main_ui import Ui_MainWindow
from login import login_script
from database import database_script
from scripts import search_scipt, inf
from addPassword import addPassword_script
from controlPanel import controlPanel_script
import sys


#setUp UI
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

#run program
def run_passwordManager():
    disable_main() 
    MainWindow.show()
    if not login_script.isLogin:
        open_login()
    sys.exit(app.exec_())
    

#<-----------------------functions used befor login------------------------------------------------------->

#hide search panel and resize window(window before login)
def disable_main():
    ui.passwordManager_text.setText("Please login to continue.")
    MainWindow.setFixedSize(800, 160)
    ui.searchApassword_groupBox.hide()
    ui.menuBar.hide()

#open login window and hide main window until login window is closed
def open_login():
    MainWindow.hide()
    login_script.run()
    if login_script.isLogin:
        enable_main()
    if inf.attemptsEnds:
        sys.exit(app.exit())
    MainWindow.show()

#<----------------functions used after successful login-------------------------------------------------------->

#helper: used after successful login with enable_main()
def resizeAndCenter(): 
    MainWindow.setFixedSize(1035, 734)  #resize window
    #center the window
    window = MainWindow.frameGeometry()
    screenCenter = QtWidgets.QDesktopWidget().availableGeometry().center()  #get screen center
    window.moveCenter(screenCenter)
    MainWindow.move(window.topLeft())

#show search panel and adjust size(window after login)
def enable_main():  
    resizeAndCenter()
    ui.start_pushButton.hide()
    ui.passwordManager_text.setText("Password Manager")
    ui.welcome_label.setText(f"Welcome {login_script.ui.username_lineEdit.text()}.")
    ui.menuBar.show()
    ui.searchApassword_groupBox.show()
    ui.results_found_groupBox.hide()


#<-------------------------------------search functions--------------------------------------------->
    
#functions used to enable/disable next and prev buttons
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

#reset whole main window
def reset_window():
    ui.search_lineEdit.clear()
    clear_display()

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

#----------------------------functions that open menu bar actions------------------------------------------->

#run (add password) dialog and reset main window
def open_add_password():
    MainWindow.hide()
    addPassword_script.run()
    reset_window()
    MainWindow.show()

# run control panel dialog

#helper (used in recursion): open control panel then execute reOpen_or_close_panel() after closing panel
def run_control_panel():
    controlPanel_script.run()
    reOpen_or_close_panel()

#helper (used in recursion): sheck if reopen control panel is needed, if yes: run_control_panel(), if not: show MainWindow
def reOpen_or_close_panel():
    if inf.reOpenControlPanel:
        run_control_panel()
    else:
        reset_window()
        MainWindow.show()

#main function to open control panel window
def open_control_panel():
    MainWindow.hide()
    run_control_panel()


#setup buttons
ui.start_pushButton.clicked.connect(open_login)
ui.search_pushButton.clicked.connect(search_info)
ui.next_pushButton.clicked.connect(next_result)
ui.prev_pushButton.clicked.connect(prev_result)

#setup menuBar actions
ui.addModifyInfo_action.triggered.connect(open_add_password)
ui.controlPanel_action.triggered.connect(open_control_panel)


#run the script
run_passwordManager()
