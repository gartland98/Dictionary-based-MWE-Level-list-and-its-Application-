import nltk
import os
import re

os.chdir('C:/')
os.chdir('C:/Users/jhokay/Downloads')

BNC=open('BNC_spoken_count.txt',encoding='utf-8').readlines()

BNC=[i.strip().lower() for i in BNC]

bnc=[re.findall('[a-z]+',i) for i in BNC]

bnc=[j for i in bnc for j in i if j!='unclearword']

bnc_old=open('BNC_count.txt',encoding='utf-8').readlines()

BNC_old=[i.strip() for i in bnc_old]

total_bncs=bnc+BNC_old

print(len(total_bncs))


error = ['b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

total_bnc=[i for i in total_bncs if i not in error]

print(len(total_bnc))


bnc_sort=nltk.FreqDist(total_bnc)


print(bnc_sort.most_common(50))

phrase_list_file=open('./BNC_level.txt','w',encoding='utf-8')
for i in bnc_sort.most_common():
    phrase_list_file.write(i[0]+'\t'+str(i[1])+'\n')
phrase_list_file.close()





#print([i[1] for i in bnc_sort.most_common() if i[0]=="not"])