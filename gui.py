# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Temp_prj\Python_prj\Ctrl_cabinet\gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(715, 430)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(480, 20, 221, 71))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_closeport = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_closeport.setEnabled(False)
        self.pushButton_closeport.setGeometry(QtCore.QRect(130, 40, 75, 23))
        self.pushButton_closeport.setObjectName("pushButton_closeport")
        self.pushButton_openport = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_openport.setGeometry(QtCore.QRect(130, 10, 75, 23))
        self.pushButton_openport.setObjectName("pushButton_openport")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 101, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_portnum = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_portnum.setEnabled(True)
        self.lineEdit_portnum.setMaxLength(5)
        self.lineEdit_portnum.setObjectName("lineEdit_portnum")
        self.horizontalLayout_5.addWidget(self.lineEdit_portnum)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 461, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget_stat = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_stat.setGeometry(QtCore.QRect(10, 20, 441, 181))
        self.tableWidget_stat.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_stat.setMidLineWidth(1)
        self.tableWidget_stat.setAutoScrollMargin(16)
        self.tableWidget_stat.setObjectName("tableWidget_stat")
        self.tableWidget_stat.setColumnCount(4)
        self.tableWidget_stat.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stat.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stat.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stat.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stat.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stat.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stat.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stat.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stat.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_stat.setItem(4, 3, item)
        self.tableWidget_stat.horizontalHeader().setDefaultSectionSize(101)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(480, 100, 221, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_single_motor_run = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_single_motor_run.setGeometry(QtCore.QRect(130, 140, 75, 23))
        self.pushButton_single_motor_run.setObjectName("pushButton_single_motor_run")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 20, 151, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_single_motor_name = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_single_motor_name.setObjectName("comboBox_single_motor_name")
        self.comboBox_single_motor_name.addItem("")
        self.comboBox_single_motor_name.addItem("")
        self.comboBox_single_motor_name.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_single_motor_name)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 50, 151, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_single_motor_ctrl = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_single_motor_ctrl.setObjectName("comboBox_single_motor_ctrl")
        self.comboBox_single_motor_ctrl.addItem("")
        self.comboBox_single_motor_ctrl.addItem("")
        self.comboBox_single_motor_ctrl.addItem("")
        self.comboBox_single_motor_ctrl.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_single_motor_ctrl)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(40, 80, 151, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.doubleSpinBox_single_motor_angel = QtWidgets.QDoubleSpinBox(self.layoutWidget3)
        self.doubleSpinBox_single_motor_angel.setMinimumSize(QtCore.QSize(82, 0))
        self.doubleSpinBox_single_motor_angel.setDecimals(4)
        self.doubleSpinBox_single_motor_angel.setMinimum(-200.0)
        self.doubleSpinBox_single_motor_angel.setMaximum(200.0)
        self.doubleSpinBox_single_motor_angel.setSingleStep(1.0)
        self.doubleSpinBox_single_motor_angel.setProperty("value", 0.0)
        self.doubleSpinBox_single_motor_angel.setObjectName("doubleSpinBox_single_motor_angel")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_single_motor_angel)
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(40, 110, 151, 22))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.doubleSpinBox_single_motor_speed = QtWidgets.QDoubleSpinBox(self.layoutWidget4)
        self.doubleSpinBox_single_motor_speed.setMinimumSize(QtCore.QSize(82, 0))
        self.doubleSpinBox_single_motor_speed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_single_motor_speed.setDecimals(2)
        self.doubleSpinBox_single_motor_speed.setMinimum(0.0)
        self.doubleSpinBox_single_motor_speed.setMaximum(6.0)
        self.doubleSpinBox_single_motor_speed.setSingleStep(1.0)
        self.doubleSpinBox_single_motor_speed.setProperty("value", 5.0)
        self.doubleSpinBox_single_motor_speed.setObjectName("doubleSpinBox_single_motor_speed")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_single_motor_speed)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(480, 280, 221, 141))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit_flow = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_flow.setGeometry(QtCore.QRect(10, 30, 201, 71))
        self.textEdit_flow.setObjectName("textEdit_flow")
        self.pushButton_flow_file = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_flow_file.setGeometry(QtCore.QRect(30, 110, 75, 23))
        self.pushButton_flow_file.setObjectName("pushButton_flow_file")
        self.pushButton_flow_next = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_flow_next.setEnabled(False)
        self.pushButton_flow_next.setGeometry(QtCore.QRect(140, 110, 75, 23))
        self.pushButton_flow_next.setObjectName("pushButton_flow_next")
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 240, 461, 181))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textEdit_log = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_log.setGeometry(QtCore.QRect(10, 20, 441, 121))
        self.textEdit_log.setObjectName("textEdit_log")
        self.pushButton_log_clear = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_log_clear.setGeometry(QtCore.QRect(380, 150, 75, 23))
        self.pushButton_log_clear.setObjectName("pushButton_log_clear")

        self.retranslateUi(Form)
        self.comboBox_single_motor_ctrl.setCurrentIndex(3)
        self.pushButton_log_clear.clicked.connect(Form.click_log_clear)
        self.pushButton_openport.clicked.connect(Form.click_pushButton_openport)
        self.pushButton_closeport.clicked.connect(Form.click_pushButton_closeport)
        self.pushButton_single_motor_run.clicked.connect(Form.click_pushButton_single_motor_run)
        self.pushButton_flow_file.clicked.connect(Form.click_pushButton_flow_file)
        self.pushButton_flow_next.clicked.connect(Form.click_pushButton_flow_next)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_portnum, self.pushButton_openport)
        Form.setTabOrder(self.pushButton_openport, self.comboBox_single_motor_name)
        Form.setTabOrder(self.comboBox_single_motor_name, self.comboBox_single_motor_ctrl)
        Form.setTabOrder(self.comboBox_single_motor_ctrl, self.doubleSpinBox_single_motor_angel)
        Form.setTabOrder(self.doubleSpinBox_single_motor_angel, self.doubleSpinBox_single_motor_speed)
        Form.setTabOrder(self.doubleSpinBox_single_motor_speed, self.pushButton_single_motor_run)
        Form.setTabOrder(self.pushButton_single_motor_run, self.textEdit_flow)
        Form.setTabOrder(self.textEdit_flow, self.pushButton_flow_file)
        Form.setTabOrder(self.pushButton_flow_file, self.pushButton_flow_next)
        Form.setTabOrder(self.pushButton_flow_next, self.tableWidget_stat)
        Form.setTabOrder(self.tableWidget_stat, self.textEdit_log)
        Form.setTabOrder(self.textEdit_log, self.pushButton_log_clear)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "转台控制程序"))
        self.groupBox.setTitle(_translate("Form", "串口控制"))
        self.pushButton_closeport.setText(_translate("Form", "关闭"))
        self.pushButton_openport.setText(_translate("Form", "打开"))
        self.label_5.setText(_translate("Form", "串口号"))
        self.lineEdit_portnum.setText(_translate("Form", "COM1"))
        self.groupBox_2.setTitle(_translate("Form", "偏振盒状态"))
        item = self.tableWidget_stat.verticalHeaderItem(0)
        item.setText(_translate("Form", "轴1"))
        item = self.tableWidget_stat.verticalHeaderItem(1)
        item.setText(_translate("Form", "轴2"))
        item = self.tableWidget_stat.verticalHeaderItem(2)
        item.setText(_translate("Form", "轴3"))
        item = self.tableWidget_stat.verticalHeaderItem(3)
        item.setText(_translate("Form", "轴4"))
        item = self.tableWidget_stat.verticalHeaderItem(4)
        item.setText(_translate("Form", "盒体"))
        item = self.tableWidget_stat.horizontalHeaderItem(0)
        item.setText(_translate("Form", "当前位置"))
        item = self.tableWidget_stat.horizontalHeaderItem(1)
        item.setText(_translate("Form", "开闭环"))
        item = self.tableWidget_stat.horizontalHeaderItem(2)
        item.setText(_translate("Form", "运动状态"))
        item = self.tableWidget_stat.horizontalHeaderItem(3)
        item.setText(_translate("Form", "报警情况"))
        __sortingEnabled = self.tableWidget_stat.isSortingEnabled()
        self.tableWidget_stat.setSortingEnabled(False)
        self.tableWidget_stat.setSortingEnabled(__sortingEnabled)
        self.groupBox_3.setTitle(_translate("Form", "单路电机控制"))
        self.pushButton_single_motor_run.setText(_translate("Form", "设置"))
        self.label.setText(_translate("Form", "电机名称"))
        self.comboBox_single_motor_name.setItemText(0, _translate("Form", "盒体"))
        self.comboBox_single_motor_name.setItemText(1, _translate("Form", "轴1轴2"))
        self.comboBox_single_motor_name.setItemText(2, _translate("Form", "轴3轴4"))
        self.label_2.setText(_translate("Form", "控制方式"))
        self.comboBox_single_motor_ctrl.setItemText(0, _translate("Form", "闭环"))
        self.comboBox_single_motor_ctrl.setItemText(1, _translate("Form", "开环"))
        self.comboBox_single_motor_ctrl.setItemText(2, _translate("Form", "停车"))
        self.comboBox_single_motor_ctrl.setItemText(3, _translate("Form", "运动"))
        self.label_3.setText(_translate("Form", "目标角度"))
        self.label_4.setText(_translate("Form", "运动速度"))
        self.groupBox_4.setTitle(_translate("Form", "流程控制"))
        self.textEdit_flow.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">注意：导入的文件名不能为中文</p></body></html>"))
        self.pushButton_flow_file.setText(_translate("Form", "导入文件"))
        self.pushButton_flow_next.setText(_translate("Form", "执行下一步"))
        self.groupBox_5.setTitle(_translate("Form", "日志"))
        self.pushButton_log_clear.setText(_translate("Form", "清除"))

