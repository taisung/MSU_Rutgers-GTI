import os

dir = '/mnt/scratch/songlin3/run/thrombin/ligand_final/final/6e_resp/MD/ti_one-step/6e_1d/'
filesdir = dir + 'files/'
temp_equiin = filesdir + 'temp_equi.in'
temp_prodin = filesdir + 'temp_prod.in'
temp_pbs = filesdir + 'temp.pbs'

lambd = [ 0.00922, 0.04794, 0.11505, 0.20634, 0.31608, 0.43738, 0.56262, 0.68392, 0.79366, 0.88495, 0.95206, 0.99078]
for j in lambd:
  os.system("rm -r %6.5f" %(j)) 
  os.system("mkdir %6.5f" %(j)) 
  os.chdir("%6.5f" %(j))
  os.system("rm *")
  workdir = dir + "%6.5f" %(j) + '/'
  #equiin
  eqin = workdir + "%6.5f_equi.in" %(j)
  os.system("cp %s %s" %(temp_equiin, eqin))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, eqin))
  #prodin
  prodin = workdir + "%6.5f_prod.in" %(j)
  os.system("cp %s %s" %(temp_prodin, prodin))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, prodin))
  #PBS
  pbs = workdir + "%6.5f.pbs" %(j)
  os.system("cp %s %s" %(temp_pbs, pbs))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, pbs))
  #top
  os.system("cp ../6e-1d_merged.prmtop .")
  os.system("cp ../6e-1d_merged.inpcrd .")
  #submit pbs 
  os.system("qsub %s" %(pbs)) 
  os.chdir(dir)
