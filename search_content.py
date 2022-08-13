import os
import sys

# 思路
"""
1, 基础命令为 grep "xxx" * -nr > file  // 这样就能够找到所有内容含有xxx的文件
2, 使用文件读写的方式来读结果并且打印出来

使用 grep "aaa" * -nr 观察到结果如下，有下面三个文件中含有aaa字符串，可以据此来验证
[xieshaowen@iZ8vb1kjch99vz9qj9mldfZ test]$ grep "aaa" * -nr
dir1/testfile111:1:aaaaaaa
search_content.py:19:│   ├── aaaaaa
search_file.py:19:│   ├── aaaaaa

使用 python3 search_content.py aaa 进行验证
经过验证，结果合理

"""

# 使用cmd命令拼凑出来os.system命令要执行的linux命令，这里应该为 grep "xxx" * -nr > file
# 拼接这里有细节，要使用\" 这种转义字符的方式给里面加上 " 字符
cmd = "grep " + "\"" + sys.argv[1] + "\" * -nr" +  " > file"
os.system(cmd)

# 读取文件
with open ("file") as f:
    # 写死循环一直读一行，然后在循环里面写退出条件
    while True:
        # 读一行
        content = f.readline()
        # 如果读到的d内容为空，说明到尾部了，则退出循环
        if not content:
            break
os.getcwd() + "        
        # 接下来将读到的内容打印出来, content为文件， str(os.getcwd() + "/" + content) 为文件的绝对路径, 用两个变量分别存储这两个数据，然后打印出来

        # 这里将这两行注掉，用下面的代码，放在一行里面去打印，这样比较直观
        # print("查找结果为:" + content)
        # print("目标路径为:" + str(os.getcwd() + "/" + content))

        name = content
        abspath = str(os.getcwd() + "/" + content)
        print("查找结果为 " + name + ", 目标绝对路径为: " + abspath)

# 这里必须要写f.close，否则会有文件句柄泄漏，这个暂时记住要这么写就可以，解释起来比较久且不好理解
f.close
# 删除搜索产生的临时文件 file , file是 22行重定向时指定的名字
os.system("rm -rf file")

