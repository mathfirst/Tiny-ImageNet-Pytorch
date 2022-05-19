# -*- coding: utf-8 -*-
"""
Created on Thu May 19 16:36:38 2022

@author: Kaikai Zhao
description: first put this file under the folder of ./tiny-imagenet-200/val/, 
             then run the command: python3 formatting_TinyImageNet.py.
             
             When you are done, your val folder will contain 200 folders with 50 images in each folder.
"""

import os
from shutil import move

val_dict = {}
with open('./val_annotations.txt', 'r') as f:
    for line in f.readlines():
        split_line = line.split('\t')
        print(split_line)
        val_dict[split_line[0]] = split_line[1] # store filenames as keys and labels as values
        
cnt_folder, cnt_image=0, 0  
for file,label in val_dict.items():
    if not os.path.exists('./' + str(label)):
        cnt_folder = cnt_folder + 1 # 200 folders in total
        print("%d creating a folder named %s" %(cnt_folder,label))
        os.mkdir(label)
        
    cnt_image = cnt_image + 1 # 10,000 images in total
    print(cnt_image)
    source = './images/' + str(file) 
    dest = './' + str(label)
    # move the images in the folder of images to the folder named with their corresponding labels
    move(source,dest) 
    
os.rmdir('./images') # removing this folder is necessary because of the Pytorch dataset format
exit()
