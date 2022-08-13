import os
import sys
cmd = "find * -name " +"\"" +sys.argv[1] + "\"" + " > data"
os.system(cmd)
with open ("data") as f:
    while True:
        content = f.read()
        print("查找结果为:" + content)
        print("目标路径为:" + str(os.getcwd() + content))
        if not content:
            break

