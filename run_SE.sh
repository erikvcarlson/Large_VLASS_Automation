#!/bin/bash

#SBATCH --cpus-per-task=4   # Amount of memory needed by each process (ppn) in the job.
#SBATCH -D /data/astrolab/Carlson/Astro/VLASS_Data/Rnd2/J0000+0000/working/ # Working directory (PBS_O_WORKDIR) set to your Lustre area
#SBATCH --mem=64GB
#SBATCH --mail-type=END,FAIL                 # Send mail on begin, end and abort
#SBATCH --mail-user=erikvcarlson@uri.edu

module load Xvfb/1.20.13-GCCcore-11.2.0
module load CASA


# casa's python requires a DISPLAY for matplot, so create a virtual X server
xvfb-run -a casa --pipeline --nogui --nologger -c command_script.py