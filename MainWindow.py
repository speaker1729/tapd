# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(153, 153, 153);")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(100, 0, 500, 400))
        self.stackedWidget.setStyleSheet(u"QLabel\n"
"{\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(0,0,0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton\n"
"{\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.page_user.setStyleSheet(u"")
        self.btn_registry = QPushButton(self.page_user)
        self.btn_registry.setObjectName(u"btn_registry")
        self.btn_registry.setGeometry(QRect(20, 140, 70, 30))
        self.btn_login = QPushButton(self.page_user)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(100, 140, 70, 30))
        self.in_username = QLineEdit(self.page_user)
        self.in_username.setObjectName(u"in_username")
        self.in_username.setGeometry(QRect(100, 40, 150, 30))
        self.in_password = QLineEdit(self.page_user)
        self.in_password.setObjectName(u"in_password")
        self.in_password.setGeometry(QRect(100, 90, 150, 30))
        self.in_password.setEchoMode(QLineEdit.Normal)
        self.label = QLabel(self.page_user)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 60, 30))
        self.label.setStyleSheet(u"")
        self.label_2 = QLabel(self.page_user)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 60, 30))
        self.label_3 = QLabel(self.page_user)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 40, 150, 30))
        self.btn_logout = QPushButton(self.page_user)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setGeometry(QRect(180, 140, 70, 30))
        self.lab_user = QLabel(self.page_user)
        self.lab_user.setObjectName(u"lab_user")
        self.lab_user.setGeometry(QRect(290, 90, 150, 30))
        self.lab_statue = QLabel(self.page_user)
        self.lab_statue.setObjectName(u"lab_statue")
        self.lab_statue.setGeometry(QRect(290, 190, 150, 30))
        self.label_6 = QLabel(self.page_user)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 140, 150, 30))
        self.stackedWidget.addWidget(self.page_user)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.lv_user = QListView(self.page_admin)
        self.lv_user.setObjectName(u"lv_user")
        self.lv_user.setGeometry(QRect(20, 90, 120, 300))
        self.lv_folder = QListView(self.page_admin)
        self.lv_folder.setObjectName(u"lv_folder")
        self.lv_folder.setGeometry(QRect(360, 90, 120, 300))
        self.label_4 = QLabel(self.page_admin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 120, 30))
        self.label_5 = QLabel(self.page_admin)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(360, 20, 120, 30))
        self.btn_delete = QPushButton(self.page_admin)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(150, 170, 70, 30))
        self.lab_folder = QLabel(self.page_admin)
        self.lab_folder.setObjectName(u"lab_folder")
        self.lab_folder.setGeometry(QRect(360, 60, 120, 30))
        self.lab_userview = QLabel(self.page_admin)
        self.lab_userview.setObjectName(u"lab_userview")
        self.lab_userview.setGeometry(QRect(20, 60, 120, 30))
        self.btn_choose = QPushButton(self.page_admin)
        self.btn_choose.setObjectName(u"btn_choose")
        self.btn_choose.setGeometry(QRect(150, 130, 70, 30))
        self.btn_add = QPushButton(self.page_admin)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(280, 170, 70, 30))
        self.btn_open = QPushButton(self.page_admin)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setGeometry(QRect(280, 130, 70, 30))
        self.btn_apply = QPushButton(self.page_admin)
        self.btn_apply.setObjectName(u"btn_apply")
        self.btn_apply.setGeometry(QRect(150, 230, 70, 30))
        self.btn_cancle = QPushButton(self.page_admin)
        self.btn_cancle.setObjectName(u"btn_cancle")
        self.btn_cancle.setGeometry(QRect(150, 270, 70, 30))
        self.lab_admin = QLabel(self.page_admin)
        self.lab_admin.setObjectName(u"lab_admin")
        self.lab_admin.setGeometry(QRect(190, 60, 120, 30))
        self.label_10 = QLabel(self.page_admin)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(190, 20, 120, 30))
        self.stackedWidget.addWidget(self.page_admin)
        self.page_file = QWidget()
        self.page_file.setObjectName(u"page_file")
        self.lv_folder_2 = QListView(self.page_file)
        self.lv_folder_2.setObjectName(u"lv_folder_2")
        self.lv_folder_2.setGeometry(QRect(360, 20, 120, 360))
        self.btn_down = QPushButton(self.page_file)
        self.btn_down.setObjectName(u"btn_down")
        self.btn_down.setGeometry(QRect(130, 110, 70, 30))
        self.btn_downview = QPushButton(self.page_file)
        self.btn_downview.setObjectName(u"btn_downview")
        self.btn_downview.setGeometry(QRect(130, 50, 70, 30))
        self.btn_up = QPushButton(self.page_file)
        self.btn_up.setObjectName(u"btn_up")
        self.btn_up.setGeometry(QRect(30, 110, 70, 30))
        self.btn_upview = QPushButton(self.page_file)
        self.btn_upview.setObjectName(u"btn_upview")
        self.btn_upview.setGeometry(QRect(30, 50, 70, 30))
        self.label_7 = QLabel(self.page_file)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 290, 150, 30))
        self.lab_folder_2 = QLabel(self.page_file)
        self.lab_folder_2.setObjectName(u"lab_folder_2")
        self.lab_folder_2.setGeometry(QRect(30, 240, 150, 30))
        self.lab_file = QLabel(self.page_file)
        self.lab_file.setObjectName(u"lab_file")
        self.lab_file.setGeometry(QRect(30, 340, 150, 30))
        self.label_8 = QLabel(self.page_file)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 190, 150, 30))
        self.lab_statue_2 = QLabel(self.page_file)
        self.lab_statue_2.setObjectName(u"lab_statue_2")
        self.lab_statue_2.setGeometry(QRect(200, 340, 150, 30))
        self.label_9 = QLabel(self.page_file)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(200, 290, 150, 30))
        self.stackedWidget.addWidget(self.page_file)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 100, 400))
        self.frame.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 255, 255);\n"
