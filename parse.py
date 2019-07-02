# Abu Shoeb, Rutgers University
# Created on 30 June 2019
# Modified on 2 July 2019
# This simple scripts reads all emoji counts from emojitracker and saves
# them into a csv file. Simply save emojitracker.com as a html file and
# pass the file name to this parser.
#
# How to run: python parse.py
#
# Requirements: pip install BeautifulSoup

from BeautifulSoup import BeautifulSoup as BSHTML

INPUT_FILE = 'emojitracker-sample.html'
OUTPUT_FILE = 'output-sample.csv' 

INPUT_FILE = 'emojitracker-2-july-2019.html'
OUTPUT_FILE = 'output.csv' 

f = open(OUTPUT_FILE,'w')
f.write('unicode\tname\tcount\n') # write headers

with open(INPUT_FILE) as texts:
    soup = BSHTML(texts)
    lis = soup.findAll('li', attrs = {'class' : 'emoji_char'})
    for li in lis:
        emoji = li['id'].lower()
        name = li['data-title'].lower()
        count = li.find('span', attrs = {'class' : 'score'}).text
        f.write(emoji+'\t"'+name+'"\t'+count+'\n') # write to file

f.close()
