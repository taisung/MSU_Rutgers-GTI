respgen -i ANTECHAMBER_AC.AC -a additional.in -o I6E.respin1 -f resp1
respgen -i ANTECHAMBER_AC.AC -a additional.in -o I6E.respin2 -f resp2
resp -O -i I6E.respin1 -o I6E.respout1 -e ANTECHAMBER.ESP -t qout_stage1
resp -O -i I6E.respin2 -o I6E.respout2 -e ANTECHAMBER.ESP -q qout_stage1 -t qout_stage2
antechamber -i ANTECHAMBER_AC.AC -fi ac -o I6E_ACE_resp.mol2 -fo mol2 -c rc -cf qout_stage2 -at amber
awk '$4=="I6E" {print}' I6E_ACE.pdb  > I6E.pdb
antechamber -fi pdb -i I6E.pdb -fo mol2 -o I6E.mol2 -at amber
