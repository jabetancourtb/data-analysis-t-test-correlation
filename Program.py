# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Programa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import upload_file as ufile
import t_test as tt
import correlation_test as ct

from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))



file_data = ufile.upload_file(r"C:\Users\pck\Downloads\Jupyter\hour.csv")

preprocessed_data = file_data.copy()

#tt.paired_t_test(preprocessed_data['registered'], preprocessed_data['casual'])

#tt.one_sample_t_test(20, [2.25, 2.0, 1.95, 2.0, 2.19, 2.30])

#tt.insert_data()

ct.pearson_cor(preprocessed_data['registered'], preprocessed_data['casual'])

ct.spearman_cor(preprocessed_data['registered'], preprocessed_data['casual'])