# 迴圈的使用

# 迴圈大致分兩種 for and while
# for迴圈更適合使用在已知迴圈數 而while則相反
# while要更注意變數更新 判斷條件 for則是 起始 結束 跟 迴圈數

# for variable in range(start,end,step size):
#     Code
# 迴圈內的程式碼一定要記得縮排 再來range裡的end是一定要設定的
# 其他start 跟 step size 如果沒設就是預設

for num in range(2):
    print(num, end=' ')
print()

for num in range(1, 7):
    print(num, end=' ')
print()

for num in range(1, 7, 2):
    print(num, end=' ')
print()

rock = ['花崗岩', '礫石', '安山岩']
sed = ['砂岩', '頁岩', '石灰岩', '礫石']
integer = [1, 2, 3, 4]

for num in range(len(rock)):
    if rock[num] in sed:
        print(f"{rock[num]}是沉積岩")
    else:
        print(rock[num]+"不是沉積岩")
print('判斷完成')

# # 預設是空白做分割 也可以用, 寫法是 scores.split(',')
# # input=> 90 90 80 50 60 40 30 也可以是 90,90,80,60,30,20

# scores = input()
# scores = scores.split()  # split 是將 多個元素 轉換成 字串清單

# count = 0

# for num in range(len(scores)):
#     if int(scores[num]) >= 60:
#         count += 1
# print('及格人數:' + str(count))

# scores 的另外一種寫法

scores = input()
scores = scores.split()
count = 0
count1 = 0
total = 0
avg = 0
for score in scores:
    total += int(score)
avg = total/(len(scores))
print(avg)


for score in scores:
    if (int(score) >= 60):
        count += 1
    print("及格人數為"+str(count)+" "+score)

slogan = '戰校我最會'
for num in range(len(slogan)):
    print(slogan[num], end='~')

lst1 = [20, 30, 40, 50, 11, 60, 90]
largest = lst1[0]
for num in range(len(lst1)):
    if (largest < lst1[num]):
        largest = lst1[num]

print("\n最大數字為"+str(largest))

# for variable in lst:
#     迴圈內
# 迴圈外

su = ['蘇軾', '蘇轍']
for name in su:
    print(name)

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):  # enumerate 是用來取得index和
    print(index, fruit)

# 以字串使用for迴圈
# for variable in 'string':
#     回圈內
# 迴圈外
s = 'lol'
for alphabet in s:
    print(alphabet)

# 另一種寫法在每一個字元後面加上~
for alphabet in slogan:
    print(alphabet, end='~')

# 計算字元出現次數
string = input()
ss = input()
count = 0
for s in string:
    if s == ss:
        count += 1
print(f"出現了:{count}次")
