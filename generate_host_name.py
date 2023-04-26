# 机 构：中国科学院大学
# 程序员：李浩东
# 时 间：2023/4/17 13:38

num = int(input("请输入需要的长度："))

str_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_2 = "abcdefghijklmnopqrstuvwxyz"

# 产生主机名的字符串
def generate_str(num):
    host_name = ""
    for i in range(26):
        for j in range(26):
            host_name += str_1[i] + str_2[j]
            if len(host_name) > num:
                host_name = host_name[:num]
                return host_name

host_name = generate_str(num)
print(host_name)

with open("host_name.txt", "w") as f:
    f.write(host_name)