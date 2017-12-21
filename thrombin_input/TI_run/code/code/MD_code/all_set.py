import os
import json
fp2 = open('uniq.json','r')
dic2=json.load(fp2)

# parameter set up
dir = '/mnt/ls15/scratch/users/songlin3/run/thrombin/ligand_final/final/TTT_resp/MD/ti_one-step/'
res1i='TTT'
res1='NNN'
res2list=LIST1

#need input files: uniq.json, protein.pdb, ions_wat.pdb, mol2, frcmod, tleap.in, 

#need to modify files: set.py, temp.pbs

for i in res2list:
  res2='I'+ i.upper()
  os.system("rm -r %s_%s"%(res1i,i))
  os.system("mkdir %s_%s"%(res1i,i))
  workdir = dir + "%s_%s"%(res1i,i) + "/"
  os.chdir(workdir)
  os.system("cp ../files/protein.pdb %s_protein.pdb"%(res1))
  pdb = open('%s_protein.pdb'%(res1),'r')
  pdb_cp = open('%s_protein.pdb'%(res2),'w')
  for line in pdb:
    newlist=[]
    newlist=line.split()
    if len(newlist) > 4 and  newlist[3] == '%s'%(res1) and newlist[2] not in dic2[res1][res2]['%s has uniq'%(res1)]:
        line = line.replace(newlist[3],res2)
        pdb_cp.write(line)
    elif newlist[3] != '%s'%(res1):
        pdb_cp.write(line)
  pdb_cp.close()
  os.system("cp ../files/ions_wat.pdb .")
  os.system("cat %s_protein.pdb %s_protein.pdb ions_wat.pdb > twoprotein.pdb"%(res1,res2))
  os.system("pdb4amber -i twoprotein.pdb > twoprotein_sort.pdb")
  os.system("cp ../files/*.in .")
  os.system("sed -i 's/XXX/%s/g' tleap.in"%(res2))
  os.system("sed -i 's/YYY/%s/g' tleap.in"%(i))
  os.system("cp ../files/%s.mol2 ."%(res2))
  os.system("cp ../files/%s.mol2 ."%(res1))
  os.system("cp ../files/ligand.frcmod .")
  os.system("tleap -s -f tleap.in")
  os.system("cp ../files/set.py .")
  os.system("sed -i 's/YYY/%s/g' set.py"%(i))
  os.system("cp -r ../input-files files")
  os.system("sed -i 's/YYY/%s/g' files/temp.pbs"%(i))
  os.chdir(dir)
