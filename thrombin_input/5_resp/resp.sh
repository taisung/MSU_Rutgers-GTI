respgen -i ANTECHAMBER_AC.AC -a additional.in -o I5.respin1 -f resp1
respgen -i ANTECHAMBER_AC.AC -a additional.in -o I5.respin2 -f resp2
resp -O -i I5.respin1 -o I5.respout1 -e ANTECHAMBER.ESP -t qout_stage1
resp -O -i I5.respin2 -o I5.respout2 -e ANTECHAMBER.ESP -q qout_stage1 -t qout_stage2
antechamber -i ANTECHAMBER_AC.AC -fi ac -o I5_ACE_resp.mol2 -fo mol2 -c rc -cf qout_stage2 -at amber
awk '$4=="I5" {print}' I5_ACE.pdb  > I5.pdb
antechamber -fi pdb -i I5.pdb -fo mol2 -o I5.mol2 -at amber
