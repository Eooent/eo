height = input("请输入您的身高(m):")   # 定义自己的身高和体重。
weight = input("请输入您的体重(kg):")
bmi = float(weight) / (float(height)**2)                   # 定义BMI数值的计算表达式。
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
print("您的BMI指数为：%s" % bmi)
