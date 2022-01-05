import os
fpeer=open("peers.txt","r")
lines=fpeer.readlines()
fpeer.close()


def addnode(node):
    cmd="""gethr.exe attach http://localhost:8545 --exec "admin.addPeer('""" + node+ """')\""""
    print(cmd)
    os.system(cmd)




for line in lines:
    line=line.strip()
    if len(line)==0:
        continue
    #print(line)
    addnode(line)
