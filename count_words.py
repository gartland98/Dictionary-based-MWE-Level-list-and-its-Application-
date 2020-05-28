import os
import nltk

import xml.etree.ElementTree as elemTree
from nltk.corpus import wordnet as wn
import re

os.chdir('C:/Users/gartl/Documents')


''' sum every word files into one'''
spoken_bnc=open('BNC_spoken_count.txt','r',encoding='utf-8').readlines()
spoken_bnc=[i.strip() for i in spoken_bnc]
print('spoken bnc')
bnc=open('BNC_count.txt','r',encoding='utf-8').readlines()
bnc=[i.strip() for i in bnc]
print('bnc')
tv0=open('TVcount0.txt','r',encoding='utf-8').readlines()
tv0=[i.strip() for i in tv0]
print('tv0')
tv1=open('TVcount1.txt','r',encoding='utf-8').readlines()
tv1=[i.strip() for i in tv1]
print('tv1')
tv2=open('TVcount2.txt','r',encoding='utf-8').readlines()
tv2=[i.strip() for i in tv2]
print('tv2')
tv3=open('TVcount3.txt','r',encoding='utf-8').readlines()
tv3=[i.strip() for i in tv3]
print('tv3')
tv4=open('TVcount4.txt','r',encoding='utf-8').readlines()
tv4=[i.strip() for i in tv4]
print('tv4')
tv5=open('TVcount5.txt','r',encoding='utf-8').readlines()
tv5=[i.strip() for i in tv5]
print('tv5')

coca_fiction0=open('coca_fiction_count0.txt.','r',encoding='utf-8').readlines()
coca_fiction0=[i.strip() for i in coca_fiction0]
coca_fiction1=open('coca_fiction_count1.txt.','r',encoding='utf-8').readlines()
coca_fiction1=[i.strip() for i in coca_fiction1]
print('coca_fiction')
coca_news0=open('coca_news_count0.txt.','r',encoding='utf-8').readlines()
coca_news0=[i.strip() for i in coca_news0]
coca_news1=open('coca_news_count1.txt.','r',encoding='utf-8').readlines()
coca_news1=[i.strip() for i in coca_news1]
print('coca_news')
coca_megazine0=open('coca_megazine_count0.txt','r',encoding='utf-8').readlines()
coca_megazine0=[i.strip() for i in coca_megazine0]
coca_megazine1=open('coca_megazine_count1.txt','r',encoding='utf-8').readlines()
coca_megazine1=[i.strip() for i in coca_megazine1]
print('coca_megazine')
coca_academic0=open('coca_academic_count0.txt','r',encoding='utf-8').readlines()
coca_academic0=[i.strip() for i in coca_academic0]
coca_academic1=open('coca_academic_count1.txt','r',encoding='utf-8').readlines()
coca_academic1=[i.strip() for i in coca_academic1]
print('coca_academic')


words=spoken_bnc+bnc+tv0+tv1+tv2+tv3+tv4+tv5+coca_fiction0+coca_fiction1+coca_news0+coca_news1+coca_megazine0+coca_megazine1+coca_academic0+coca_academic1
print('words')
print(len(words))

words_freq={}
for word in words:
    if word in words_freq.keys():
        words_freq[word]+=1
    else:
        words_freq[word]=1

word_freqdist_revise={k:v for k,v in sorted(words_freq.items(), key=lambda item: item[1], reverse=True)}

words_freqdist=open('words_freqdist.txt','w',encoding='utf-8')
for i in word_freqdist_revise.items():
    words_freqdist.write(i[0]+'\t'+str(i[1])+'\n')
words_freqdist.close()

print('words_freqdist')

word_count=open('word_data.txt','w',encoding='utf-8')
for i in words:
    word_count.write(i+'\n')
word_count.close()

print('finished')


