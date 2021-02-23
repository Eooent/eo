import random
print("####################")
print("欢迎来到石头剪子布游戏")
print("0标识为石头")
print("1表示为剪刀")
print("2表示为布")
print("游戏结果如果您赢了会+2积分，输了会-1积分")
print("####################")
index = 0
while index < 100:
    index += 1
    computer = random.randint(0, 2)
    user = int(input("请输入您的数字:"))
    if (user == 0 and computer == 1) or (user == 1 and computer == 2) or (user == 2 and computer == 0):
        print("恭喜您赢了，+2积分")
        break
    elif computer == user:
        print("平局")
    else:
        print("您输了，-1积分")
