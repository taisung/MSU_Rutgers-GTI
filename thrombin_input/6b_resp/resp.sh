respgen -i ANTECHAMBER_AC.AC -a additional.in -o I6B.respin1 -f resp1
respgen -i ANTECHAMBER_AC.AC -a additional.in -o I6B.respin2 -f resp2
resp -O -i I6B.respin1 -o I6B.respout1 -e ANTECHAMBER.ESP -t qout_stage1
resp -O -i I6B.respin2 -o I6B.respout2 -e ANTECHAMBER.ESP -q qout_stage1 -t qout_stage2
antechamber -i ANTECHAMBER_AC.AC -fi ac -o I6B_ACE_resp.mol2 -fo mol2 -c rc -cf qout_stage2 -at amber
awk '$4=="I6B" {print}' I6B_ACE.pdb  > I6B.pdb
antechamber -fi pdb -i I6B.pdb -fo mol2 -o I6B.mol2 -at amber
