a = -1
d = int(input("请输入起始数:"))
e = int(input("请输入终止数:"))
c = str(input("请输入文件名:"))
with open(c,"r") as f:
	while True:
		b = f.readline()
		a = a + 1
		if not b:
			break
print("文章有" + str(a) + "行")
import os
u = str(os.getcwd() + "/" + c)
print(u)
import linecache
while True:
	test = linecache.getline(u,d)
	print(test)
	d = d + 1
	if d >= e:
		break
cmd = "find * -name " + "\"*.py"\"
print(cmd)
