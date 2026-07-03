def calculate_BMI(height, weight):
    BMI = weight / (height * height)
    return BMI
weight = input("请输入您的体重(kg):")
height = input("请输入您的身高(m):")
BMI = calculate_BMI(float(height),float(weight))
print(f"您的bmi值为{BMI},您的身体状况为：")
if BMI <= 18.5:
    print("偏瘦")
elif BMI <= 25:
    print("正常")
elif BMI <= 30:
    print("偏肥")
else:
    print("肥胖")
