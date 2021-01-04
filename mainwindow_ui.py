# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(984, 651)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.widget_pane = QWidget(self.centralWidget)
        self.widget_pane.setObjectName(u"widget_pane")
        self.widget_pane.setGeometry(QRect(0, 0, 981, 381))
        self.tabWidget = QTabWidget(self.widget_pane)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 971, 281))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 471, 231))
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 30, 221, 171))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setSpacing(6)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit)

        self.textLabelLabel = QLabel(self.formLayoutWidget)
        self.textLabelLabel.setObjectName(u"textLabelLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.textLabelLabel)

        self.textLabelLineEdit = QLineEdit(self.formLayoutWidget)
        self.textLabelLineEdit.setObjectName(u"textLabelLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.textLabelLineEdit)

        self.formLayoutWidget_2 = QWidget(self.groupBox)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(240, 30, 221, 171))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setContentsMargins(11, 11, 11, 11)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.t1Label = QLabel(self.formLayoutWidget_2)
        self.t1Label.setObjectName(u"t1Label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.t1Label)

        self.t1LineEdit = QLineEdit(self.formLayoutWidget_2)
        self.t1LineEdit.setObjectName(u"t1LineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.t1LineEdit)

        self.t2Label = QLabel(self.formLayoutWidget_2)
        self.t2Label.setObjectName(u"t2Label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.t2Label)

        self.t2LineEdit = QLineEdit(self.formLayoutWidget_2)
        self.t2LineEdit.setObjectName(u"t2LineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.t2LineEdit)

        self.t3Label = QLabel(self.formLayoutWidget_2)
        self.t3Label.setObjectName(u"t3Label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.t3Label)

        self.t3LineEdit = QLineEdit(self.formLayoutWidget_2)
        self.t3LineEdit.setObjectName(u"t3LineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.t3LineEdit)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(490, 10, 471, 231))
        self.formLayoutWidget_3 = QWidget(self.groupBox_2)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(10, 30, 221, 171))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setSpacing(6)
        self.formLayout_3.setContentsMargins(11, 11, 11, 11)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.t5Label = QLabel(self.formLayoutWidget_3)
        self.t5Label.setObjectName(u"t5Label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.t5Label)

        self.t5LineEdit = QLineEdit(self.formLayoutWidget_3)
        self.t5LineEdit.setObjectName(u"t5LineEdit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.t5LineEdit)

        self.t6Label = QLabel(self.formLayoutWidget_3)
        self.t6Label.setObjectName(u"t6Label")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.t6Label)

        self.t6LineEdit = QLineEdit(self.formLayoutWidget_3)
        self.t6LineEdit.setObjectName(u"t6LineEdit")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.t6LineEdit)

        self.t7Label = QLabel(self.formLayoutWidget_3)
        self.t7Label.setObjectName(u"t7Label")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.t7Label)

        self.t7LineEdit = QLineEdit(self.formLayoutWidget_3)
        self.t7LineEdit.setObjectName(u"t7LineEdit")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.t7LineEdit)

        self.formLayoutWidget_4 = QWidget(self.groupBox_2)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(240, 30, 221, 171))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setSpacing(6)
        self.formLayout_4.setContentsMargins(11, 11, 11, 11)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.t8Label = QLabel(self.formLayoutWidget_4)
        self.t8Label.setObjectName(u"t8Label")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.t8Label)

        self.t8LineEdit = QLineEdit(self.formLayoutWidget_4)
        self.t8LineEdit.setObjectName(u"t8LineEdit")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.t8LineEdit)

        self.t9Label = QLabel(self.formLayoutWidget_4)
        self.t9Label.setObjectName(u"t9Label")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.t9Label)

        self.t9LineEdit = QLineEdit(self.formLayoutWidget_4)
        self.t9LineEdit.setObjectName(u"t9LineEdit")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.t9LineEdit)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 984, 22))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Device", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.textLabelLabel.setText(QCoreApplication.translate("MainWindow", u"text label", None))
        self.t1Label.setText(QCoreApplication.translate("MainWindow", u"t1", None))
        self.t2Label.setText(QCoreApplication.translate("MainWindow", u"t2", None))
        self.t3Label.setText(QCoreApplication.translate("MainWindow", u"t3", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.t5Label.setText(QCoreApplication.translate("MainWindow", u"t5", None))
        self.t6Label.setText(QCoreApplication.translate("MainWindow", u"t6", None))
        self.t7Label.setText(QCoreApplication.translate("MainWindow", u"t7", None))
        self.t8Label.setText(QCoreApplication.translate("MainWindow", u"t8", None))
        self.t9Label.setText(QCoreApplication.translate("MainWindow", u"t9", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Device &  Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Test Measurements", None))
    # retranslateUi

