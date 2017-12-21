respgen -i ANTECHAMBER_AC.AC -a additional.in -o I1B.respin1 -f resp1
respgen -i ANTECHAMBER_AC.AC -a additional.in -o I1B.respin2 -f resp2
resp -O -i I1B.respin1 -o I1B.respout1 -e ANTECHAMBER.ESP -t qout_stage1
resp -O -i I1B.respin2 -o I1B.respout2 -e ANTECHAMBER.ESP -q qout_stage1 -t qout_stage2
antechamber -i ANTECHAMBER_AC.AC -fi ac -o I1B_ACE_resp.mol2 -fo mol2 -c rc -cf qout_stage2 -at amber
