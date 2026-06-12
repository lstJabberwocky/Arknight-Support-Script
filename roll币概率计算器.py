import sys
from PySide6 import QtWidgets,QtCore
from PySide6.QtCore import Qt
import math
from math import comb





class Window(QtWidgets.QWidget):

    # 按 F1 关闭窗口
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F1:
            self.close()  
        else:
            super().keyPressEvent(event)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("roll币概率计算器")
        self.setFixedSize(800, 600)
    
        self.setup_ui()

    def setup_ui(self):

        #总币数量
        self.LB_BoxCapacity = QtWidgets.QLabel("总币数 : " , self)
        self.LB_BoxCapacity.move(100, 100)
        self.LE_BoxCapacity = QtWidgets.QLineEdit("10",self)
        self.LE_BoxCapacity.setGeometry(100 + 130, 92, 30, 30)


        #每次roll钱可roll出的钱币数量
        self.LB_RollNum = QtWidgets.QLabel("可roll出钱币数量 : ",self)
        self.LB_RollNum.move(100, 140)
        self.LE_RollNum = QtWidgets.QLineEdit("3",self)
        self.LE_RollNum.setGeometry(100 + 130, 132, 30, 30)

        #相合钱币数量
        self.LB_XHCoinNum = QtWidgets.QLabel("相合钱币数量 : ",self)
        self.LB_XHCoinNum.move(100, 180)
        self.LE_XHCoinNum = QtWidgets.QLineEdit(self)
        self.LE_XHCoinNum.setGeometry(100 + 130, 172, 30, 30)

        #厉 钱币数量
        self.LB_LiCoinNum = QtWidgets.QLabel("厉币数量 (除去相合) : ",self)
        self.LB_LiCoinNum.move(100, 220)
        self.LE_LiCoinNum = QtWidgets.QLineEdit(self)
        self.LE_LiCoinNum.setGeometry(100 + 130, 212, 30, 30)

        #花 钱币数量
        self.LB_HuaCoinNum = QtWidgets.QLabel("花币数量 (除去相合) : ",self)
        self.LB_HuaCoinNum.move(100, 260)
        self.LE_HuaCoinNum = QtWidgets.QLineEdit(self)
        self.LE_HuaCoinNum.setGeometry(100 + 130, 252, 30, 30)

        #衡 钱币数量
        self.LB_HengCoinNum = QtWidgets.QLabel("衡币数量 (除去相合) : ",self)
        self.LB_HengCoinNum.move(100, 300)
        self.LE_HengCoinNum = QtWidgets.QLineEdit(self)
        self.LE_HengCoinNum.setGeometry(100 + 130, 295, 30, 30)

        #开始分析计算按钮
        self.BT_Analysis = QtWidgets.QPushButton("开始分析计算",self)
        self.BT_Analysis.setGeometry(300,260,120,70)
        self.BT_Analysis.clicked.connect(self.connectUIwithFunc)


        #result
        self.LB_res = QtWidgets.QLabel("结果 : ",self)
        self.LB_res.move(20,370)
        self.PTE_res = QtWidgets.QPlainTextEdit(self)
        self.PTE_res.setGeometry(10,400,780,190)
        self.PTE_res.setReadOnly(True)


    #计算概率函数rollCoinPro( 钱盒币总量 , 可roll出币数量  \
    #                                            , 每个类型的钱币数量 )
    #allCoinNum , rollCoinNum , LiCoinNum , HuaCoinNum , HengCoinNum , XHCoinNum
    def rollCoinPro(self,allCoinNum,rollCoinNum,
                                LiCoinNum,HuaCoinNum,HengCoinNum,XHCoinNum):

        
        res = {
            "0 花 : " : 0,
            "1 花 : " : 0,
            "2 花 : " : 0,
            "3 花 : " : 0,
            "至少 1 花 : ": 0,

            "0 衡 : " : 0,
            "1 衡 : " : 0,
            "2 衡 : " : 0,
            "3 衡 : " : 0,
            "至少 1 衡 : ": 0,

            "0 厉 : " : 0,
            "1 厉 : " : 0,
            "2 厉 : " : 0,
            "3 厉 : " : 0,
            "至少 1 厉 : ": 0,
        }

        tempHuaCoinNum = HuaCoinNum + XHCoinNum
        tempOthers = HengCoinNum + LiCoinNum
        res["至少 1 花 : "] = 1 - comb(tempOthers,rollCoinNum) / comb(allCoinNum , rollCoinNum)
        # i = roll出 i 个对应钱
        for i in range(tempHuaCoinNum+1):
            if i > 3:
                break
            probability = (comb(tempHuaCoinNum,i) * comb(tempOthers,rollCoinNum-i)) \
                  /  comb(allCoinNum , rollCoinNum)
            res[f"{i} 花 : "] = probability
        

        tempLiCoinNum = LiCoinNum + XHCoinNum
        tempOthers = HengCoinNum + HuaCoinNum
        res["至少 1 厉 : "] = 1 - comb(tempOthers,rollCoinNum) / comb(allCoinNum , rollCoinNum)
        # i = roll出 i 个对应钱
        for i in range(tempLiCoinNum+1):
            if i > 3:
                break
            probability = (comb(tempLiCoinNum,i) * comb(tempOthers,rollCoinNum-i)) \
                  /  comb(allCoinNum , rollCoinNum)
            res[f"{i} 厉 : "] = probability
        

        tempHengCoinNum = HengCoinNum + XHCoinNum
        tempOthers = HuaCoinNum + LiCoinNum
        res["至少 1 衡 : "] = 1 - comb(tempOthers,rollCoinNum) / comb(allCoinNum , rollCoinNum)
        # i = roll出 i 个对应钱
        for i in range(tempHengCoinNum+1):
            if i > 3:
                break
            probability = (comb(tempHengCoinNum,i) * comb(tempOthers,rollCoinNum-i)) \
                  /  comb(allCoinNum , rollCoinNum)
            res[f"{i} 衡 : "] = probability

        return res

    #通过按钮连接输入和分析函数,并将函数返回结果打印到PTE_res
    def connectUIwithFunc(self):
        self.allCoinNum = int(self.LE_BoxCapacity.text())
        self.rollCoinNum = int(self.LE_RollNum.text())
        self.LiCoinNum = int(self.LE_LiCoinNum.text())
        self.HuaCoinNum = int(self.LE_HuaCoinNum.text())
        self.HengCoinNum = int(self.LE_HengCoinNum.text())
        self.XHCoinNum = int(self.LE_XHCoinNum.text())


        result = self.rollCoinPro(
            self.allCoinNum,
            self.rollCoinNum,
            self.LiCoinNum,
            self.HuaCoinNum,
            self.HengCoinNum,
            self.XHCoinNum
        )

        self.show_result(result)

    def show_result(self, result):
        if (self.LiCoinNum + self.HuaCoinNum + self.HengCoinNum + self.XHCoinNum > self.allCoinNum):
            text = "厉币,花币,衡币,相合币数量之和 大于 当前钱盒容量.  请检查输入信息"
            
            self.PTE_res.setPlainText(text)
            return

        prefixes = ["0", "1", "2", "3", "至少 1"]
        categories = ["厉", "花", "衡"]

        lines = []
        lines.append(f"{'':<20} {'厉':<20} {'花':<20} {'衡':<16}")

        for prefix in prefixes:
            label = f"{prefix} :"
            line = f"{label:<14} "
            for cat in categories:
                key = f"{prefix} {cat} : "
                val = result.get(key, 0)
                line += f"{val:.4%}".ljust(16) + " "
            lines.append(line)

        self.PTE_res.setPlainText("\n".join(lines))

        
        
    





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.setWindowFlag(Qt.WindowStaysOnTopHint, True)
    window.move(1250, 150)
    window.show()
    sys.exit(app.exec())

