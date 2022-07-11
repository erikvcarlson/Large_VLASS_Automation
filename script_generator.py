import pandas as pd 
import sys 
import os
import shutil

archive_directory='wwww.example.com'


run_command = 'wget -r --reject "index.html*" -np -nH -e robots=off --cut-dirs=3 archive_directory' + archive_directory

#need to change this to whatever it is supposed to be
os.system(run_command) 

#I want the portion of the script starting with VLASS2.* to .ms 
MS_Name = str(sys.argv[1])

allsourcedf = pd.read_csv('general_csv_ex.csv')
sig_source_df = allsourcedf['MeSet'].iloc[MS_Name]

J_Name = sig_source_df['J-Name']

#fix 
shutil.mkdir(J_Name)
shutil.chdir(J_Name)

copied_dir_name = 'casa_run_file_' + J_Name[0~4] + J_Name[6~9]  '_.py'

shutil.copyfile('/luste/aoc/observers/nm-11325/data/casa_run_file.py',copied_dir_name)

with open(copied_dir_name, 'r') as file :
  filedata = file.read()


filedata = filedata.replace('example.ms',MS_Name)
filedata = filedata.replace('00:00:00.0 +00.00.00.0',sig_source_df['Coords'])
filedata = filedata.replace('J0000+0000',J_Name)


with open(copied_dir_name, 'w') as file :
    file.write(filedata)

run_command = 'xvfb-run -d /home/casa/packages/pipeline/casa-6.1.3-3-pipeline-2021.1.1.32/bin/casa --pipeline --nogui --nologger -c ' + copied_dir_name