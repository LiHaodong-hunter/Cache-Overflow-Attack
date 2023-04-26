# 机 构：中国科学院大学
# 程序员：李浩东
# 时 间：2023/4/17 14:51

str = '4A6A4A69'

str_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_2 = "abcdefghijklmnopqrstuvwxyz"

# 构造大写字母和小写字母组合的字符串列表
str_total = ""
for i in range(0, 26):
    for j in range(0, 26):
            str_total += str_1[i] + str_2[j]

str_sub = ''
for i in range(len(str), 0, -2):
    tmp = int(str[i - 2:i], 16)  # 将两个十六进制字符转换为整型数字
    str_sub += chr(tmp)  # 将整型数字转换为对应的 ASCII 字符
print(str_sub)

print(str_total.find(str_sub))
print(str_total.find('mJnJ'))
print(str_total.find('eLfL'))

# 给定的 str 为 '4A6A4A69'：
# 第一次迭代，i=8：
# str[i-2:i] 等于 '69'
# 将 '69' 转换为十进制整数 105
# 使用 chr() 函数将 105 转换为对应的 ASCII 字符 'i'
# 将 'i' 添加到 str_sub 中
# 第二次迭代，i=6：
# str[i-2:i] 等于 '4A'
# 将 '4A' 转换为十进制整数 74
# 使用 chr() 函数将 74 转换为对应的 ASCII 字符 'J'
# 将 'J' 添加到 str_sub 中
# 第三次迭代，i=4：
# str[i-2:i] 等于 '6A'
# 将 '6A' 转换为十进制整数 106
# 使用 chr() 函数将 106 转换为对应的 ASCII 字符 'j'
# 将 'j' 添加到 str_sub 中
# 第四次迭代，i=2：
# str[i-2:i] 等于 '4A'
# 将 '4A' 转换为十进制整数 74
# 使用 chr() 函数将 74 转换为对应的 ASCII 字符 'J'
# 将 'J' 添加到 str_sub 中
# 最终得到的 str_sub 为字符串 'iJjJ'。
