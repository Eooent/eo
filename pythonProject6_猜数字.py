import random
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
