#!/usr/bin/env python

from dotenv import load_dotenv
import os
import requests
import sys, getopt

def main(argv):
    verify_env()
    collection, url, files = parse_args(argv)
    post_files(collection, url, files)

    for url in files:
        print(url)

def verify_env():
    if not 'GALLERIA_API_TOKEN' in os.environ:
        sys.exit('First set GALLERIA_API_TOKEN in environment')

def post_files(collection, url, files):
    for file in files:
        post_file(collection, url, file)

def post_file(collection, url, file):
    data = {
        "collection_title": collection,
        "title": os.path.basename(file),
        "image": file
    }
    head = {'Authorization': 'Token {}'.format(os.environ['GALLERIA_API_TOKEN'])}
    requests.post(url, data=data,headers=head)

def parse_args(argv):
    url = 'http://localhost:8000/api/works/'
    collection = None
    try:
        opts, files = getopt.getopt(argv,"hc:u:",["collection=", "url="])
    except getopt.GetoptError:
        print('post.py -c <collection> <file paths>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('post.py -c <collection>')
            sys.exit()
        elif opt in ("-c", "--collection"):
            collection = arg
        elif opt in ("-u", "--url"):
            url = arg
        else:
            files.append(arg)
    return collection, url, files

load_dotenv()
if __name__ == "__main__":
    main(sys.argv[1:])
