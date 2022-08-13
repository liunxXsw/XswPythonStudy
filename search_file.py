import os
import sys

# 思路
"""
1, 基础命令为 find * -name xxx  // 这样就能够找到xxx对应的文件
2, find * -name xxx > data      // 将搜索结果导入到data中
3, 使用文件读写的方式来读结果并且打印出来

使用tree命令观察到文件目录如下
[xieshaowen@iZ8vb1kjch99vz9qj9mldfZ test]$ tree
.
├── data
├── dir1
│   └── testfile111
├── dir2
│   └── 123456
├── dir3
│   ├── aaaaaa
│   └── testfile111
├── file
├── find.py
├── search_file.py
├── search.py
├── test2.py
└── test.py

使用 python3 search_file.py testfile111 进行验证

"""

# 使用cmd命令拼凑出来os.system命令要执行的linux命令，这里应该为 find * -name "*xxx*" > file
# 拼接这里有细节，要使用\" 这种转义字符的方式给里面加上 " 字符
cmd = "find  * -name " + "\"*" + sys.argv[1] + "*\"" +  " > file"
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
        
        # 接下来将读到的内容打印出来, content为文件， str(os.getcwd() + "/" + content) 为文件的绝对路径, 用两个变量分别存储这两个数据，然后打印出来

        # 这里将这两行注掉，用下面的代码，放在一行里面去打印，这样比较直观
        # print("查找结果为:" + content)
        # print("目标路径为:" + str(os.getcwd() + "/" + content))

        name = content
        abspath = str(os.getcwd() + "/" + content)
        print("查找结果为 " + name + ", 目标绝对路径为: " + abspath)
        a = str(os.getcwd() + content)
        print("查找结果为 " + name + ", 目标绝对路径为(无): " + a)
# 这里必须要写f.close，否则会有文件句柄泄漏，这个暂时记住要这么写就可以，解释起来比较久且不好理解
f.close
# 删除搜索产生的临时文件 file , file是 22行重定向时指定的名字
os.system("rm -rf file")
