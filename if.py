# 條件判斷 if
# if condition:
#   action
# else:
#   action

# try:
'''
temp = int(input("請輸入溫度:"))
if temp >= 38:
    print("fever")
elif 36 < temp < 38:
    print("healthy")
else:
    print("sick")
'''
# except ValueError:
#     print("請輸入正確的數字!")

# 判斷是不是三角形 是甚麼三角形
a = int(input("請輸入邊長A:"))
b = int(input("請輸入邊長B:"))
c = int(input("請輸入邊長C:"))

if a+b > c and c+b > a and a+c > b:
    if a == b and b == c:
        print("是正三角形")
    else:
        print("是三角形")
else:
    print("非三角形")
