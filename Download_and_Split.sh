#!/bin/bash
#SBATCH --export all #Export all environment variables from the qsub commands environment to the batch job.
#SBATCH -D /lustre/aoc/observers/nm-11325/data  # Working directory (PBS_O_WORKDIR) set to your Lustre area
#SBATCH -n 1   #Number of nodes and the number of cores request
#SBATCH --ntasks=1
#SBATCH --mail-type =END,FAIL  # Send mail on begin, end and abort
#SBATCH --exclusive
#SBATCH --nice 
python3 /lustre/aoc/observers/nm-11325/data/script_generator.py 

