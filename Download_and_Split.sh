#!/bin/bash
#PBS -V #Export all environment variables from the qsub commands environment to the batch job.
#PBS -d /lustre/aoc/observers/nm-11325/data  # Working directory (PBS_O_WORKDIR) set to your Lustre area
#PBS -l nodes=1:ppn=1   #Number of nodes and the number of cores request
#PBS -m ae  # Send mail on begin, end and abort

python3 /lustre/aoc/observers/nm-11325/data/script_generator.py 

