#!/bin/bash
# Author : Ali Snedden
# Date : 07-feb-2024
# License : GPL-3.0
#
#
# How to run : 
#   bash run.sh nprocs ngb niter
#
# Where 
#   nprocs =  is the number of processes to spawn, pick a number equal to or maybe
#             larger than the number of cores on the system
#   ngb : size of the written files in GBs
#   niter : number of iterations to run.
#
# Suggestion : 
#   Try testing 600 process writing 0.00000001 size files for 10000 iterations
#
NPROCS=$1
NGB=$2
NITER=$3
echo "NPROCS = ${NPROCS}"
echo "NGB = ${NGB}"
echo "NITER = ${NITER}"

for((n=0; n<=${NPROCS}; n++)); do
    python thrash.py --niter ${NITER} --ngb ${NGB} --path outfile_${n}.npy > stdout_${n}.txt &
done




