# thrash_gpfs
#### Author : Ali Snedden
#### License : GPL-3.0
#### Date : 07-feb-2024

### Description :
This code is intended to thrash our gpfs file system.  It contains a shell script 
that uses a loop to spawn N python processes that allocate memory, write a file, 
read that same file and repeat.  It uses np.zeros(), which (I believe) calls mmap()
behind the scenes, which does not play well with GPFS.


### Recommendation :
DO NOT RUN THIS ON A PRODUCTION FILE SYSTEM!!!! 

This code attempts to stress/break the file system.  Use common sense on this one.


### How To Run :
```
bash start_thrash.sh nprocs ngb nitir
```

Where 
1. `nprocs` : is the number of processes to spawn, pick a number equal to or
              maybe larger than the number of cores on the system
2. `ngb`    : size of the written files in GBs
3. `niter`  : number of iterations to run.


