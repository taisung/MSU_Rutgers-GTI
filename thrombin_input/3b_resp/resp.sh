respgen -i ANTECHAMBER_AC.AC -a additional.in -o I3B.respin1 -f resp1
respgen -i ANTECHAMBER_AC.AC -a additional.in -o I3B.respin2 -f resp2
resp -O -i I3B.respin1 -o I3B.respout1 -e ANTECHAMBER.ESP -t qout_stage1
resp -O -i I3B.respin2 -o I3B.respout2 -e ANTECHAMBER.ESP -q qout_stage1 -t qout_stage2
antechamber -i ANTECHAMBER_AC.AC -fi ac -o I3B_ACE_resp.mol2 -fo mol2 -c rc -cf qout_stage2 -at amber
awk '$4=="I3B" {print}' I3B_ACE.pdb  > I3B.pdb
antechamber -fi pdb -i I3B.pdb -fo mol2 -o I3B.mol2 -at amber
