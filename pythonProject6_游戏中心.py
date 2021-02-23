import random
import sys
Id = "1205526615"
card = "15029541492"
count = 1
while True:
    count += 1
    user = input("请输入账号:")
    index = input("请输入密码:")
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
while True:
    print("游戏菜单")
    print("1.选择游戏")
    print("2.退出")

    choice = input("请选择:")
    if choice == "1":
        while True:
            print("请选择游戏")
            print("1.石头剪子布")
            print("2.猜数字")
            print("3.BMI计算器")
            print("4.返回上一界面")

            choice = input("请选择游戏")
            if choice == "1":
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

            elif choice == "2":
                index = 0
                computer = random.randint(0, 10)
                while True:
                    user = int(input("请输入您的数字:"))
                    index += 1
                    if user > computer:
                        print("猜大了，请再试一次!!![您已经猜了%s次了]" % index)
                        continue
                    elif user < computer:
                        print("猜小了，请再试一次!!![您已经猜了%s次了]" % index)
                    elif int(user) == computer:
                        print("恭喜你，猜对了数字就是%s!!![您共猜了%s次了]" % (computer, index))
                        break
                print("游戏结束")
            elif choice == "3":
                height = input("请输入您的身高(m):")  # 定义自己的身高和体重。
                weight = input("请输入您的体重(kg):")
                bmi = float(weight) / (float(height) ** 2)  # 定义BMI数值的计算表达式。
                # 进行逻辑判断
                if bmi < 18.5:
                    print("过轻")
                elif 18.5 <= bmi < 24:
                    print("正常")
                elif 24 <= bmi < 27:
                    print("过重")
                elif 27 <= bmi < 30:
                    print("轻度肥胖")
                elif 30 <= bmi < 35:
                    print("中度肥胖")
                elif bmi >= 35:
                    print("重度肥胖")
                    break
                print("您的BMI指数为：%s" % bmi)
            elif choice == "4":
                break
            else:
                print("没有这个选项，请重新输入")
            while True:
                print("退出到上一页面")
                break
    elif choice == "2":
        print("谢谢光临，欢迎下次惠顾，程序即将退出!!!")
        sys.exit(1)
    else:
        print("没有这个选项，请重新输入")
