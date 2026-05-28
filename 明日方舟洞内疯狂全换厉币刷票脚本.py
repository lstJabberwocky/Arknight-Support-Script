from clickScreenScript import click
import json
import time

print("=" * 50)
print(">>> 明日方舟 - 疯狂刷票 启动 <<<")
print("=" * 50)

time.sleep(5)


# 读取坐标配置
with open("coordinate.json", "r") as f:
    coordinates = json.load(f)

choumouCX, choumouCY = coordinates["choumou"]
qianwangCX, qianwangCY = coordinates["qianwang"]
nextCX, nextCY = coordinates["next"]


while True:
    #点击筹谋
    if not click(choumouCX, choumouCY, 2 , gap = 1):    
        break
    
    #进入筹谋
    if not click(qianwangCX, qianwangCY, 3 , gap = 1):
        break

    #抛出钱盒
    if not click(coordinates["paochuqianhe"][0], coordinates["paochuqianhe"][1], 3 , gap = 1):
        break

    #选择交换厉钱
    if not click(2400,1100, 4 , gap = 1):
        break

    time.sleep(1)

    #重复点击next,收钱
    if not click(nextCX, nextCY, 13 , gap = 0.5):
        break

    #点击√,完成兑换
    if not click(1300,1400, 2 , gap = 1):
        break
    