import os
import shutil

base_path = 'result'
male_path = base_path+'/Male'
female_path = base_path+'/Female'

os.makedirs(male_path,exist_ok=True)
os.makedirs(female_path,exist_ok=True)


all_files = []
for root,dirs,files in os.walk(base_path):
    for file in files:
        if file.endswith('.png'):
            all_files.append(os.path.join(root,file))
                             
for i in all_files:
    if 'FEMALE' in i:
        shutil.move(i,female_path)
    else:
        shutil.move(i,male_path)
