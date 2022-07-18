import pandas as pd
import os
import shutil
import sys


J_Name_of_Source = str(sys.argv[1])

allsourcedf = pd.read_csv('/data/astrolab/Carlson/Astro/VLASS_Data/Large_VLASS_Automation/No_VLA_Obs_Data_and_MS.csv')
allsourcedf['Coords'] = allsourcedf['Coords'].str.replace(' ',':',n=3)
allsourcedf['Coords'] = allsourcedf['Coords'].str.replace(' ','.')
allsourcedf['Coords'] = allsourcedf['Coords'].str.replace(':+',' +',regex=False)


sig_source_df = allsourcedf[allsourcedf['J-Name'] == J_Name_of_Source]


os.makedirs("working")

shutil.copyfile('/data/astrolab/Carlson/Astro/VLASS_Data/Large_VLASS_Automation/command_script.py','working/command_script.py')
MS_Name = J_Name_of_Source + '_split.ms'

shutil.move(MS_Name,'working/'+ MS_Name)

with open('working/command_script.py', 'r') as file :
    filedata = file.read()

filedata = filedata.replace('example.ms',MS_Name)

with open('working/command_script.py', 'w') as file :
    file.write(filedata)


filedata = filedata.replace('00:00:00.0 +00.00.00.0',sig_source_df['Coords'].to_string())

shutil.copyfile('/data/astrolab/Carlson/Astro/VLASS_Data/Large_VLASS_Automation/command_script.py','working/SEIP_parameter.list')


with open('working/command_script.py', 'r') as file :
    filedata = file.read()

filedata = filedata.replace('00:00:00.0 +00.00.00.0',sig_source_df['Coords'].to_string())
filedata = filedata.replace('J0000+0000',J_Name_of_Source)

with open('working/command_script.py', 'w') as file :
    file.write(filedata)
