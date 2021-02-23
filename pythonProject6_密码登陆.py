import sys
Id = "1205526615"
card = "15029541492"
count = 1
while True:
    count += 1
    user = input("请输入账号")
    index = input("请输入密码")
    if count > 3:
        print("强制退出")
        sys.exit(1)
    elif user == Id and index == card:
        print("登陆成功")
        break
    elif user != Id:
        print("账号或密码输入错误，请重新输入")
    elif user == Id and index != card:
        print("密码错误，请重新输入")

