import random
computer = random.randint(0, 2)
user = input("请输入您的数字:")
if (user == "0" and computer == 1) or (user == "1" and computer == 2) or (user == "2" and computer == 0):
    print("恭喜您赢了，+2积分")
elif int(user) == computer:
    print("平局")
else:
    print("您输了，-1积分")
