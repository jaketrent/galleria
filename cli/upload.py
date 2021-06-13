#!/usr/bin/env python

import boto3
from PIL import Image
import os
import shutil
import sys, getopt

def main(argv):
    verify_env()
    size, bucket_name, directory, files = parse_args(argv)
    temp_dir = setup_tempdir()
    resized_files = resize_files(temp_dir, size, files)
    file_urls = upload_files(bucket_name, directory, resized_files)

    for url in file_urls:
        print(url)

    cleanup_tempdir(temp_dir)

def verify_env():
    if not ('AWS_ACCESS_KEY_ID' in os.environ and 'AWS_SECRET_ACCESS_KEY' in os.environ):
        sys.exit('First set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in the environment')

def setup_tempdir():
    temp_dir = os.path.join(os.getcwd(), "_resize_temp")
    os.makedirs(temp_dir, exist_ok=True)
    return temp_dir

def cleanup_tempdir(dir_path):
    shutil.rmtree(dir_path)

def upload_files(bucket_name, directory, files):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    urls = []
    for file in files:
        urls.append(upload_file(bucket, directory, file))
    return urls

def upload_file(bucket, directory, file):
    # print("Uploading file ", file, "...")
    key = f'{directory}/{os.path.basename(file)}'
    bucket.upload_file(file, key)
    return f'https://{bucket.name}/{key}'

def resize_files(temp_dir, size, files):
    # print(f'Resizing {len(files)} image(s) to {size}px wide...')
    new_paths = []
    for file in files:
        new_paths.append(resize_file(temp_dir, size, file))
    return new_paths

def resize_file(temp_dir, size, file):
    img = Image.open(file)
    img.thumbnail((size, size), Image.ANTIALIAS)
    orig_filename, ext = os.path.splitext(os.path.basename(file))
    new_filename = f'{orig_filename}-{size}px{ext}'
    new_path = os.path.join(temp_dir, new_filename)
    img.save(new_path)
    return new_path

def parse_args(argv):
    size = '1200'
    bucket_name = 'cdn.jaketrent.com'
    directory = 'galleria'
    try:
        opts, files = getopt.getopt(argv,"hs:b:d:",["size=","bucket=","directory="])
    except getopt.GetoptError:
        print('resize.py -s <size> -b <bucket> -d <directory> <file paths>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('resize.py -s <size> -b <bucket>')
            sys.exit()
        elif opt in ("-s", "--size"):
            size = arg
        elif opt in ("-b", "--bucket"):
            bucket_name = arg
        elif opt in ("-d", "--directory"):
            directory = arg
        else:
            files.append(arg)
    return int(size), bucket_name, directory, files

if __name__ == "__main__":
    main(sys.argv[1:])
