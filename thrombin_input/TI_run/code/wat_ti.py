import os

# parameter set up
dir = '/mnt/ls15/scratch/users/songlin3/run/thrombin/ligand_final/final/'
#res1list=["1c","3a","3b","5","6a","6e","7a"]
res1list=["6a","6e"]

for i in res1list:
  res2='I'+ i.upper()
  wdir = dir + "%s_resp/wat/"%(i)
  os.chdir(wdir)
  os.system("cpptraj wat_%s.prmtop < ptraj.in > out" %(res2))
  os.system("rm -r ti_one-step")
  os.system("cp -r ../../code/wat_code ti_one-step")
  workdir = wdir + "ti_one-step/"
  os.chdir(workdir)
  os.system("sed -i 's/TTT/%s/g' *.py"%(i))
  os.system("sed -i 's/NNN/%s/g' *.py"%(res2))
  filesdir = workdir + 'files/'
  os.chdir(filesdir)
  os.system("cp ../../2.5_us_200.pdb .")
  pdb = file.readlines(open('2.5_us_200.pdb','r'))
  protein = open('protein.pdb','w')
  for line in pdb:
    newlist = []
    newlist = line.split()
    if len(newlist) > 4 and  newlist[3] != "Cl-" and newlist[3] != "WAT":
       protein.write(line)
    elif newlist[0] == "TER" and newlist[2] !="Cl-" and newlist[2] != "WAT":
       protein.write(line)
  iowat = open('ions_wat.pdb','w')
  for line in pdb:
    newlist = []
    newlist = line.split()
    if newlist[0] == "TER" and (newlist[2] == "Cl-" or newlist[2] == "WAT"):
       iowat.write(line)
    if newlist[0] !="TER" and newlist[0] !="END" and (newlist[3] == "Cl-" or newlist[3] == "WAT"):
       iowat.write(line)
  os.system("sed -i 's/TTT/%s/g' *.in"%(i))
  os.system("sed -i 's/NNN/%s/g' *.in"%(res2))
  os.system("sed -i 's/TTT/%s/g' set.py"%(i))
  inpufildir = workdir + 'input-files/'
  os.chdir(inpufildir)
  os.system("sed -i 's/TTT/%s/g' temp.pbs"%(i))
  os.chdir(dir)
