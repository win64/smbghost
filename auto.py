import os
handle=open("./vulned.txt","r")
for x in handle:
	os.system('python3 ./exploit.py -ip %s -p %s'%(x.split(':')[0], x.split(':')[1]))
