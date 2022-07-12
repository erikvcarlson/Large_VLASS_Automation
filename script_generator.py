from cProfile import run
import pandas as pd 
import sys 
import os
import shutil
import re

archive_directory='wwww.example.com'


m = re.search('VLASS(.+?)\/', archive_directory)
if m:
    found = m.match(1)

MS_Name = found[:-1]

#ex: https://dl-dsoc.nrao.edu/anonymous/1053790614/45a79daq3lqcrdkqcbge6r4lfi/VLASS2.1.sb38536469.eb38590168.59084.87988079861/
run_command = 'wget -r --reject "index.html*" -np -nH -e robots=off --cut-dirs=3 archive_directory' + archive_directory

#need to change this to whatever it is supposed to be
os.system(run_command) 

#I want the portion of the script starting with VLASS2.* to .ms 

allsourcedf = pd.read_csv('general_csv_ex.csv')
sig_source_df = allsourcedf['MeSet'].iloc[MS_Name]

J_Name = sig_source_df['J-Name']

os.makedirs(J_Name)
os.chdir(J_Name)

copied_dir_name = 'casa_run_file_' + J_Name[0~4] + J_Name[6~9]  '_.py'

shutil.copyfile('/luste/aoc/observers/nm-11325/data/casa_run_file.py',copied_dir_name)

with open(copied_dir_name, 'r') as file :
  filedata = file.read()

MS_Name = MS_Name + '.ms'
filedata = filedata.replace('example.ms',MS_Name)
filedata = filedata.replace('00:00:00.0 +00.00.00.0',sig_source_df['Coords'])
filedata = filedata.replace('J0000+0000',J_Name)


with open(copied_dir_name, 'w') as file :
    file.write(filedata)

run_command = 'xvfb-run -d /home/casa/packages/pipeline/casa-6.1.3-3-pipeline-2021.1.1.32/bin/casa --pipeline --nogui --nologger -c ' + copied_dir_name
os.system(run_command)