import os
from PySide6 import QtWidgets
from PySide6.QtCore import QDir, Qt
from PySide6.QtWidgets import QApplication, QFileDialog


def file_choose():
    file_dialog = QFileDialog()
    file_dialog.setOption(QFileDialog.DontUseNativeDialog)
    file_dialog.setFileMode(QFileDialog.ExistingFiles)
    file_dialog.exec()
    selected_file = file_dialog.selectedFiles()
    return selected_file


def folder_choose():
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.Directory)
    file_dialog.exec()
    selected_folder = file_dialog.selectedFiles()[0]
    return selected_folder

