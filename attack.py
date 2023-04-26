# 机 构：中国科学院大学
# 程序员：李浩东
# 时 间：2023/4/17 14:28

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个IPV4的套接字对象
sock.connect(("192.168.47.128", 21))  # 连接FTP服务器，"192.168.47.128"为FTP服务器的IP地址，21为FTP协议的默认端口号

with open("host_name.txt", "r") as f:
    host_name = f.read()

host_name = host_name.encode('utf-8')

sock.send(b"USER " + host_name + b"\r\n\0")  # 向FTP服务器发送用户名，b"\r\n\0"这个字节序列通常用于在网络协议中作为字符串结束的标志

sock.send(b"666888\r\n")  # 向FTP服务器发送密码，b"\r\n" 这个字节序列通常用于表明一行文本的结束

sock.close()  # 关闭连接
