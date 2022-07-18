import pandas as pd
import os
import shutil
import sys
#this script is run in the /data/astrolab/Carlson/Astro/VLASS_Data/Rnd2 folder
Sources = ['J0740+3756','J0912+5650','J0945+1726', 'J1007+5802','J1049+6406','J1214+1631','J1253+4633','J1350+1740','J1548+1935','J1558+1304','J1635+2547', 'J1643+1235','J0744+1825','J0930+1859', 'J1002+1916', 'J1010+1851', 'J1207+1127', 'J1246+2245',  'J1344+2852',  'J1416+6205', 'J1553+1401', 'J1612+2029', 'J1642+1848']
for source in Sources:
    J_Name_of_Source = source

    allsourcedf = pd.read_csv('/data/astrolab/Carlson/Astro/VLASS_Data/Large_VLASS_Automation/No_VLA_Obs_Data_and_MS.csv')
    allsourcedf['Coords'] = allsourcedf['Coords'].str.replace(' ',':',n=3)
    allsourcedf['Coords'] = allsourcedf['Coords'].str.replace(' ','.')
    allsourcedf['Coords'] = allsourcedf['Coords'].str.replace(':+',' +',regex=False)


    sig_source_df = allsourcedf[allsourcedf['J-Name'] == J_Name_of_Source]

    os.chdir('/data/astrolab/Carlson/Astro/VLASS_Data/Rnd2' +  J_Name_of_Source)
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
    shutil.copyfile('/data/astrolab/Carlson/Astro/VLASS_Data/Large_VLASS_Automation/run_SE.sh','working/run_SE.sh')



    with open('working/command_script.py', 'r') as file :
        filedata = file.read()

    filedata = filedata.replace('00:00:00.0 +00.00.00.0',sig_source_df['Coords'].to_string())
    filedata = filedata.replace('J0000+0000',J_Name_of_Source)

    with open('working/command_script.py', 'w') as file :
        file.write(filedata)


    with open('working/run_SE.sh', 'r') as file :
        filedata = file.read()

    filedata = filedata.replace('J0000+0000',J_Name_of_Source)

    with open('working/run_SE.sh', 'w') as file :
        file.write(filedata)
    
    os.system('sbatch working/run_SE.sh')
    os.chdir('/data/astrolab/Carlson/Astro/VLASS_Data/Rnd2')