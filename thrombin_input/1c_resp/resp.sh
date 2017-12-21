respgen -i ANTECHAMBER_AC.AC -a additional.in -o I1C.respin1 -f resp1
respgen -i ANTECHAMBER_AC.AC -a additional.in -o I1C.respin2 -f resp2
resp -O -i I1C.respin1 -o I1C.respout1 -e ANTECHAMBER.ESP -t qout_stage1
resp -O -i I1C.respin2 -o I1C.respout2 -e ANTECHAMBER.ESP -q qout_stage1 -t qout_stage2
antechamber -i ANTECHAMBER_AC.AC -fi ac -o I1C_ACE_resp.mol2 -fo mol2 -c rc -cf qout_stage2 -at amber
awk '$4=="I1C" {print}' I1C_ACE.pdb  > I1C.pdb
antechamber -fi pdb -i I1C.pdb -fo mol2 -o I1C.mol2 -at amber
