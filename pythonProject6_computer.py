num1 = float(input("请输入第一个数字:"))
num2 = float(input("请输入第二个数字:"))
opra_t = input("用户输入操作符号: + - * / % :")

ok = True
result = 0
if opra_t == "+":
    result = (num1 + num2)
elif opra_t == "-":
    result = (num1 - num2)
elif opra_t == "*":
    result = (num1 * num2)
elif opra_t == "/":
    result = (num1 / num2)
elif opra_t == "%":
    result = (num1 % num2)
else:
    ok = False
    print("不存在此操作符号")
if ok == True:
    print("运算结果: %s" % result)
