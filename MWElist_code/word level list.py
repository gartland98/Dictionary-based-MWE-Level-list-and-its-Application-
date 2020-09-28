import os
import matplotlib.pyplot as plt
os.chdir('C:/Users/gartl/Documents/word level list')

word_stat=open('word_stats.txt','r',encoding='utf-8').readlines()
word_stat=[i.strip().split('\t') for i in word_stat]
word_level1=word_stat[:1000]
word_level2=word_stat[1000:2000]
word_level3=word_stat[2000:3000]
word_level4=word_stat[3000:4000]
word_level5=word_stat[4000:5000]
word_level6=word_stat[5000:6000]
word_level7=word_stat[6000:7000]
word_level8=word_stat[7000:8000]
word_level9=word_stat[8000:9000]
word_level10=word_stat[9000:10000]

level1_cutoff=float(word_level1[-1][1])
level2_cutoff=float(word_level2[-1][1])
level3_cutoff=float(word_level3[-1][1])
level4_cutoff=float(word_level4[-1][1])
level5_cutoff=float(word_level5[-1][1])
level6_cutoff=float(word_level6[-1][1])
level7_cutoff=float(word_level7[-1][1])
level8_cutoff=float(word_level8[-1][1])
level9_cutoff=float(word_level9[-1][1])
level10_cutoff=float(word_level10[-1][1])


word_level1_file=open('word_level1.txt','w',encoding='utf-8')
for i in word_level1:
    word_level1_file.write(i[0]+'\t'+i[1]+'\n')
word_level1_file.close()

word_level2_file=open('word_level2.txt','w',encoding='utf-8')
for i in word_level2:
    word_level2_file.write(i[0]+'\t'+i[1]+'\n')
word_level2_file.close()

word_level3_file=open('word_level3.txt','w',encoding='utf-8')
for i in word_level3:
    word_level3_file.write(i[0]+'\t'+i[1]+'\n')
word_level3_file.close()

word_level4_file=open('word_level4.txt','w',encoding='utf-8')
for i in word_level4:
    word_level4_file.write(i[0]+'\t'+i[1]+'\n')
word_level4_file.close()

word_level5_file=open('word_level5.txt','w',encoding='utf-8')
for i in word_level5:
    word_level5_file.write(i[0]+'\t'+i[1]+'\n')
word_level5_file.close()

word_level6_file=open('word_level6.txt','w',encoding='utf-8')
for i in word_level6:
    word_level6_file.write(i[0]+'\t'+i[1]+'\n')
word_level6_file.close()

word_level7_file=open('word_level7.txt','w',encoding='utf-8')
for i in word_level7:
    word_level7_file.write(i[0]+'\t'+i[1]+'\n')
word_level7_file.close()

word_level8_file=open('word_level8.txt','w',encoding='utf-8')
for i in word_level8:
    word_level8_file.write(i[0]+'\t'+i[1]+'\n')
word_level8_file.close()

word_level9_file=open('word_level9.txt','w',encoding='utf-8')
for i in word_level9:
    word_level9_file.write(i[0]+'\t'+i[1]+'\n')
word_level9_file.close()

word_level10_file=open('word_level10.txt','w',encoding='utf-8')
for i in word_level10:
    word_level10_file.write(i[0]+'\t'+i[1]+'\n')
word_level10_file.close()

os.chdir('C:/Users/gartl/Documents/MWE level list')

MWE_stat=open('MWE_stats.txt','r',encoding='utf-8').readlines()
MWE_stat=[i.strip().split('\t') for i in MWE_stat]

MWE_level_top=[i for i in MWE_stat if float(i[1])>level1_cutoff]
MWE_level1=MWE_level_top[:162]
MWE_level2=MWE_level_top[162:162*2]
MWE_level3=MWE_level_top[324:486]
MWE_level4=MWE_level_top[486:648]
MWE_level5=MWE_level_top[648:810]
MWE_level6=MWE_level_top[810:972]
MWE_level7=MWE_level_top[972:1134]
MWE_level8=MWE_level_top[1134:1296]
MWE_level9=MWE_level_top[1296:1458]
MWE_level10=MWE_level_top[1458:1620]
MWE_level11=MWE_level_top[1620:]

MWE_level12=[i for i in MWE_stat if float(i[1])>level2_cutoff and float(i[1])<level1_cutoff]
MWE_level13=[i for i in MWE_stat if float(i[1])>level3_cutoff and float(i[1])<level2_cutoff]
MWE_level14=[i for i in MWE_stat if float(i[1])>level4_cutoff and float(i[1])<level3_cutoff]
MWE_level15=[i for i in MWE_stat if float(i[1])>level5_cutoff and float(i[1])<level4_cutoff]
MWE_level16=[i for i in MWE_stat if float(i[1])>level6_cutoff and float(i[1])<level5_cutoff]
MWE_level17=[i for i in MWE_stat if float(i[1])>level7_cutoff and float(i[1])<level6_cutoff]
MWE_level18=[i for i in MWE_stat if float(i[1])>level8_cutoff and float(i[1])<level7_cutoff]
MWE_level19=[i for i in MWE_stat if float(i[1])>level9_cutoff and float(i[1])<level8_cutoff]
MWE_level20=[i for i in MWE_stat if float(i[1])>level10_cutoff and float(i[1])<level9_cutoff]

