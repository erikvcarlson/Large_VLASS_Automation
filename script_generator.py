from cProfile import run
import sys 
import os
import shutil
import re
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#install("pandas")
sys.path.append('/lustre/aoc/observers/nm-11325/.local/lib/python3.8/site-packages')


import pandas as pd 

archive_directory='https://dl-dsoc.nrao.edu/anonymous/1068855824/irbjqjef5g9248onhmf2qhti37/VLASS2.1.sb38529434.eb38589592.59082.86913579861/'


m = re.search('VLASS(.+?)\/', archive_directory)
 
found = m.group(0)

MS_Name = found[:-1]

#ex: https://dl-dsoc.nrao.edu/anonymous/1053790614/45a79daq3lqcrdkqcbge6r4lfi/VLASS2.1.sb38536469.eb38590168.59084.87988079861/
run_command = 'wget -r --reject "index.html*" -np -nc -nH -e robots=off --cut-dirs=4 ' + archive_directory

#need to change this to whatever it is supposed to be
os.system(run_command) 

#I want the portion of the script starting with VLASS2.* to .ms but not including the .ms

#MS_Name = 'VLASS2.1.sb38536469.eb38590168.59084.87988079861'

allsourcedf = pd.read_csv('No_VLA_Obs_Data_and_MS.csv')
allsourcedf['Coords'] = allsourcedf['Coords'].str.replace(' ',':',n=3)
allsourcedf['Coords'] = allsourcedf['Coords'].str.replace(' ','.')
allsourcedf['Coords'] = allsourcedf['Coords'].str.replace(':+',' +',regex=False)



sig_source_df = allsourcedf[allsourcedf['MeSet'] == MS_Name]
MS_Name = MS_Name + '.ms'

for ind in sig_source_df.index:
  try:
    J_Name = sig_source_df['J-Name'][ind]

    os.makedirs(J_Name)
    os.chdir(J_Name)

    copied_dir_name = 'casa_run_file_' + J_Name[0:4] + J_Name[6:9]  + '_.py'

    shutil.copyfile('/lustre/aoc/observers/nm-11325/data/casa_run_file.py',copied_dir_name)

    with open(copied_dir_name, 'r') as file :
      filedata = file.read()


    filedata = filedata.replace('example.ms',MS_Name)
    filedata = filedata.replace('00:00:00.0 +00.00.00.0',sig_source_df['Coords'][ind])
    filedata = filedata.replace('J0000+0000',J_Name)


    with open(copied_dir_name, 'w') as file :
      file.write(filedata)

    run_command = 'xvfb-run -d /home/casa/packages/pipeline/casa-6.1.3-3-pipeline-2021.1.1.32/bin/casa --pipeline --nogui --nologger -c ' + copied_dir_name
    os.system(run_command)
    os.chdir('/lustre/aoc/observers/nm-11325/data')
  except:
    print('There was an error')
shutil.rmtree('/lustre/aoc/observers/nm-11325/data/' + MS_Name) 