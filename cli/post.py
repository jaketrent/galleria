#!/usr/bin/env python

from dotenv import load_dotenv
import os
import requests
import sys, getopt

def main(argv):
    verify_env()
    collection, url, files = parse_args(argv)
    posted_urls = post_files(collection, url, files)

    for url in posted_urls:
        print(url)

def verify_env():
    if not 'GALLERIA_API_TOKEN' in os.environ:
        sys.exit('First set GALLERIA_API_TOKEN in environment')

def post_files(collection, url, files):
    posted_urls = []
    for file in files:
        posted_urls.append(post_file(collection, url, file))
    return list(set(posted_urls))

def post_file(collection, url, file):
    data = {
        "collection_title": collection,
        "title": os.path.basename(file),
        "image": file
    }
    head = {'Authorization': 'Token {}'.format(os.environ['GALLERIA_API_TOKEN'])}
    res = requests.post(url, data=data,headers=head)
    if (res.status_code != 201):
        print(res)
        sys.exit('API post failed')
    return res.json()['collection_url']

def parse_args(argv):
    url = 'https://galleria.jaketrent.com/api/works/'
    collection = None
    try:
        opts, files = getopt.getopt(argv,"hc:u:",["collection=", "url="])
    except getopt.GetoptError:
        print('post.py -c <collection> -u <api_url> <file paths>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('post.py -c <collection> -u <api_url> <file paths>')
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
