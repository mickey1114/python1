fruit = ['apple', 'guava', 'banana', 'watermelon', 'kiiiiiii']

# sorted 排序後面可以加上條件key len長度 second 從哪個字元開始
fruit_len = sorted(fruit, key=len, reverse=True)
print(fruit_len)
fruit_sorted = fruit.sort()
print(fruit_sorted)


# sorted 中的key 可以直接寫函式名稱 會依照函式出來的大小進行排列
# 按照key的規則進行排序 不會改變原本lst的值

def vowel(s):
    v = 'AEIOUaeiou'
    count = 0
    for letter in s:
        if letter in v:
            count += 1
    return count


print(sorted(fruit, key=vowel))


def f(x):
    return x**2


num = [1, -7, 14, 2, -5, 9]
num = sorted(num, key=f)
print(num[-1])
