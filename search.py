import os
import sys
cmd = "grep " +"\"" +sys.argv[1] + "\"" +" * -nr" +  " > file"
os.system(cmd)
with open ("file") as f:
    while True:
        content = f.read()
        print("查找结果为:" + content)
        print("目标路径为:"+str(os.getcwd() + "/" +content))
        if not content:
                break
f.close