"	background-color: rgb(96, 96, 96);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QFrame\n"
"{\n"
"	background-color: rgb(96, 96, 96);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_user = QPushButton(self.frame)
        self.btn_user.setObjectName(u"btn_user")
        self.btn_user.setGeometry(QRect(10, 10, 80, 30))
        self.btn_admin = QPushButton(self.frame)
        self.btn_admin.setObjectName(u"btn_admin")
        self.btn_admin.setGeometry(QRect(10, 50, 80, 30))
        self.btn_file = QPushButton(self.frame)
        self.btn_file.setObjectName(u"btn_file")
        self.btn_file.setGeometry(QRect(10, 90, 80, 30))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_registry.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u7528\u6237\u540d</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u5bc6\u7801</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u5f53\u524d\u7528\u6237</span></p></body></html>", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u767b\u51fa", None))
        self.lab_user.setText(QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.lab_statue.setText(QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u5f53\u524d\u72b6\u6001</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u7528\u6237\u89c6\u56fe</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u6587\u4ef6\u5939</span></p></body></html>", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u4e00\u9879", None))
        self.lab_folder.setText(QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.lab_userview.setText(QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.btn_choose.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7528\u6237", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u4e00\u9879", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.btn_apply.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u7528", None))
        self.btn_cancle.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.lab_admin.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u7ba1\u7406\u5458\u767b\u5f55</span></p></body></html>", None))
        self.btn_down.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.btn_downview.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u89c6\u56fe", None))
        self.btn_up.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20", None))
        self.btn_upview.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u89c6\u56fe", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u5f53\u524d\u6587\u4ef6</span></p></body></html>", None))
        self.lab_folder_2.setText(QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.lab_file.setText(QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u5f53\u524d\u6587\u4ef6\u5939</span></p></body></html>", None))
        self.lab_statue_2.setText(QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u5f53\u524d\u72b6\u6001</span></p></body></html>", None))
        self.btn_user.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237", None))
        self.btn_admin.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406\u5458", None))
        self.btn_file.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

