#明日方舟四结局洞,茧成绢roll币刷钱脚本


from pynput.mouse import Button, Controller
import pyautogui
import time
import keyboard

mouse = Controller()

print("=" * 50)
print(">>> 明日方舟 - 疯狂roll币脚本 启动 <<<")
print("=" * 50)

time.sleep(5)

rollCount = 50

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