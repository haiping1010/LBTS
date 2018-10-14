import sys

name_list=[]
fw=open(sys.argv[1].replace(".pro", "")+'_n_nonredundent',"w")
index=0
with open(sys.argv[1],"r") as f:
  for  line in f:
     line=line.strip()
     if line.startswith('#MOLECULE compound_')  and line[19:] not in  name_list:
            name_list.append(line[19:])
            index=1
    
     if index==1:
          fw.write(line+"\n")
           
     if line.startswith('END'):
          index=0


