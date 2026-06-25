from pynput.mouse import Button, Controller
import pyautogui
from clickScreenScript import click
import json
import time
import keyboard
from PySide6 import QtWidgets,QtGui,QtCore
import sys

""" 
mouse = Controller()

print("=" * 50)
print(">>> 明日方舟 - 疯狂roll币脚本 启动 <<<")
print("=" * 50)

time.sleep(5)

rollCount = 200

print("运行中")
print("F8 停止")
print("鼠标移到左上角强制退出")


rollCount = rollCount  * 2

while True:

    rollCount -= 1
    
    # 左上角强制退出
    x, y = pyautogui.position()

    if y >= 1538:
        print("触发左上角紧急停止")
        break

    # 第一次点击
    mouse.position = (2290, 238)
    mouse.click(Button.left, 1)

    time.sleep(1)

    # 第二次点击
    mouse.position = (2066, 1348)
    mouse.click(Button.left, 1)

    time.sleep(1)

    # F8退出
    if keyboard.is_pressed("F8"):
        print("已停止")
        break

    if rollCount <= 0:
        break

""" 


class RollWindow(QtWidgets.QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(800,600)
        self.setWindowTitle('明日方舟疯狂roll币脚本')
        self.setup_ui()
        self.connectLogi()

    def setup_ui(self):
        layout = QtWidgets.QFormLayout()

        #roll币点位
        self.LE_CoinCoordinate = QtWidgets.QLineEdit()
        self.LB_CoinCoordinate = QtWidgets.QLabel('请输入roll币坐标, 以空格隔开')
        self.LE_CoinCoordinate.setPlaceholderText('默认坐标为 2290  238')
#        self.LE_CoinCoordinate.setFixedWidth(300)
        layout.addRow(self.LB_CoinCoordinate,self.LE_CoinCoordinate)

        #快进点位
        self.LE_SkipCoordinate = QtWidgets.QLineEdit()
        self.LB_SkipCoordinate = QtWidgets.QLabel('请输入快进坐标, 以空格隔开')
        self.LE_SkipCoordinate.setPlaceholderText('默认坐标为 2066  1348')
        layout.addRow(self.LB_SkipCoordinate,self.LE_SkipCoordinate)

        #操作次数
        self.LE_OperationsCount = QtWidgets.QLineEdit()
        self.LB_OperationsCount = QtWidgets.QLabel('请输入操作次数')
        self.LE_OperationsCount.setPlaceholderText('默认为10次')
        layout.addRow(self.LB_OperationsCount,self.LE_OperationsCount)

        self.setLayout(layout)

        #开始操作
        self.BT_StartOperation = QtWidgets.QPushButton('开始操作',self)
        self.BT_StartOperation.setGeometry(100,150,140,70)



        #日志打印
        self.PTE_log = QtWidgets.QPlainTextEdit(self)
        self.PTE_log.setGeometry(5,300,790,295)

    def connectLogi(self):
        #默认roll币坐标
        RollCoo = (2290, 238)

        #默认快进坐标
        SkipCoo = (2066, 1348)

        #默认操作次数
        OperationsCount = 10

        if self.LE_CoinCoordinate.text() == '':
            pass
        else :
            text = self.LE_CoinCoordinate.text()
            text = text.split()
            RollCoo = int(text[0]),int(text[1])

        if self.LE_SkipCoordinate.text() == '':
            pass
        else :
            text = self.LE_SkipCoordinate.text()
            text = text.split()
            SkipCoo = int(text[0]),int(text[1])

        if self.LE_OperationsCount.text() == '':
           pass
        else :
            text = self.LE_OperationsCount.text()
            OperationsCount = int(text)
    
        OperationsCount = OperationsCount*2

        def start():
            time.sleep(1)
#          self.showMinimized()
            for i in range(OperationsCount):
                if not click(RollCoo[0],RollCoo[1],1):
                    break
                if not click(SkipCoo[0],SkipCoo[1],1):
                    break
            

        self.BT_StartOperation.clicked.connect(start)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RollWindow()    
    window.show()
    sys.exit(app.exec())


