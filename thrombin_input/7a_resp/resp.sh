respgen -i ANTECHAMBER_AC.AC -a additional.in -o I7A.respin1 -f resp1
respgen -i ANTECHAMBER_AC.AC -a additional.in -o I7A.respin2 -f resp2
resp -O -i I7A.respin1 -o I7A.respout1 -e ANTECHAMBER.ESP -t qout_stage1
resp -O -i I7A.respin2 -o I7A.respout2 -e ANTECHAMBER.ESP -q qout_stage1 -t qout_stage2
antechamber -i ANTECHAMBER_AC.AC -fi ac -o I7A_ACE_resp.mol2 -fo mol2 -c rc -cf qout_stage2 -at amber
awk '$4=="I7A" {print}' I7A_ACE.pdb  > I7A.pdb
antechamber -fi pdb -i I7A.pdb -fo mol2 -o I7A.mol2 -at amber
