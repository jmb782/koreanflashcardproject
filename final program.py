import csv
import pandas
import ndic
import requests
from bs4 import BeautifulSoup
import urllib

#reads korean to english tsv file as dataframe and renames the columns
dictionary = pandas.read_csv('c://Python//Korean flashcard project//kengdic_2011.tsv.txt', sep =('\t'), dtype='str')
dictionary.columns=['a','b','c','d','e','f','g','h','i','j','k','l']

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

korean_english = []
with open('sample.csv', "r", encoding="utf-8") as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        print(line)
        if
        
#makes dataframe of all the definitions for the korean word "line"
#defdf = dictionary.loc[dictionary['b'] == line, 'd']
#makes dataframe of hanja (chinese character) of korean word "line"        
#hanja = dictionary.loc[dictionary['b'] == line, 'j']

#code to pull sample sentences
#        search_term = urllib.parse.quote(line.strip().encode('utf-8'))
#        baseurl = 'http://endic.naver.com/search_example.nhn?sLn=kr&query='
#        url = baseurl+search_term
#        raw = requests.get(url).text
#        soup = BeautifulSoup(raw, "lxml")
#        sentences = soup.find_all(class_="N=a:xmp.detail", limit=6)


with open('output.csv', 'w', encoding="utf-8") as output:
    for line in korean_english:
        output.write('{}\n'.format(line))
