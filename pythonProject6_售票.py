index = 10
while index > 0:
    index -= 1
    print("售出一张票，剩余%s" % index)
    if index == 2:
        print("恐怖袭击，停止售票")
        break
else:
    print("今天的票全部出售完毕")
print("下班回家")