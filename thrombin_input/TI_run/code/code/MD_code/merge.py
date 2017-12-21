import os

#input parameters:
dir = '/mnt/ls15/scratch/users/songlin3/run/thrombin/ligand_final/final/TTT_resp/MD/ti_one-step/'
res1i='TTT'
res1='NNN'
res2list=LIST1

#need to modify files: merge.in, wat/complex

for i in res2list:
  a=i.upper()
  print a
  os.chdir("%s_%s"%(res1i,i))
  os.system("sed -i 's/YYY/%s/g' merge.in"%(i)) 
  os.system("parmed.py -i merge.in -p %s-%s_complex.prmtop"%(res1i,i))
  os.chdir(dir)
