#明日方舟四结局洞内商店购物脚本


from pynput.mouse import Button, Controller
import pyautogui
import time
import keyboard


mouse = Controller()

print("=" * 50)
print(">>> 明日方舟 - 洞内全币商店疯狂刷币脚本 启动 <<<")
print("=" * 50)

time.sleep(5)

print("运行中")
print("F8 停止")
print("鼠标移到左上角强制退出")


coinCoordinate = [[1000,500],[1400,500],[1800,500],[2200,500],[1000,900],[1400,900]]

buy = [2000,1030]
renew = [750,400]

coinGiveup = [1960,1500]
swapEnter = [2300,1450]
No1coin = [1200,400]
skip = [2400,200]
renewEnter = [1900,1000]

while True:


    for i in coinCoordinate:
        mouse.position = (i[0],i[1])
        mouse.click(Button.left , 1)
        if pyautogui.position()[1] >= 1538:
            print("触发左上角紧急停止")
            break  
        time.sleep(1)

        mouse.position = (buy[0],buy[1])
        mouse.click(Button.left , 1)
        if pyautogui.position()[1] >= 1538:
            print("触发左上角紧急停止")
            break  
        time.sleep(1)

        #和第一个币交换
        mouse.position = (No1coin[0],No1coin[1])
        mouse.click(Button.left , 1)
        if pyautogui.position()[1] >= 1538:
            print("触发左上角紧急停止")
            break  
        time.sleep(1)

        mouse.position = (swapEnter[0],swapEnter[1])
        mouse.click(Button.left , 1)
        if pyautogui.position()[1] >= 1538:
            print("触发左上角紧急停止")
            break  
        time.sleep(1)


        mouse.position = (skip[0],skip[1])
        mouse.click(Button.left , 1)
        if pyautogui.position()[1] >= 1538:
            print("触发左上角紧急停止")
            break  
        


    mouse.position = (renew[0],renew[1])
    mouse.click(Button.left , 1)
    if pyautogui.position()[1] >= 1538:
            print("触发左上角紧急停止")
            break  
    time.sleep(1)
 
    mouse.position = (renewEnter[0],renewEnter[1])
    mouse.click(Button.left , 1)
    if pyautogui.position()[1] >= 1538:
            print("触发左上角紧急停止")
            break  
    time.sleep(1)


    if pyautogui.position()[1] >= 1538:
        print("触发左上角紧急停止")
        break


    
    # F8退出
    
    if keyboard.is_pressed("F8"):
        print("已停止")
        break