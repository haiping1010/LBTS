import os
import os
import shutil
if (len(os.sys.argv)<2):

    print "usage: python compare.py file1 file2"


nf=open(os.sys.argv[1], 'r')
old=[]
oldvalue=[]
oldline=[]

print os.sys.argv[1]
newlines=nf.readlines()

f=open(os.sys.argv[2], 'r')

lines=f.readlines()
for newname in newlines:
    old=[]
    oldvalue=[]
    oldline=[]
    #print newname
    for name in lines:
         index=0
         arrtem=name.split()
         # print name
         #print newname[0:4].upper(),name[0:4].upper()

         if newname[0:4].upper() == arrtem[1][0:4].upper():
                 index=index+1
                 if arrtem[0] < oldvalue:
                     oldline=oldline   
                 if arrtem[0] >= oldvalue:
                       oldvalue=arrtem[0]
                       oldline=newname.strip() + "  " + name.strip()
                       #print oldline
    if index==1:
        oldline=newname.strip() + "  " + name.strip()
        print oldline
    if  oldline != []:
        print oldline
#print oldline
