%RWF=myrwf
%NoSave
%chk=esp.chk
%NprocShared=4
%Mem=16GB
#HF/CEP-31G SCF=tight Test Pop=MK iop(6/33=2) iop(6/42=6) opt
#Pop=ReadRadii iop(6/50=1)

remark line goes here

0   1
    H    6.2289090000       -1.2485470000       -0.8902070000     
    C    5.2206390000       -1.1110950000       -1.2729760000     
    H    4.8134900000       -2.0758750000       -1.5659940000     
    H    5.2820220000       -0.4664570000       -2.1461900000     
    C    4.3813220000       -0.4174370000       -0.2065620000     
    O    4.7006620000        0.6998690000        0.2448340000     
    H   -1.7497330000        2.3474450000       -0.8284130000     
    H    0.5066320000        3.3637300000       -0.6386260000     
    C   -0.9367970000        1.7802850000       -0.4130920000     
    C    0.3487030000        2.3524980000       -0.3033990000     
    I   -3.0682260000       -0.4263410000       -0.1133040000     
    C   -1.1318190000        0.4611240000        0.0338140000     
    C    1.4179450000        1.6198310000        0.2412120000     
    H    2.3955430000        2.0602530000        0.3203240000     
    C   -0.0700380000       -0.2854920000        0.5823940000     
    C    1.2143510000        0.2918820000        0.6834360000     
    H   -0.2371970000       -1.2905350000        0.9277080000     
    H    2.9787410000        0.1087870000        1.9072810000     
    C    2.3741820000       -0.5172210000        1.2641630000     
    H    1.9918970000       -1.3433510000        1.8560620000     
    N    3.2675310000       -1.0797010000        0.2343920000     
    H    3.0167130000       -1.9466940000       -0.1902000000     

I         1.99

final.esp

I         1.99

final.esp


