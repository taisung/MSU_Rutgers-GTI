%RWF=myrwf
%NoSave
%chk=opt.chk
%NprocShared=4
%Mem=16GB
#HF/6-31G* SCF=tight Test Pop=MK iop(6/33=2) iop(6/42=6) opt

remark line goes here

0   1
    H   18.6060000000      -12.9450000000       20.7530000000     
    C   18.1770000000      -11.9780000000       21.0130000000     
    H   18.8350000000      -11.1820000000       20.6640000000     
    H   18.0660000000      -11.9090000000       22.0950000000     
    C   16.7890000000      -11.7920000000       20.3610000000     
    O   16.3130000000      -12.6820000000       19.6530000000     
    H   10.7940000000      -11.4930000000       23.5600000000     
    C   11.6070000000      -11.2560000000       22.8870000000     
    F   11.6290000000       -8.9900000000       23.6640000000     
    H   11.7600000000      -13.2620000000       22.0960000000     
    C   12.1300000000       -9.9480000000       22.8490000000     
    C   12.1530000000      -12.2550000000       22.0550000000     
    C   13.1830000000       -9.6360000000       21.9680000000     
    C   13.2090000000      -11.9430000000       21.1730000000     
    H   13.5780000000       -8.6310000000       21.9530000000     
    H   13.6270000000      -12.7130000000       20.5370000000     
    C   13.7200000000      -10.6280000000       21.1180000000     
    H   14.6150000000      -10.7330000000       19.1720000000     
    H   14.8210000000       -9.1970000000       19.9900000000     
    C   14.8280000000      -10.2760000000       20.1410000000     
    N   16.1560000000      -10.6410000000       20.6070000000     
    H   16.6540000000       -9.9370000000       21.1520000000     


