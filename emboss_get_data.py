import os
dir_list = os.listdir()
for dir in dir_list:
    try:
        command = r'python ./emboss_pepstats.py --email swatantra.5.dhara@gmail.com --sequence ' + dir
        os.system(command)
    except:
        pass