__author__ = 'WangYi'
__version__ = 0.1

# 串口接收 定时接收数据 仅取出1帧有效帧 然后解码并显示 其他帧丢弃 所有接收和处理在一个函数中完成
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QTableWidgetItem, QFileDialog
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QBrush, QColor
from gui import Ui_Form

import time
import serial
import numpy as np
import pandas as pd
import queue

class Test(QWidget, Ui_Form):
    def __init__(self):
        super(Test, self).__init__()        
        self.setupUi(self)
        # 串口类   
        self.myserial = serial.Serial() 
        # 需要发送的21字节 第21字节为累加和
        self.data_send21 = np.zeros(21, dtype='uint8')
        # 用于流程的队列 每一次put都将整帧放入 串口直接发送即可
        self.flow_queue = queue.Queue()
        self.flow_next_step = list()  # 保存下一个流程的角度 点击下一步按钮执行该列表内容
        # 定时器 定时中断收取串口数据
        self.timer_serial_rcv = QTimer()
        self.timer_serial_rcv.stop()  # 可靠性设计 立即停止
        self.timer_serial_rcv.setInterval(500)
        self.timer_serial_rcv.timeout.connect(self.serial_recv)  # 绑定信号和槽         
        

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
            self.timer_serial_rcv.start()  # 启动接收定时器
            self.lineEdit_portnum.setEnabled(False)
            self.pushButton_closeport.setEnabled(True)
            self.pushButton_openport.setEnabled(False)
        except Exception as e:
            self.log_show('串口打开失败')
    
    def click_pushButton_closeport(self):   # 关闭串口        
        try:  # 关闭串口              
            self.myserial.close() 
            self.log_show('串口关闭成功')
            self.timer_serial_rcv.stop()  # 停止接收定时器
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

    # 打开流程文件
    def click_pushButton_flow_file(self):
        # 流程队列非空则清空
        while self.flow_queue.qsize() > 0:
            self.flow_queue.get()

        filename = QFileDialog.getOpenFileName(self, filter='csv file(*.csv)', caption='打开流程文件')
        if filename[0] :
            flow_dat_df = pd.read_csv(filename[0], header=0)
            # 处理csv文件并导入队列
            flow_len = len(flow_dat_df.index)        
            for i in range(flow_len):
                pos = [0, 0.0, 0.0, 0.0] 
                pos[0] = int(flow_dat_df.iloc[i,0])  # np类型转python类型
                pos[1] = float(flow_dat_df.iloc[i,1])
                pos[2] = float(flow_dat_df.iloc[i,2])
                pos[3] = float(flow_dat_df.iloc[i,3])                       
                self.flow_queue.put(self.flow2queue(pos[0], pos[1], pos[2], pos[3]))
            
            self.log_show('流程导入成功 共计' + str(flow_len) + '步')
        else:
            self.log_show('文件未打开')            

        # 如果有流程 取出第一行并显示 '下一步'按钮使能
        if self.flow_queue.qsize() > 0 :
            self.flow_next_step = self.flow_queue.get()
            self.textEdit_flow.clear()
            self.textEdit_flow.append('下一步序号： ' + self.flow_next_step[-4])
            self.textEdit_flow.append('轴1轴2目标角度： ' + self.flow_next_step[-3])
            self.textEdit_flow.append('轴3轴4目标角度： ' + self.flow_next_step[-2])
            self.textEdit_flow.append('盒体目标角度： ' + self.flow_next_step[-1])
            self.pushButton_flow_next.setEnabled(True)           


    # 运行下一步流程
    def click_pushButton_flow_next(self):
        # 将现存的字节发送出去
        try:
            self.myserial.write(self.flow_next_step[0:21])
             # 取出数据用于显示
            cnt = self.flow_next_step[-4]
            pos12 = self.flow_next_step[-3]
            pos34 = self.flow_next_step[-2]
            posbox = self.flow_next_step[-1]
            self.log_show('第' + cnt + '步执行完成 轴1轴2:' + pos12 + ' 轴3轴4:'
                            + pos34 + ' 盒体:' + posbox)
            # 发送完成后 如果后续还有内容 提取、暂存并显示 如果没有 '下一步'按钮禁用
            if self.flow_queue.qsize() > 0 :
                self.flow_next_step = self.flow_queue.get()
                self.textEdit_flow.clear()
                self.textEdit_flow.append('下一步序号： ' + self.flow_next_step[-4])
                self.textEdit_flow.append('轴1轴2目标角度： ' + self.flow_next_step[-3])
                self.textEdit_flow.append('轴3轴4目标角度： ' + self.flow_next_step[-2])
                self.textEdit_flow.append('盒体目标角度： ' + self.flow_next_step[-1])
            else:
                self.pushButton_flow_next.setEnabled(False)
                                        
        except Exception as e:
            self.log_show('串口发送失败')

       

        
     

