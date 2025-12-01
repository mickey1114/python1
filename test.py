# python中 字串是不可變序列 而c++是可變序列
# 也就是說python一旦決定了某個字串 便不能改變其中的任何一個字

print("hello")
a = 10
b = 50
print("耶 我開始python入門啦!"+str(a*b))

# 這是python的註解

# 以下是python中的運算子、變數

print((1+100)*100/3)  # 如果只有單斜線 預設就是帶小數點
print(100//3)  # 如果是雙斜線就會是整數 跟Java C++語言相反

print(2**5)  # **代表取冪次方

top = 1
bottom = 100
h = 100
result1 = (top+bottom)*h//2
print(result1)
print(type(result1))
print(type(True))
print(type(None))
print(type(30.0))

# id方法，可以將一個變數所存放的記憶體位子印出來
testa = 10
teatb = testa
print(id(testa))

print(id(teatb))

testa = 25
print(id(testa))

print(id(teatb))

name = input("請輸入姓名:")
print(name)
print(type(name))
