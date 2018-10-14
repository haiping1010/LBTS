name_list=[]
##fw=open("all_n_nonredundant.pro_n","w")
index=0
with open("all.pro","r") as f:
  for  line in f:
     line=line.strip()
     if line.startswith('#MOLECULE compound_')  and line[19:] not in  name_list:
            fws=open(line[19:]+".pdb" ,"w")
            name_list.append(line[19:])
            index=1
    
     if index==1:
          print line+"\n"
          fws.write(line+"\n")
           
     if line.startswith('END') and index==1:
          index=0
          fws.write(line+"\n")



