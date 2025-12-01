# def greet(name):
#     print("你好%s先生!" % name)
#     print(f"你好{name}先生!!")


# greet("炭志郎")


def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        # return "閏年"
        print("閏年")
    else:
        # return "平年"
        print("平年")


a = int(input())
# or print(check_leap_year(int(input())))
check_leap_year(a)


def num(s):
    n = 0
    for i in s:
        e = int(i)
        n += e
    print(n)
    return n


usa = '17760704'
print(num(usa))