print('level1:',len(MWE_level1))
print('level2:',len(MWE_level2))
print('level3:',len(MWE_level3))
print('level4:',len(MWE_level4))
print('level5:',len(MWE_level5))
print('level6:',len(MWE_level6))
print('level7:',len(MWE_level7))
print('level8:',len(MWE_level8))
print('level9:',len(MWE_level9))
print('level10:',len(MWE_level10))
print('level11:',len(MWE_level11))
print('level12:',len(MWE_level12))
print('level13:',len(MWE_level13))
print('level14:',len(MWE_level14))
print('level15:',len(MWE_level15))
print('level16:',len(MWE_level16))
print('level17:',len(MWE_level17))
print('level18:',len(MWE_level18))
print('level19:',len(MWE_level19))
print('level20:',len(MWE_level20))


MWE_level1_file=open('MWE_level1.txt','w',encoding='utf-8')
for i in MWE_level1:
    MWE_level1_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level1_file.close()

MWE_level2_file=open('MWE_level2.txt','w',encoding='utf-8')
for i in MWE_level2:
    MWE_level2_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level2_file.close()

MWE_level3_file=open('MWE_level3.txt','w',encoding='utf-8')
for i in MWE_level3:
    MWE_level3_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level3_file.close()

MWE_level4_file=open('MWE_level4.txt','w',encoding='utf-8')
for i in MWE_level4:
    MWE_level4_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level4_file.close()

MWE_level5_file=open('MWE_level5.txt','w',encoding='utf-8')
for i in MWE_level5:
    MWE_level5_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level5_file.close()

MWE_level6_file=open('MWE_level6.txt','w',encoding='utf-8')
for i in MWE_level6:
    MWE_level6_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level6_file.close()

MWE_level7_file=open('MWE_level7.txt','w',encoding='utf-8')
for i in MWE_level7:
    MWE_level7_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level7_file.close()

MWE_level8_file=open('MWE_level8.txt','w',encoding='utf-8')
for i in MWE_level8:
    MWE_level8_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level8_file.close()

MWE_level9_file=open('MWE_level9.txt','w',encoding='utf-8')
for i in MWE_level9:
    MWE_level9_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level9_file.close()

MWE_level10_file=open('MWE_level10.txt','w',encoding='utf-8')
for i in MWE_level10:
    MWE_level10_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level10_file.close()

MWE_level11_file=open('MWE_level11.txt','w',encoding='utf-8')
for i in MWE_level11:
    MWE_level11_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level11_file.close()

MWE_level12_file=open('MWE_level12.txt','w',encoding='utf-8')
for i in MWE_level12:
    MWE_level12_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level12_file.close()

MWE_level13_file=open('MWE_level13.txt','w',encoding='utf-8')
for i in MWE_level13:
    MWE_level13_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level13_file.close()

MWE_level14_file=open('MWE_level14.txt','w',encoding='utf-8')
for i in MWE_level14:
    MWE_level14_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level14_file.close()

MWE_level15_file=open('MWE_level15.txt','w',encoding='utf-8')
for i in MWE_level15:
    MWE_level15_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level15_file.close()

MWE_level16_file=open('MWE_level16.txt','w',encoding='utf-8')
for i in MWE_level16:
    MWE_level16_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level16_file.close()

MWE_level17_file=open('MWE_level17.txt','w',encoding='utf-8')
for i in MWE_level17:
    MWE_level17_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level17_file.close()

MWE_level18_file=open('MWE_level18.txt','w',encoding='utf-8')
for i in MWE_level18:
    MWE_level18_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level18_file.close()

MWE_level19_file=open('MWE_level19.txt','w',encoding='utf-8')
for i in MWE_level19:
    MWE_level19_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level19_file.close()

MWE_level20_file=open('MWE_level20.txt','w',encoding='utf-8')
for i in MWE_level20:
    MWE_level20_file.write(i[0]+'\t'+i[1]+'\n')
MWE_level20_file.close()

MWE_len=[len(MWE_level1),len(MWE_level2),len(MWE_level3),len(MWE_level4),len(MWE_level5),len(MWE_level6),len(MWE_level7),len(MWE_level8),len(MWE_level9),len(MWE_level10),
         len(MWE_level11), len(MWE_level12),len(MWE_level13), len(MWE_level14),len(MWE_level15),len(MWE_level16),len(MWE_level17), len(MWE_level18),len(MWE_level19),len(MWE_level20)]
MWE_label=['level1-1','level1-2','level1-3','level1-4','level1-5','level1-6','level1-7','level1-8','level1-9','level1-10',
           'level1-11','level12','level13','level14','level15','level16','level17','level18','level19','level20']
MWE_level_label=['L1-1','L1-2','L1-3','L1-4','L1-5','L1-6','L1-7','L1-8','L1-9','L1-10',
           'L1-11','L12','L13','L14','L15','L16','L17','L18','L19','L20']
MWE_labels=['1K','2K','3K','4K','5K','6K','7K','8K','9K','10K']
plt.bar(MWE_level_label,MWE_len,color='grey')
plt.xlabel('MWE level',fontsize='20')
plt.ylim(0,200)
plt.ylabel('The number of MWEs in each level',fontsize='20')
plt.xticks(fontsize='15')
plt.yticks(fontsize='15')
fig=plt.gcf()
fig.set_size_inches(10, 8)
plt.show()
fig.savefig('MWE level histogram_.png')
