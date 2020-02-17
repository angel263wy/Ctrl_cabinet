__author__ = 'WangYi'
__version__ = 0.1

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from gui import Ui_Form

import time
import serial
import numpy as np

class Test(QWidget, Ui_Form):
    def __init__(self):
        super(Test, self).__init__()        
        self.setupUi(self)
        # 串口类   
        self.myserial = serial.Serial() 
        # 需要发送的21字节 第21字节为累加和
        self.data_send21 = np.zeros(21, dtype='uint8')
        

# ----------------响应和槽函数----------------
    def click_log_clear(self):  # 清除日志界面
        self.textEdit_log.clear()

    def click_pushButton_openport(self):  # 打开串口函数
        self.myserial.port = self.lineEdit_portnum.text()
        self.myserial.baudrate = 38400
        self.myserial.bytesize = serial.EIGHTBITS
        self.myserial.parity = serial.PARITY_NONE
        self.myserial.stopbits = serial.STOPBITS_ONE
        try:  # 打开串口         
            self.myserial.open()
            self.log_show('串口打开成功')
            self.lineEdit_portnum.setEnabled(False)
            self.pushButton_closeport.setEnabled(True)
            self.pushButton_openport.setEnabled(False)
        except Exception as e:
            self.log_show('串口打开失败')
    
    def click_pushButton_closeport(self):   # 关闭串口
        try:  # 关闭串口  
            self.myserial.close() 
            self.log_show('串口关闭成功')
            self.lineEdit_portnum.setEnabled(True)
            self.pushButton_openport.setEnabled(True)
            self.pushButton_closeport.setEnabled(False)
        except Exception as e:
            self.log_show('串口关闭失败')

    def click_pushButton_single_motor_run(self):  # 单电机控制
        # 清除需要发送的字节 并进行帧头初始化
        self.data_send21 = np.zeros(21, dtype='uint8')
        self.data_send21[0] = 0xaa
        self.data_send21[1] = 0xaa

        # 获取单机名称
        if 0 == self.comboBox_single_motor_name.currentIndex(): #盒体
            data_index = 14
            motor_name = '盒体 ' #字符串用于记录日志
        elif 1 == self.comboBox_single_motor_name.currentIndex(): # 轴1轴2
            data_index = 2
            motor_name = '轴1轴2 '
        elif 2 == self.comboBox_single_motor_name.currentIndex(): # 轴3轴4
            data_index = 8
            motor_name = '轴3轴4 '
        else:
            pass

        # 获取控制方式
        if 0 == self.comboBox_single_motor_ctrl.currentIndex(): #闭环
            self.data_send21[data_index] = 0xAB
            motor_ctrl = '闭环 ' #字符串用于记录日志
        elif 1 == self.comboBox_single_motor_ctrl.currentIndex(): # 开环
            self.data_send21[data_index] = 0xAC
            motor_ctrl = '开环 '
        elif 2 == self.comboBox_single_motor_ctrl.currentIndex(): # 停车
            self.data_send21[data_index] = 0x80
            motor_ctrl = '停车 '
        elif 3 == self.comboBox_single_motor_ctrl.currentIndex(): # 运动
            self.data_send21[data_index] = 0x81
            motor_ctrl = '运动 '
        else:  
            pass
        
        # 获取转动目标角度 并转换
        tmp_position = self.doubleSpinBox_single_motor_angel.value()
        motor_pos = str(tmp_position) #字符串用于记录日志
        
        ll, mm, hh = self.pos2byte(tmp_position)
        self.data_send21[data_index+1] = ll
        self.data_send21[data_index+2] = mm
        self.data_send21[data_index+3] = hh

        # 获取运动速度
        tmp_speed = self.doubleSpinBox_single_motor_speed.value()
        motor_speed = str(tmp_speed)

        ll, hh = self.speed2byte(tmp_speed)
        self.data_send21[data_index+4] = ll
        self.data_send21[data_index+5] = hh
        
        # 求累加和
        self.data_send21[-1] = self.serial_sum(self.data_send21)
        
        # 发送数据
        try:
            self.myserial.write(self.data_send21)
            self.log_show(motor_name+motor_ctrl + '角度' 
                    + motor_pos + ' 速度' + motor_speed + ' 设置完成')
        except Exception as e:
            self.log_show('串口发送失败')
        

# ----------------内部函数----------------
    # 记录日志函数
    def log_show(self, foo_txt):
        now = time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time()))
        txt_out = now + foo_txt
        self.textEdit_log.append(txt_out)

    # 转台位置十进制转三个字节
    def pos2byte(self, pos):
        foo_pos = abs(round(pos * 10000)) # 求绝对值 乘1000后取整数
        
        low_byte = foo_pos & 0xff
        mid_byte = (foo_pos >> 8 ) & 0xff
        high_byte = (foo_pos >> 16 ) & 0xff

        if pos < 0:  # 有负数 最高位补1
            high_byte = 0x80 | high_byte
        
        return low_byte, mid_byte, high_byte
    
    # 转台速度转换函数
    def speed2byte(self, sped):
        foo_speed = abs(round(sped * 100)) # 求绝对值 乘100后取整数
        
        low_byte = foo_speed & 0xff
        high_byte = (foo_speed >> 8 ) & 0xff     

        return low_byte, high_byte

    def serial_sum(self, foo):
        sum = 0
        for i in foo[2:-1]:
            sum += i
        return (sum & 0xff)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywidget = Test()
    mywidget.show()
    sys.exit(app.exec_())


