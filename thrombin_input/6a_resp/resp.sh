respgen -i ANTECHAMBER_AC.AC -a additional.in -o I6A.respin1 -f resp1
respgen -i ANTECHAMBER_AC.AC -a additional.in -o I6A.respin2 -f resp2
resp -O -i I6A.respin1 -o I6A.respout1 -e ANTECHAMBER.ESP -t qout_stage1
resp -O -i I6A.respin2 -o I6A.respout2 -e ANTECHAMBER.ESP -q qout_stage1 -t qout_stage2
antechamber -i ANTECHAMBER_AC.AC -fi ac -o I6A_ACE_resp.mol2 -fo mol2 -c rc -cf qout_stage2 -at amber
awk '$4=="I6A" {print}' I6A_ACE.pdb  > I6A.pdb
antechamber -fi pdb -i I6A.pdb -fo mol2 -o I6A.mol2 -at amber
