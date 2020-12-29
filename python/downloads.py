#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import urllib.request
import os
import sys
import ssl
from progress.bar import Bar
from progress.spinner import Spinner

ssl._create_default_https_context = ssl._create_unverified_context
# def Download(url, out_name):
#     # Download the file from `url` and save it locally under `file_name`:
#     with urllib.request.urlopen(url) as response, open(out_name, 'wb') as out_file:
#         data = response.read() # a `bytes` object
#         out_file.write(data)

def Download(url, out_name):
    with urllib.request.urlopen(url) as Response:
        Length = Response.getheader('Content-Length')
        BlockSize = 4096  # default value
        os.path.basename
        if Length:
            p = Bar(os.path.basename(out_name), max=int(Length))
        else:
            p = Spinner(os.path.basename(out_name))

        # print("UrlLib len:%s, blocksize:%s " % (Length, BlockSize))
        with open(out_name, 'wb') as out_file:
            # Size = 0
            while True:
                BufferNow = Response.read(BlockSize)
                if not BufferNow:
                    break
                out_file.write(BufferNow)
                p.next(len(BufferNow))
        print()
# def Download(url, out_name):
#     r = requests.get(url, stream=True)

#     size = r.headers['Content-Length']
#     if size:
#         p = Bar(out_name, max=int(size))
#     else:
#         p = Spinner(out_name)

#     with open(out_name, 'wb') as f:
#         for chunk in r.iter_content(chunk_size=1024*50):
#             if chunk: # filter out keep-alive new chunks
#                 p.next(len(chunk))
#                 f.write(chunk)

#     p.finish()
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage:%s url [out_name]')
        sys.exit(1);
    
    url = sys.argv[1]
    out_name = 'tmp'
    if len(sys.argv) > 2:
        out_name = sys.argv[2]

    Download(url, out_name)
    sys.exit(0)