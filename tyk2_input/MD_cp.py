import os

# parameter set up
dir = '/mnt/home/songlin3/Schrodinger_FEP_set/tyk2_input/'

f = open('muta_list', 'r')

for line in f:
  i, mu_list = line.split()[:2]
  i=i.upper()
  newlist=mu_list.split(',')
  print i
  res2='L'+ i
  os.system("rm -r %s"%(res2))
  os.system("mkdir %s"%(res2))
  resdir = dir + '%s/'%(res2)
  os.chdir(resdir)
  for n in range(0,len(newlist)):
    os.system("mkdir %s-%s_MD"%(i,newlist[n]))
    wdir = resdir + '%s-%s_MD'%(i,newlist[n])
    os.chdir(wdir)
    os.system("cp ../../../tyk2/%s/MD/ti_one-step/%s_%s/0.5_equi_0.rst ."%(res2,i,newlist[n]))
    os.system("cp ../../../tyk2/%s/MD/ti_one-step/%s_%s/set.py run.py"%(res2,i,newlist[n]))
    os.system("cp ../../../tyk2/%s/MD/ti_one-step/%s_%s/%s-%s_merged.* ."%(res2,i,newlist[n],i,newlist[n]))
    os.system("cp ../../../tyk2/%s/MD/ti_one-step/%s_%s/0.5_equi_0.in ."%(res2,i,newlist[n]))
    os.system("cp ../../../tyk2/%s/MD/ti_one-step/%s_%s/equi_0.pbs ."%(res2,i,newlist[n]))
    os.system("cp ../../../tyk2/%s/MD/ti_one-step/%s_%s/*mol2 ."%(res2,i,newlist[n]))
    os.system("cp ../../../tyk2/%s/MD/ti_one-step/%s_%s/*frcmod ."%(res2,i,newlist[n]))
    os.system("mkdir files")
    os.system("cp ../../../tyk2/%s/MD/ti_one-step/%s_%s/files/temp.pbs files/"%(res2,i,newlist[n]))
    os.system("cp ../../../tyk2/%s/MD/ti_one-step/%s_%s/files/temp_equi.in files/"%(res2,i,newlist[n]))
    os.system("cp ../../../tyk2/%s/MD/ti_one-step/%s_%s/files/temp_prod.in files/"%(res2,i,newlist[n]))
    lambd = [ 0.00922, 0.04794, 0.11505, 0.20634, 0.31608, 0.43738, 0.56262, 0.68392, 0.79366, 0.88495, 0.95206, 0.99078]
    for j in lambd:
      os.system("rm -r %6.5f"%(j))
      os.system("mkdir %6.5f"%(j))
      os.system("cp ../../../tyk2/%s/MD/ti_one-step/%s_%s/%6.5f/%6.5f_equi.rst %6.5f/"%(res2,i,newlist[n],j,j,j))
    os.chdir(resdir)
  os.chdir(dir)
