import os
import sys

# 思路
"""
1, 使用ps -ef|grep xxx > data , 找到xxx名字相关进程对应的pid, 然后重定向到 data 文件中
2, 使用文件读写的方式来读结果并且通过字符串解析的方式找到xxx进程对应的pid
3, 使用 kill -9 xxxpid 的方式杀掉 xxx应用

测试方式，写一个测试应用 thread_test.py 在那里一直跑

使用 python3 thread_killer.py thread_test.py 杀掉 thread_test.py进程

测试方法：
1，先用一个窗口执行 thread_test.py
2，用另一个窗口执行 python3 thread_killer.py thread_test.py， 发现 thread_test.py 被杀掉了

"""

'''
如何 GetPidFromContent ？
[xieshaowen@iZ8vb1kjch99vz9qj9mldfZ test]$ python3 thread_killer.py thread_killer.py
xieshao+  507622  506769  0 20:33 pts/3    00:00:00 python3 thread_killer.py thread_killer.py

xieshao+  507623  507622  0 20:33 pts/3    00:00:00 sh -c ps -ef|grep thread_killer.py > data

xieshao+  507625  507623  0 20:33 pts/3    00:00:00 grep thread_killer.py

我们观察到 每一行的数据有很多的空格，那么每一行可以使用split函数切分空格，然后第二个数据就是我们想要的pid
'''
def GetPidFromContent(content):
    # 这里的rstrip('\n')是删除字符串右侧的换行符
    resList = content.rstrip('\n').split('  ')
    pid = resList[1]
    #print ("pid is " + pid)
    # 这里比较难解释，暂时不用管
    if ("thread_killer.py" in content or "grep" in content):
        return -1
    return int(pid)

# 使用cmd命令拼凑出来os.system命令要执行的linux命令，这里应该为 ps -ef|grep xxx > data
# 拼接这里有细节，要使用\" 这种转义字符的方式给里面加上 " 字符
cmd = "ps -ef|grep "  + sys.argv[1] + " > data"
os.system(cmd)

# 读取文件
with open ("data") as f:
    # 写死循环一直读一行，然后在循环里面写退出条件
    while True:
        # 读一行
        content = f.readline()
        if not content:
            break
        print (content)        

        # 解析content里面的pid, 封装一个函数，传content进去，传pid出来
        pid = GetPidFromContent(content)
        # 只有是我们想要的数据才杀
        if (pid != -1):
            cmd = "kill -9 " + str(pid)
            os.system(cmd)

# 这里必须要写f.close，否则会有文件句柄泄漏，这个暂时记住要这么写就可以，解释起来比较久且不好理解
f.close
# 删除搜索产生的临时文件 data , data是 22行重定向时指定的名字
os.system("rm -rf data")
