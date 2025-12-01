fruit = ['pear', 'apple', 'grape']
print(fruit)
print(type(fruit))

lst = ['A', 6, ['True', '8', '7']]
print(lst)

# 如果要複製一個串列的話 要使用a=b[:]
list1 = ['car', 'truck', 'sports car', 'SUV', 'Sedan', 'Coupe', 'Pickup truck']
list2 = list1[:]

list1[0] = 'cybertruck'  # 將串列第0格改成cybertruck
print(list1, list2)

# lst[start:end:step size]
print(list1[1:])
print(list1[:4])

print(f"list1長度為:{len(list1)}")
print("list1字串長度為"+str(len(list1)))
print("list1字串長度為:{}".format(len(list1)))
# f-string 跟 format 都是字串格式化都需要{}當佔位符插入數值

score = [90, 90, 60, 30, 60, 80, 40, 50, 30, 90, 90, 80, 90]

# lst.count(content) 會計算某content在串列中出現幾次
print(f"score裡面有多少個90:{score.count(90)}個")

# 串列-附加 lst.append(content)
list1.append(1)  # append 一次只能插入一個元素到最後一個位子
list1.append("王安石")
print(list1)

# lst.extend(lst2)會改變原來的lst
list1.extend(lst)
print(list1)

# 如果我們不想改變原來的list 可以使用+號 有點像字串的串接
terrestrial_planet = ['Mercury', 'Venus', 'Earth', 'Mars']
gas_giant = ['Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet = terrestrial_planet+gas_giant
print(planet)

# list的插入 lst.insert(index,content)
planet1 = planet
planet1.insert(6, '小行星')
print(planet1)

# list的移除內容 lst.remove(content) 只會移除第一個符合的內容
score.remove(90)
print(score)

# 第二種list移除內容方法 lst.pop(index) 如果不寫會移除最後一個
# 但如果寫上索引值就會移除索引值
last = score.pop()
print(last, score)
fifth_score = score.pop(5)
print(fifth_score, score)

# in用來判斷此內容在不在串列中 傳回值是boolean
print(30 in score)

# lst.sort()排序 lst.reverse() 反轉串列 不會進行傳回
# 要先進行排序 不能直接寫成print(fruit.sort())
fruit.sort()
print(fruit)

# 使用sorted會建立一個新的排序過的串列 原本的串列不會改變
# 會進行傳回 所以可以直接寫在print裡面
print(sorted(terrestrial_planet))
print(terrestrial_planet)
