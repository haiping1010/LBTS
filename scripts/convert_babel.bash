
##for i in 9
for i in {1..9}
  do
#echo $i""???_?_*.pdb
babel -ipdb  $i""???_?_*.pdb  -omol2  'all.pro_'$i'.mol2'  -h

done
