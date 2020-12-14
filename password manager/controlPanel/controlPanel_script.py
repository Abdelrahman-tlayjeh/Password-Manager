from PyQt5 import QtWidgets
from controlPanel.control_panel_ui import Ui_controlDialog
from controlPanel.modify_password import modify_password_script
from controlPanel.view_all import viewAll_script
from controlPanel.clear_data import clearAllData_script
from scripts import inf
import sys

#setup ui
app = QtWidgets.QApplication(sys.argv)
controlDialog = QtWidgets.QDialog()
ui = Ui_controlDialog()
ui.setupUi(controlDialog)


def run():
    inf.reOpenControlPanel = False
    controlDialog.exec_()
    controlDialog.close()

#close dialog
def back_to_main():
    controlDialog.close()

def open_modify_password():
    inf.reOpenControlPanel = True
    controlDialog.close()
    modify_password_script.run()

def open_view_all():
    inf.reOpenControlPanel = True
    controlDialog.close()
    viewAll_script.run()

def open_clear_data():
    inf.reOpenControlPanel = True
    controlDialog.close()
    clearAllData_script.run()
    
#setup buttons
ui.change_delete_commandLinkButton.clicked.connect(open_modify_password)
ui.view_all_commandLinkButton.clicked.connect(open_view_all)
ui.clear_all_data_commandLinkButton.clicked.connect(open_clear_data)
ui.return_pushButton.clicked.connect(back_to_main)
