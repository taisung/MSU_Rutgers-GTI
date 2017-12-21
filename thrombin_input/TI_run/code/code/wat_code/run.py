import os

dir = '/mnt/ls15/scratch/users/songlin3/run/thrombin/ligand_final/final/TTT_resp/wat/ti_one-step/'
res2list=LIST1

for i in res2list:
  a=i.upper()
  print a
  workdir = dir + "TTT_%s"%(i) + "/"
  os.chdir(workdir)
  os.system("cp -r ../input-files/temp.pbs files")
  os.system("sed -i 's/YYY/%s/g' files/temp.pbs"%(i))
  os.system("python set.py")
  os.chdir(dir)
