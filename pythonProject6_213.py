"""
从用户键盘接收用户的输入
记录用户信息
"""
print("请输入您的姓名:", end="")
name = input()

age = input("请输入您的年龄:")

gender = input("请输入您的性别:")

print("       用户信息展示")
print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ")
print("\t用户姓名:" + name)
print("\t用户年龄:" + age)
print("\t用户性别:" + gender)
print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ")
input("(温馨提示)按任意键继续")
