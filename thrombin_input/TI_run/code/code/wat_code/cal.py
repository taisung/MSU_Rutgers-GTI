import os

dir = '/mnt/ls15/scratch/users/songlin3/run/thrombin/ligand_final/final/TTT_resp/wat/ti_one-step/'
res2list=LIST1

for i in res2list:
  os.system("rm -r calcu_TTT_%s"%(i))
  os.system("cp -r calcu calcu_TTT_%s"%(i))
  workdir = dir + 'calcu_TTT_%s'%(i) + '/'
  os.chdir(workdir)
  os.system("sed -i 's/XXX/%s/g' c.sh"%(i))
  os.system("sh c.sh")
  os.chdir(dir)
