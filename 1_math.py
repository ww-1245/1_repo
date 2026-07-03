total = 0
i = 0
num = input("请输入任意数量的数字，按q结束程序：") 
while num != "q":
    total += float(num)
    i += 1
    num = input("请输入任意数量的数字，按q结束程序：")
if i == 0:
    avge =0
else: 
    avge = total / i
print("你输入的数的平均值为：" + str(avge))

    