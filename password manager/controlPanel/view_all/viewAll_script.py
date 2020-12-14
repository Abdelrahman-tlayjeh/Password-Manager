from PyQt5 import QtWidgets
from controlPanel.view_all.view_all_ui import Ui_viewAllDialog
from database import database_script
from scripts import search_scipt, inf
import sys

#setup UI
app = QtWidgets.QApplication(sys.argv)
viewAllDialog = QtWidgets.QDialog()
ui = Ui_viewAllDialog()
ui.setupUi(viewAllDialog)


def run():
    viewAllDialog.exec_()
    viewAllDialog.close()


#helper: display results from list to results screen
def display_result(result_lst):
    if result_lst:
        for result in result_lst:
            idKey, usn, email, appname, pswd, date = result
            ui.results_textBrowser.append(f"{idKey}__'{usn}'__'{email}'__'{appname}'__'{pswd}'__'{date}'")
            ui.results_textBrowser.append("-"*150)
        ui.results_textBrowser.append("-"*150)
        ui.results_textBrowser.append("End of Results...")
        #scroll to the top
        vert_scroll = ui.results_textBrowser.verticalScrollBar()
        vert_scroll.setValue(0)
    else:
        ui.results_textBrowser.append("No Results Found!")

#search all and display results
def view_all():
    #style
    ui.results_textBrowser.clear()
    ui.view_all_pushButton.setStyleSheet("background-color: rgb(85, 85, 255);")
    ui.search_groupBox.hide()
    ui.view_specific_pushButton.setStyleSheet("background-color: rgb(0, 0, 0);")
    results = database_script.return_all_info(inf.Username)
    display_result(results)

#show specific search items
def specific_view():
    ui.results_textBrowser.clear()
    ui.view_specific_pushButton.setStyleSheet("background-color: rgb(85, 85, 255);")
    ui.search_groupBox.show()
    ui.view_all_pushButton.setStyleSheet("background-color: rgb(0, 0, 0);")

#search specific and display results
def search_and_view_specific():
    ui.results_textBrowser.clear()
    if  ui.search_by_comboBox.currentText() == "All":
        results = search_scipt.search_by_keyWord(inf.Username, ui.search_lineEdit.text())
        display_result(results)
        
    else:
        results = search_scipt.search(inf.Username, ui.search_by_comboBox.currentText(), ui.search_lineEdit.text(), return_all=True)
        display_result(results)

#reset everything
def reset():
    ui.results_textBrowser.clear()
    ui.view_specific_pushButton.setStyleSheet("background-color: rgb(85, 85, 255);")
    ui.view_all_pushButton.setStyleSheet("background-color: rgb(85, 85, 255);")
    ui.search_by_comboBox.setCurrentText("All")
    ui.search_lineEdit.clear()
    ui.search_groupBox.hide()


#close dialog and reset
def back_to_main():
    viewAllDialog.close()
    reset()


#setup buttons
ui.view_all_pushButton.clicked.connect(view_all)
ui.view_specific_pushButton.clicked.connect(specific_view)
ui.return_pushButton.clicked.connect(back_to_main)
ui.view_pushButton.clicked.connect(search_and_view_specific)