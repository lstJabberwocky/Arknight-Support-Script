#明日方舟四结局洞钱转火脚本


from pynput.mouse import Button, Controller
import pyautogui
import time
import keyboard
import json

print("=" * 50)
print(">>> 明日方舟 - 疯狂钱买火脚本 启动 <<<")
print("=" * 50)

print("请确保票转火,血转火,盾转火已用掉," \
"并且已配置故肆坐标和需要兑换火数量,默认50")
mouse = Controller()

time.sleep(5)

print("运行中")
print("F8 停止")
print("鼠标移到左上角强制退出")

with open("coordinate.json", "r") as f:
    coordinates = json.load(f)

choumouX,choumouY = coordinates["gusi"]
fireCount = 30


while True:
    fireCount-= 1


    # 左上角强制退出
    x, y = pyautogui.position()

    if y >= 1538:
        print("触发左上角紧急停止")
        break


    mouse.position = (choumouX, choumouY)
    mouse.click(Button.left, 1)
    time.sleep(1)


    if y >= 1538:
        print("触发左上角紧急停止")
        break



    mouse.position = (choumouX, choumouY)
    mouse.click(Button.left, 1)
    time.sleep(1)


    if y >= 1538:
        print("触发左上角紧急停止")
        break


    
    # 点击前往节点
    mouse.position = (2375, 1180)
    mouse.click(Button.left, 2)
    time.sleep(0.5)


    mouse.position = (2375, 1180)
    mouse.click(Button.left, 2)
    time.sleep(1)

    if y >= 1538:
        print("触发左上角紧急停止")
        break

    
    for i in range(7):
        mouse.position = (2302, 653)
        mouse.click(Button.left, 1)
        time.sleep(0.5)

        if y >= 1538:
            print("触发左上角紧急停止")
            break


    
    # F8退出
    
    if keyboard.is_pressed("F8"):
        print("已停止")
        break

    if fireCount <= 0 :
        break;