respgen -i ANTECHAMBER_AC.AC -a additional.in -o I3A.respin1 -f resp1
respgen -i ANTECHAMBER_AC.AC -a additional.in -o I3A.respin2 -f resp2
resp -O -i I3A.respin1 -o I3A.respout1 -e ANTECHAMBER.ESP -t qout_stage1
resp -O -i I3A.respin2 -o I3A.respout2 -e ANTECHAMBER.ESP -q qout_stage1 -t qout_stage2
antechamber -i ANTECHAMBER_AC.AC -fi ac -o I3A_ACE_resp.mol2 -fo mol2 -c rc -cf qout_stage2 -at amber
awk '$4=="I3A" {print}' I3A_ACE.pdb  > I3A.pdb
antechamber -fi pdb -i I3A.pdb -fo mol2 -o I3A.mol2 -at amber
