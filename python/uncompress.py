#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import tarfile 
import zipfile 
import time  
import os

def un_tar(file_name, output_path=None):
    '''unzip tar file'''
    if output_path == None:
        output_path = os.path.dirname(file_name)
    start = time.time()  
    t = tarfile.open(file_name, "r:*")  
    t.extractall(path = output_path)  
    t.close()  
    print ('uncompress %s time:%lf' % (os.path.basename(file_name), time.time()-start))


def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    target_dir = os.path.splitext(file_name)[0]
    if os.path.isdir(target_dir):
        pass
    else:
        os.mkdir(target_dir)
    start = time.time() 
    for names in zip_file.namelist():
        zip_file.extract(names,target_dir)
    zip_file.close()
    print ('uncompress %s time:%lf' % (os.path.basename(file_name), time.time()-start))


