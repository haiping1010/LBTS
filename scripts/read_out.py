
fw=open("cof_all_n.pro","w")
index=0
with open("cof_all.pro","r") as f:
  for  line in f:
     if line.startswith('#MOLECULE compound_'):
               index=1
    
     if index==1:
          fw.write(line)
           
     if line.startswith('END'):
          index=0


