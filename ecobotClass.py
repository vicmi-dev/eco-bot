# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 18:19:13 2022
@author: kasper
@author: monica
@author: petra
@author: manuel
@author: laura

a collection of handy functions
related to the ecobot (an application to save laptop/cloud storage & energy)

"""

import os
from os.path import join, getsize
import matplotlib.pyplot as plt
from PIL import Image
import os, sys



class ecobot:


    def img_resize(self, img_path, resize_ratio, save_path):
        """
        INPUT: 
            img_folder_path: absolute path to img folder
            resize_ratio: a real number between 0 and 1
        
        """        
        im = Image.open(img_path)
        new_image_height = int(im.size[0] / (1/resize_ratio))
        new_image_width = int(im.size[1] / (1/resize_ratio))
        imResize = im.resize((new_image_height,new_image_width), Image.ANTIALIAS)
        imResize.save(save_path , 'JPEG', quality=90)
        
        return
    
    def img_rescale(self, img_path, x_pixels, y_pixels, save_path):
        """
        INPUT: 
            img_path: absolute path to img
            x_ratio: horizontal number of pixels
            y_ratio: vertical number of pixels
        """
        im = Image.open(img_path)
        imResize = im.resize((x_pixels,y_pixels))
        imResize.save(save_path )
      
        return
    

    def find_large_folders(self, my_folder, threshold):
        """
        INPUT: 
            root: the folder of which all subdirectories will be searched
            threshold: number of bytes (larger than this number will be considered as large)
        """
        big_files = []
        for root, dirs, files in os.walk(my_folder):
            my_bytes = sum(getsize(join(root, name)) for name in files)
    
            if my_bytes > threshold:
                big_files.append([root, my_bytes])
        big_files.sort(key = lambda x: x[1], reverse=True)
        
        return big_files
        

####################################
#                                  #
# EXAMPLE USAGES                   #
#                                  #
####################################

eb = ecobot()


img_path = r'C:\test\Trends_in_atmospheric_CO2_and_global_temperature_change_–_climate_policies_v2.png'
x_pixels = 1920
y_pixels = 1080
save_path = r'C:\test\Trends_in_atmospheric_CO2_and_global_temperature_change_–_climate_policies_v2_scaled.png'
# rescale and save
# in this case the image is re-scaled to fit the Teams background
eb.img_rescale(img_path, x_pixels, y_pixels, save_path)    
 
# show the very biggest folder in the dir-tree under my_folder
my_folder = r'C:\Users\Laura.astola\OneDrive - Accenture\repos'   
threshold = 3000
result = eb.find_large_folders(my_folder, threshold)  
print(result[0])



  