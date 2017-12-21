for i in 1a 1b 1c 1d 3a 3b 5 6a 6b 6e 7a
do
cd $i
cp /mnt/scratch/songlin3/run/thrombin/ligand_final/final/$i'_resp'/MD/2.5_us_200.pdb md_equi.pdb
cd wat
cp /mnt/scratch/songlin3/run/thrombin/ligand_final/final/$i'_resp'/wat/2.5_us_200.pdb md_equi.pdb
cd ../..
done
