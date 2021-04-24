#!/usr/bin/env python3
"""
Work in progress as of 4/24/2021


"""
import os
import argparse
import requests

words = []  # Holds words to fuzz with

def parse_wordlist(filePath):
    print('[+] Parsing wordlist @ ' + filePath)
    if os.path.isfile(filePath):
        try:
            with open(filePath, 'r') as f_obj:
                data = f_obj.read().split('\n')
                for i in data:
                    words.append(i)
                f_obj.close()
        except Exception as parsing_error:
            print('[!] Error while parsing: ' + str(parsing_error))
    else:
        print('[!] Please confirm: ' + filePath + ' is a valid path')


def build_url(url):
    print('[+] Building URL...')
    if 'FUZZ' not in url.upper():
        print('[!] Please ensure the word FUZZ is present in target url. ex: http://www.target.com/FUZZ')
    else:
        for word in words:
            print(url.replace('FUZZ', str(word)))

def fuzz_target(url):
    print('[+] Fuzzing Target...')
    fuzz_attempt = requests.get(url)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple web directory fuzzer')

    parser.add_argument('-w', '--wordlist', help='Add a path to a wordlist to fuzz with')
    parser.add_argument('-u', '--url', help='Enter the full url with the word "FUZZ" where you want to fuzz')
    parser.add_argument('-v', '--verbose', help='Verbose will include all possible output')
    # Add filter for showing status or not showing status
    args = parser.parse_args()

    if args.wordlist:
        parse_wordlist(args.wordlist)
    else:
        print('[!] No wordlist detected! Please provide path to wordlist')
    
    build_url(args.url)