# ----------------自定义信号和槽函数----------------
    def serial_recv(self): 
        rcv_frame = list()       
        if self.myserial.is_open and (self.myserial.inWaiting() > 0):
            rcv = self.myserial.read(self.myserial.inWaiting())
            for cnt, i in enumerate(rcv) :
                if (i == 0xaa) and (rcv[cnt + 1] == 0xaa):                    
                    _rcv_frame = rcv[cnt : cnt+23] 
                    break            
            # 接收完成后看看是否有整帧 如果有 转list类型 判累加和后解码显示            
            if len(_rcv_frame) == 23:  #  帧头对 只有一个AA就可以判断
                for j in _rcv_frame:  # byte类型转int
                    # rcv_frame.append(int.from_bytes(j, byteorder='little'))
                    rcv_frame.append(j)
                if rcv_frame[-1] == self.serial_sum(rcv_frame):
                    self.serial_frame_show(rcv_frame)  
            
        

# ----------------内部函数----------------
    # 记录日志函数
    def log_show(self, foo_txt):
        now = time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time()))
        txt_out = now + foo_txt
        self.textEdit_log.append(txt_out)
    
    # 偏振盒各电机状态解码函数 被串口接收解析函数调用
    def serial_frame_show(self, frame_dat):
        axis_pos = [0, 0, 0, 0, 0] # 位置列表 依次代表轴1~4 最后一个元素为盒体
        axis_loop_openclose = [0, 0, 0, 0, 0] # 开闭环中途
        axis_run_stop = [0, 0, 0, 0, 0]  # 运动 静止
        axis_ok_error = [0, 0, 0, 0, 0]  # 正常和报警

        # 角度位置提取和更新
        axis_pos[0] = self.byte2pos(frame_dat[2], frame_dat[3], frame_dat[4])
        axis_pos[1] = self.byte2pos(frame_dat[6], frame_dat[7], frame_dat[8])
        axis_pos[2] = self.byte2pos(frame_dat[10], frame_dat[11], frame_dat[12])
        axis_pos[3] = self.byte2pos(frame_dat[14], frame_dat[15], frame_dat[16])
        axis_pos[4] = self.byte2pos(frame_dat[18], frame_dat[19], frame_dat[20])

        # 状态信息提取和更新
        axis_loop_openclose[0], axis_run_stop[0], axis_ok_error[0] = self.stat_handle(frame_dat[5])
        axis_loop_openclose[1], axis_run_stop[1], axis_ok_error[1] = self.stat_handle(frame_dat[9])
        axis_loop_openclose[2], axis_run_stop[2], axis_ok_error[2] = self.stat_handle(frame_dat[13])
        axis_loop_openclose[3], axis_run_stop[3], axis_ok_error[3] = self.stat_handle(frame_dat[17])
        axis_loop_openclose[4], axis_run_stop[4], axis_ok_error[4] = self.stat_handle(frame_dat[21])
        
        # 内容显示
        for i in range(5) :
            self.tableWidget_stat.setItem(i, 0, self.table_item_set(str(axis_pos[i])))
            self.tableWidget_stat.setItem(i, 1, self.table_item_set(axis_loop_openclose[i]))            
            self.tableWidget_stat.setItem(i, 2, self.table_item_set(axis_run_stop[i]))
            self.tableWidget_stat.setItem(i, 3, self.table_item_set(axis_ok_error[i]))            

        pass


    # tablewidget中每个方框内容设置  被状态解码函数serial_frame_show调用
    def table_item_set(self, content):
        item = QTableWidgetItem(content)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        if content == '报警':
            item.setBackground(QBrush(QColor(255, 0, 0)))
        elif content == '运动' : 
            item.setBackground(QBrush(QColor(0, 255, 0)))
        else:
            item.setBackground(QBrush(QColor(255, 255, 255)))        
        
        return item

    # 转台位置十进制转三个字节
    def pos2byte(self, pos):
        foo_pos = abs(round(pos * 10000)) # 求绝对值 乘10000后取整数
        foo = foo_pos.to_bytes(length=3, byteorder='little')  # int类型转byte
        if pos < 0: # 有负数 最高位补1
            high_byte = foo[2] | 0x80
        else:
            high_byte = foo[2]
        return foo[0], foo[1], high_byte
    
    # 转台位置三字节转十进制  转台当前角度解析使用
    def byte2pos(self, ll, mm, hh):
        foo_h = hh & 0x7f # 最高位清零
        foo_pos = [ll, mm, foo_h]
        pos = int.from_bytes(foo_pos, byteorder='little')
        if hh > 127 :
            pos = -1 * pos
        return (pos/10000)


    # 转台速度转换函数
    def speed2byte(self, sped):
        foo_speed = abs(round(sped * 100)) # 求绝对值 乘100后取整数
        
        low_byte = foo_speed & 0xff
        high_byte = (foo_speed >> 8 ) & 0xff     

        return low_byte, high_byte

    # 转动运行状态处理函数 按bit拆分状态 状态显示线程调用
    def stat_handle(self, stat):
        foo = stat & 0xff  # 仅保留一个字节        
        alarm = False
        # 开环闭环判断
        if (foo & 0x01) == 1:
            openclose = '闭环'
        else:
            openclose = '开环'
        # 运动静止判断
        if (foo & 0x02) == 0x02:
            run_stop =  '运动'
        else:
            run_stop = '静止'
        # 正常报警判断
        if (foo & 0x80) == 0x80:
            ok_error =  '报警'
            alarm = True
        else:
            ok_error = '正常'        
        return openclose, run_stop, ok_error

    
    # 流程表转串口发送队列函数 将流程表文件三个角度转换成用于发送的字节
    def flow2queue(self, cnt, pos12, pos34, pos_box):
        data_queue = list()
        foo_pos = [0, 0, 0]  # 暂存POS转BYTE的三字节
        data_queue.append(0xaa)  # 帧头 
        data_queue.append(0xaa)
        # 轴1轴2
        data_queue.append(0x81)  # 走位置
        foo_pos[0], foo_pos[1], foo_pos[2] = self.pos2byte(pos12)  # 角度
        data_queue.append(foo_pos[0]) 
        data_queue.append(foo_pos[1])
        data_queue.append(foo_pos[2])
        data_queue.append(0xf4)  # 速度 5度/s
        data_queue.append(0x01)
        # 轴3轴4
        data_queue.append(0x81)  # 走位置
        foo_pos[0], foo_pos[1], foo_pos[2] = self.pos2byte(pos34)  # 角度
        data_queue.append(foo_pos[0]) 
        data_queue.append(foo_pos[1])
        data_queue.append(foo_pos[2])
        data_queue.append(0xf4)  # 速度 5度/s
        data_queue.append(0x01)
        # 盒体
        data_queue.append(0x81)  # 走位置
        foo_pos[0], foo_pos[1], foo_pos[2] = self.pos2byte(pos_box)  # 角度
        data_queue.append(foo_pos[0]) 
        data_queue.append(foo_pos[1])
        data_queue.append(foo_pos[2])
        data_queue.append(0xf4)  # 速度 5度/s
        data_queue.append(0x01)
        # 累加和
        data_queue.append(0)
        data_queue[20] = self.serial_sum(data_queue)
        # 串口发送序列后 保存输入的角度值 用于显示
        data_queue.append(str(cnt))
        data_queue.append(str(pos12))
        data_queue.append(str(pos34))
        data_queue.append(str(pos_box))
        
        return data_queue


    #  求累加和函数
    def serial_sum(self, foo):
        sum = 0
        for i in foo[0:-1]:
            sum += i
        return (sum & 0xff)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywidget = Test()
    mywidget.show()
    sys.exit(app.exec_())


