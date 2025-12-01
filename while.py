import random
# while condition:
# first line
# second line
# third line
# outline

'''
num = 0
while num < 3:
    print(num)
    num += 1
'''

'''
max = int(input("將計算1~指定數字的平方和 請輸入指定數字"))
num1 = 1
result = 0
while max >= num1:
    result += num ** 2
    num1 += 1
print(result)
'''

# 計算字元出現幾次 while寫法
'''
string = input()
s = input()
num = 0
count = 0
while num < len(string):
    if s == string[num]:
        count += 1
    num += 1
print(s+f"出現了{count}次")
'''

'''
# 計算平均分數 while寫法

scores = input().split()
count = 0
total = 0
while count < len(scores):
    total += int(scores[count])
    count += 1
avg = total/len(scores)
print(avg)
'''

# 讓使用者猜數字 直到猜中答案

ans = 25
random_num = random.randint(1, 100)
num = int(input("請輸入1~100的數字 進行遊戲"))
while num != random_num:
    if num > random_num:
        print("猜太高了喔")
    elif num < random_num:
        print("猜太低了喔")
    num = int(input("請輸入1~100的數字 進行遊戲"))
print(f"{num}是正確答案")
