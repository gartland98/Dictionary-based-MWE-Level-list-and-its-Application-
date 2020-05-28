import os
import nltk


os.chdir('C:/Users/gartl/Documents')

''' sum every MWE files into one'''
spoken_bnc_MWE=open('lemma_spokenBNC_MWElist.txt','r',encoding='utf-8').readlines()
spoken_bnc_MWE=[i.strip() for i in spoken_bnc_MWE]

bnc_MWE=open('lemma_BNC_MWElist.txt','r',encoding='utf-8').readlines()
bnc_MWE=[i.strip() for i in bnc_MWE]

tv0_MWE=open('lemma_TV_MWE0.txt','r',encoding='utf-8').readlines()
tv0_MWE=[i.strip() for i in tv0_MWE]

tv1_MWE=open('lemma_TV_MWE1.txt','r',encoding='utf-8').readlines()
tv1_MWE=[i.strip() for i in tv1_MWE]

tv2_MWE=open('lemma_TV_MWE2.txt','r',encoding='utf-8').readlines()
tv2_MWE=[i.strip() for i in tv2_MWE]

tv3_MWE=open('lemma_TV_MWE3.txt','r',encoding='utf-8').readlines()
tv3_MWE=[i.strip() for i in tv3_MWE]

tv4_MWE=open('lemma_TV_MWE4.txt','r',encoding='utf-8').readlines()
tv4_MWE=[i.strip() for i in tv4_MWE]

tv5_MWE=open('lemma_TV_MWE5.txt','r',encoding='utf-8').readlines()
tv5_MWE=[i.strip() for i in tv5_MWE]

coca_fiction0_MWE=open('lemma_coca_fiction_MWE0.txt.','r',encoding='utf-8').readlines()
coca_fiction0_MWE=[i.strip() for i in coca_fiction0_MWE]
coca_fiction1_MWE=open('lemma_coca_fiction_MWE1.txt.','r',encoding='utf-8').readlines()
coca_fiction1_MWE=[i.strip() for i in coca_fiction1_MWE]

coca_news0_MWE=open('lemma_coca_news_MWE0.txt.','r',encoding='utf-8').readlines()
coca_news0_MWE=[i.strip() for i in coca_news0_MWE]
coca_news1_MWE=open('lemma_coca_news_MWE1.txt.','r',encoding='utf-8').readlines()
coca_news1_MWE=[i.strip() for i in coca_news1_MWE]

coca_megazine0_MWE=open('lemma_coca_megazine_MWE0.txt','r',encoding='utf-8').readlines()
coca_megazine0_MWE=[i.strip() for i in coca_megazine0_MWE]
coca_megazine1_MWE=open('lemma_coca_megazine_MWE1.txt','r',encoding='utf-8').readlines()
coca_megazine1_MWE=[i.strip() for i in coca_megazine1_MWE]

coca_academic0_MWE=open('lemma_coca_academic_MWE0.txt','r',encoding='utf-8').readlines()
coca_academic0_MWE=[i.strip() for i in coca_academic0_MWE]
coca_academic1_MWE=open('lemma_coca_academic_MWE1.txt','r',encoding='utf-8').readlines()
coca_academic1_MWE=[i.strip() for i in coca_academic1_MWE]

MWEs=spoken_bnc_MWE+bnc_MWE+tv0_MWE+tv1_MWE+tv2_MWE+tv3_MWE+tv4_MWE+tv5_MWE+coca_fiction0_MWE+coca_fiction1_MWE+coca_news0_MWE+coca_news1_MWE+coca_megazine0_MWE+coca_megazine1_MWE+coca_academic0_MWE+coca_academic1_MWE
print('MWEs:', len(MWEs))

MWE_freq=nltk.FreqDist(MWEs)
for i in MWE_freq.most_common(30):
    print(i)

MWE_freqdist=open('MWE_freqdist.txt','w',encoding='utf-8')
for i in MWE_freq.most_common():
    MWE_freqdist.write(i[0]+'\t'+str(i[1])+'\n')
MWE_freqdist.close()

print('MWE_freqdist')

MWE_count=open('lemma_MWE_data.txt','w',encoding='utf-8')
for i in MWEs:
    MWE_count.write(i+'\n')
MWE_count.close()

print('MWE_count')