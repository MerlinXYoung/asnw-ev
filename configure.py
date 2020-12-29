#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import sys
from multiprocessing import cpu_count
sys.path.append(os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'python'))
# import Download from downloads
from downloads import Download
from uncompress import un_tar 
from uncompress import un_zip

cwd = os.getcwd()
download_dir = os.path.join(cwd, '.downloads')
prefix = os.path.join(cwd, '3rd')


depends=[{
        'name': 'libev',
        'url': 'http://dist.schmorp.de/libev/libev-4.33.tar.gz',
        'package': 'libev-4.33.tgz',
        'pname': 'libev-4.33',
        'work_dir': '',
        'configure_commands':['./configure --prefix=%s' %  os.path.join(prefix, 'libev')],
        'build_commands':[
            'make',
            'make install'
        ]
    }
]



def main():
    os.makedirs(download_dir, exist_ok=True)
    os.makedirs(prefix, exist_ok=True)
    for item in depends:
        package = os.path.join(download_dir,item['package'])
        if not os.path.exists(package):
            Download(item['url'], package)
        if os.path.splitext(item['package'])[-1] == ".zip":
            un_zip(package)
        else:
            un_tar(package, download_dir)

        os.chdir(os.path.join(download_dir, item['pname']))
        if not item['work_dir'] == '':
            work_dir = os.path.join(os.getcwd(),item['work_dir'])
            os.makedirs(work_dir, exist_ok=True)
            os.chdir(work_dir)

        for cmd in item['configure_commands']:
            if os.system(cmd) != 0:
                print('configure %s error!' % item['pname'])
                exit(1)

        for cmd in item['build_commands']:
            if os.system(cmd) != 0:
                print('build %s error!' % item['pname'])
                exit(1)



    

if __name__ == '__main__':
    main()