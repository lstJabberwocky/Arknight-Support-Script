from pynput.mouse import Button, Controller
import time
import keyboard

import ctypes
ctypes.windll.user32.SetProcessDPIAware()

mouse = Controller()


#click(x坐标, y坐标, 点击次数, 点击间隔(默认1秒), 鼠标按键(默认左键))
def click(x, y, clickCount, gap=1, button=Button.left):

    mouse.position = (x, y)
    for _ in range(clickCount):
        mouse.click(button, 1)
        time.sleep(gap)

        if y >= 1538:
            print("触发鼠标移动至下方紧急停止")
            return False
        if x <10 and y < 10:
            print("触发鼠标移动至左上角紧急停止")
            return False
        if keyboard.is_pressed('F8'):
            print("触发F8键紧急停止")
            return False
        
    return True

