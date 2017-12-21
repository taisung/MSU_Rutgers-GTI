import os
import json
fp2 = open('uniq.json','r')
dic2=json.load(fp2)

dir = '/mnt/ls15/scratch/users/songlin3/run/thrombin/ligand_final/final/TTT_resp/wat/ti_one-step/'
res1i='TTT'
res1='NNN'
res2list=LIST1

for i in res2list:
  a=i.upper()
  res2='I'+a
  filesdir = dir + "%s_%s"%(res1i,i) + "/" + "files" + "/"
  os.chdir(filesdir)
  os.system("cp ../../input-files/*in .")
  os.system("cp ../%s-%s_merged.* ."%(res1i,i))
  pdb = file.readlines(open('%s-%s_merged.pdb'%(res1i,i),'r'))
  for line in pdb:
    newlist = []
    newlist = line.split()
    if len(newlist) > 4 and newlist[3] == '%s'%(res1):
      resid1 =  newlist[4]
      os.system("sed -i 's/ZZZ/%s/g' temp_*.in"%(resid1))
      break
  for line in pdb:
    newlist = []
    newlist = line.split()
    if len(newlist) > 4 and newlist[3] == '%s'%(res2):
      resid2 =  newlist[4]
      os.system("sed -i 's/YYY/%s/g' temp_*.in"%(resid2))
      break
  print res1 + '>' + res2
  atmidlist1 = []
  for atom1 in dic2[res1][res2]['%s has uniq'%(res1)]:
    print atom1
    for line in pdb:
      newlist=[]
      newlist = line.split()
      if len(newlist) > 4 and newlist[2] == atom1:
        atomid = newlist[1]
        print atomid
        atmidlist1.append(newlist[1])
  print atmidlist1
  sc1 = '@'
  for num in range(0,len(atmidlist1)):
    sc1 = sc1  + atmidlist1[num] + ','
  print sc1
  os.system("sed -i 's/AAA/%s/g' temp_*in"%(sc1))
  ###res2
  print res2 + '>' + res1
  atmidlist2 = []
  for atom2 in dic2[res2][res1]['%s has uniq'%(res2)]:
    print atom2
    for line in pdb:
      newlist=[]
      newlist = line.split()
      if len(newlist) > 4 and newlist[2] == atom2:
        atomid = newlist[1]
        print atomid
        atmidlist2.append(newlist[1])
  print atmidlist2
  sc2 = '@'
  #print len(atmidlist1)
  for num in range(0,len(atmidlist2)):
    sc2 = sc2  + atmidlist2[num] + ','
  print sc2
  os.system("sed -i 's/BBB/%s/g' temp_*in"%(sc2))
  os.system("cd ..")
  os.chdir(dir)
