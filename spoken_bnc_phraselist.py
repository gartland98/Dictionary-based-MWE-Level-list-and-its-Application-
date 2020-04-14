''' since present continuous tense can't be processed by wn.morphy that lemmatize words automatically, i made a exception list that contain present continuous tense of common words to do it manually '''
exception=['going', 
 'anything',
 'being',
 'nothing',
 'everything',
 'bring',
 'getting',
 'coming',
 'looking',
 'talking',
 'morning',
 'saying',
 'working',
 'making',
 'thinking',
 'taking',
 'meeting',
 'during',
 'telling',
 'running',
 'feeling',
 'building',
 'fucking',
 'living',
 'waiting',
 'using',
 'playing',
 'leaving',
 'asking',
 'giving',
 'seeing',
 'calling',
 'following',
 'happening',
 'watching',
 'wedding',
 'sitting',
 'lying',
 'wearing',
 'standing',
 'training',
 'putting',
 'holding',
 'starting',
 'beginning',
 'reading',
 'walking',
 'killing',
 'driving',
 'planning',
 'fighting',
 'keeping',
 'darling',
 'speaking',
 'writing',
 'helping',
 'eating',
 'finding',
 'dying',
 'hearing',
 'listening',
 'sing',
 'crying',
 'sleeping',
 'drinking',
 'willing',
 'meaning',
 'knowing',
 'growing',
 'acting',
 'bringing',
 'turning',
 'screaming',
 'opening',
 'hanging',
 'spring',
 'painting',
 'flying',
 'selling',
 'showing',
 'leading',
 'letting',
 'hiding',
 'shooting',
 'dealing',
 'breaking',
 'setting',
 'learning',
 'understanding',
 'buying',
 'dating',
 'heading',
 'teaching',
 'spending',
 'singing',
 'warning',
 'sending',
 'dancing',
 'drawing',
 'saving',
 'winning',
 'shopping',
 'picking',
 'cooking',
 'cutting',
 'pulling',
 'offering',
 'boring',
 'burning',
 'passing',
 'housing',
 'parking',
 'breathing',
 'recording',
 'cleaning',
 'panting',
 'bleeding',
 'suffering',
 'cheering',
 'hunting',
 'riding',
 'fishing',
 'pushing',
 'smoking',
 'stealing',
 'testing',
 'closing',
 'knocking',
 'facing',
 'engineering',
 'string',
 'covering',
 'beating',
 'yelling',
 'landing',
 'ending',
 'developing',
 'hitting',
 'rising',
 'stopping',
 'studying',
 'rolling',
 'swimming',
 'causing',
 'serving',
 'sharing',
 'visiting',
 'timing',
 'shouting',
 'whispering',
 'trading',
 'sobbing',
 'digging',
 'smiling',
 'guessing',
 'seeking',
 'wasting',
 'feeding',
 'joining',
 'counting',
 'marketing',
 'raising',
 'racing',
 'dressing',
 'investigating',
 'hurting',
 'handling',
 'growling',
 'cheating',
 'kissing',
 'pretending',
 'bearing',
 'annoying',
 'touching',
 'funding',
 'tracking',
 'blowing',
 'advertising',
 'washing',
 'firing',
 'ringing',
 'reaching',
 'catching',
 'travelling',
 'filling',
 'crossing',
 'thanksgiving',
 'kicking',
 'ceiling',
 'processing',
 'coughing',
 'arguing',
 'worrying',
 'entering',
 'clothing',
 'questioning',
 'jumping',
 'shaking',
 'approaching',
 'reporting',
 'signing',
 'dining',
 'begging',
 'ruling',
 'failing',
 'voting',
 'fitting',
 'starving',
 'accounting',
 'nursing',
 'manufacturing',
 'gathering',
 'blessing',
 'supporting',
 'laying',
 'climbing',
 'outstanding',
 'packing',
 'floating',
 'monitoring',
 'judging',
 'lightning',
 'freezing',
 'caring',
 'finishing',
 'pressing',
 'gambling',
 'performing',
 'dreaming',
 'kidnapping',
 'believing',
 'collecting',
 'traveling',
 'healing',
 'pudding',
 'attending',
 'backing',
 'lighting']
import os
import nltk
nltk.download('wordnet')
import xml.etree.ElementTree as elemTree
from nltk.corpus import wordnet as wn
import re




'''open lemmatized version of cambridge phrase list'''
cambridge_list=open('lemma_MWE_list.txt',encoding='utf-8').readlines()
phrase=[i.strip() for i in cambridge_list]
print('cambridge list total phrase:',len(phrase))

os.chdir('C:/')
''' get the address of every file'''
spoken_data_path=[]
spoken_data=os.listdir('./spoken_bnc')
for i in spoken_data:
    spoken_data_path.append(os.path.join(os.getcwd(),'spoken_bnc',i))
print(len(spoken_data_path))

''' get the text from corpus, since spoken bnc corpus compiled in xml format, i used xml reader code. ('u'==utterance, 'w'==word) '''
sentences = []
for i in spoken_data_path:
    root = elemTree.parse(i).getroot()
    for i in root.findall('u'):
        words = []
        for j in i.findall('w'):
            words.append(j.text.lower().strip())
        sentences.append(words)
    print(len(sentences))

print('total sentences:',len(sentences))
print('total words:',len([j for i in sentences for j in i]))

def clean_text_pre(text):
    ''' change non-standard colloquial expression into formal expression '''
    text=re.sub('du n no',"do n't know",text)
    text=re.sub('gon na', 'going to',text)
    return text

def clean_text_MWE(text):
    '''Clean text by removing unnecessary characters and altering the format of words.'''

    text = re.sub(r"'m", "am", text)
    #text = re.sub(r"'s", "is", text)
    #text = re.sub(r"\'ll", "will", text)
    #text = re.sub(r"\'ve", "have", text)
    text = re.sub(r"\'re", "are", text)
    #text = re.sub(r"n't", "not", text)
    #text = re.sub(r"n'", "ng", text)
    text = re.sub(r"'bout", "about", text)
    text = re.sub(r"'till", "until", text)
    #text = re.sub("wo", "will", text)
    #text = re.sub("ca", "can", text)
    text = re.sub('du n no', "do n't know", text)
    text = re.sub('gon na', 'going to', text)
    text = re.sub('cos', 'because', text)
    text = re.sub(r"[()\#/_@;:<>{}`+=~|]", "", text)

    return text

def clean_text_word(text):
    '''Clean text by altering the format of words.'''

    text = re.sub(r"'s", "be", text)
    text = re.sub(r"\'ll", "will", text)
    text = re.sub(r"\'ve", "have", text)

    return text


formal_sentences=[]
for sentence in sentences:
    formal_sentences.append(clean_text_pre(' '.join(sentence)))

clean_sentences = []
for sentence in formal_sentences:
    clean_sentence = []
    for word in sentence.split():
        clean_sentence.append(clean_text_MWE(word))
    clean_sentences.append(clean_sentence)

print('cleaned the sentence')

''' lemmatize the word'''
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
lemmatize_sentences=[]
for i in clean_sentences:
    lemmatize_sentence=[]
    for j in i:
        lemmatize_sentence.append(wn.morphy(j))
    lemmatize_sentences.append(lemmatize_sentence)

''' wn.morphy return none to certain part of speech such as preposition, therefore replace Nonetype outputs to unlemmatized equivalent'''
for i,y in zip(lemmatize_sentences,clean_sentences):
    for j,x in enumerate(i):
        if x==None:
            i[j]=y[j]

def correction(text):
    '''lemmatize words with present continuous tense form'''
    if text in exception:
        text=re.sub('going','go',text)
        text=re.sub('getting','get',text)
        text=re.sub('coming','come',text)
        text=re.sub('looking','look',text)
        text=re.sub('talking','talk',text)
        text=re.sub('saying','say',text)
        text=re.sub('working','work',text)
        text=re.sub('making','make',text)
        text=re.sub('thinking','think',text)
        text=re.sub('taking','take',text)
        text=re.sub('meeting','meet',text)
        text=re.sub('telling','tell',text)
        text=re.sub('running','run',text)
        text=re.sub('feeling','feel',text)
        text=re.sub('fucking','fuck',text)
        text=re.sub('living','live',text)
        text=re.sub('waiting','wait',text)
        text=re.sub('using','use',text)
        text=re.sub('playing','play',text)
        text=re.sub('leaving','leave',text)
        text=re.sub('asking','ask',text)
        text=re.sub('giving','give',text)
        text=re.sub('seeing','see',text)
        text=re.sub('calling','call',text)
        text=re.sub('following','follow',text)
        text=re.sub('happening','happen',text)
        text=re.sub('watching','watch',text)
        text=re.sub('sitting','sit',text)
        text=re.sub('lying','lie',text)
        text=re.sub('wearing','wear',text)
        text=re.sub('standing','stand',text)
        text=re.sub('training','train',text)
        text=re.sub('putting','put',text)
        text=re.sub('holding','hold',text)
        text=re.sub('starting','start',text)
        text=re.sub('beginning','begin',text)
        text=re.sub('reading','read',text)
        text=re.sub('walking','walk',text)
        text=re.sub('killing','kill',text)
        text=re.sub('driving','drive',text)
        text=re.sub('planning','plan',text)
        text=re.sub('fighting','fight',text)
        text=re.sub('keeping','keep',text)
        text=re.sub('speaking','speak',text)
        text=re.sub('writing','write',text)
        text=re.sub('helping','help',text)
        text=re.sub('eating','eat',text)
        text=re.sub('finding','find',text)
        text=re.sub('dying','die',text)
        text=re.sub('hearing','hear',text)
        text=re.sub('listening','listen',text)
        text=re.sub('crying','cry',text)
        text=re.sub('sleeping','sleep',text)
        text=re.sub('drinking', 'drink', text)
        text=re.sub('meaning', 'mean', text)
        text=re.sub('knowing','know',text)
        text=re.sub('growing','grow',text)
        text=re.sub('acting','act',text)
        text=re.sub('bringing','bring',text)
        text=re.sub('turning','turn',text)
        text=re.sub('screaming','scream',text)
        text=re.sub('opening','open',text)
        text=re.sub('hanging', 'hang',text)
        text=re.sub('painting', 'paint',text)
        text=re.sub('flying', 'fly',text)
        text=re.sub('selling', 'sell',text)
        text=re.sub('showing', 'show',text)
        text=re.sub('leading', 'lead',text)
        text=re.sub('letting', 'let',text)
        text=re.sub('hiding', 'hide',text)
        text=re.sub('shooting', 'shoot',text)
        text=re.sub('dealing', 'deal',text)
        text=re.sub('breaking','break',text)
        text=re.sub('setting', 'set',text)
        text=re.sub('learning', 'learn',text)
        text=re.sub('understanding', 'understand',text)
        text=re.sub('buying','buy',text)
        text=re.sub('dating', 'date',text)
        text=re.sub('heading', 'head',text)
        text=re.sub('teaching', 'teach',text)
        text=re.sub('spending', 'spend',text)
        text=re.sub('singing', 'sing',text)
        text=re.sub('warning', 'warn',text)
        text=re.sub('sending', 'send',text)
        text=re.sub('dancing', 'dance',text)
        text=re.sub('drawing', 'draw',text)
        text=re.sub('saving', 'save',text)
        text=re.sub('winning', 'win',text)
        text=re.sub('shopping', 'shop',text)
        text=re.sub('picking', 'pick',text)
        text=re.sub('cooking', 'cook',text)
        text=re.sub('cutting', 'cut',text)
        text=re.sub('pulling', 'pull',text)
        text=re.sub('offering', 'offer',text)
    #text=re.sub('boring', 'bore', text)
        text=re.sub('burning', 'burn',text)
        text=re.sub('passing', 'pass',text)
        text=re.sub('housing', 'house',text)
        text=re.sub('parking', 'park',text)
        text=re.sub('breathing', 'breathe',text)
        text=re.sub('recording', 'record',text)
        text=re.sub('cleaning', 'clean',text)
        text=re.sub('panting', 'pant',text)
        text=re.sub('bleeding', 'bleed',text)
        text=re.sub('suffering', 'suffer',text)
        text=re.sub('cheering', 'cheer',text)
        text=re.sub('hunting', 'hunt',text)
        text=re.sub('riding', 'ride',text)
    # fishing->fish
        text=re.sub('pushing', 'push',text)
        text=re.sub('smoking', 'smoke',text)
        text=re.sub('stealing', 'steal',text)
        text=re.sub('testing', 'test',text)
        text=re.sub('closing', 'close',text)
        text=re.sub('knocking', 'knock',text)
        text=re.sub('facing', 'face',text)
    #text=re.sub('engineering', 'engineer',text)
        text=re.sub('covering', 'cover',text)
        text=re.sub('beating', 'beat',text)
        text=re.sub('yelling', 'yell',text)
    #text=re.sub('landing', 'land',text)
        text=re.sub('ending', 'end',text)
        text=re.sub('developing', 'develop',text)
        text=re.sub('hitting', 'hit',text)
        text=re.sub('rising', 'rise',text)
        text=re.sub('stopping', 'stop',text)
        text=re.sub('studying', 'study',text)
        text=re.sub('rolling', 'roll',text)
        text=re.sub('swimming', 'swim',text)
        text=re.sub('causing', 'cause',text)
        text=re.sub('serving', 'serve',text)
        text=re.sub('sharing', 'share',text)
        text=re.sub('visiting', 'visit',text)
        text=re.sub('shouting', 'shout',text)
        text=re.sub('whispering', 'whisper',text)
        text=re.sub('trading', 'trade',text)
        text=re.sub('sobbing', 'sob',text)
        text=re.sub('digging', 'dig',text)
        text=re.sub('smiling', 'smile',text)
        text=re.sub('guessing', 'guess',text)
        text=re.sub('seeking', 'seek',text)
    #timing->time
        text=re.sub('wasting', 'waste', text)
        text=re.sub('feeding', 'feed', text)
        text=re.sub('joining', 'join',text)
        text=re.sub('counting', 'count',text)
        text=re.sub('marketing', 'market',text)
        text=re.sub('raising', 'raise',text)
        text=re.sub('racing', 'race',text)
        text=re.sub('dressing', 'dress',text)
        text=re.sub('investigating', 'investigate',text)
        text=re.sub('hurting','hurt',text)
        text=re.sub('handling', 'handle',text)
        text=re.sub('growling', 'growl',text)
        text=re.sub('cheating', 'cheat',text)
        text=re.sub('kissing', 'kiss',text)
        text=re.sub('pretending','pretend',text)
        text=re.sub('bearing', 'bear',text)
        text=re.sub('annoying','annoy',text)
        text=re.sub('touching', 'touch',text)
        text=re.sub('funding', 'fund',text)
        text=re.sub('tracking', 'track',text)
        text=re.sub('blowing', 'blow',text)
        text=re.sub('advertising','advertise',text)
        text=re.sub('washing','wash',text)
        text=re.sub('firing', 'fire',text)
        text=re.sub('ringing', 'ring',text)
        text=re.sub('reaching', 'reach',text)
        text=re.sub('catching', 'catch',text)
        text=re.sub('travelling', 'travel',text)
        text=re.sub('filling', 'fill',text)
        text=re.sub('crossing', 'cross',text)
        text=re.sub('kicking', 'kick',text)
        text=re.sub('processing', 'process',text)
        text=re.sub('coughing', 'cough',text)
        text=re.sub('arguing', 'argue',text)
        text=re.sub('worrying', 'worry',text)
        text=re.sub('entering', 'enter',text)
     #clothing->clothe
        text=re.sub('questioning', 'question',text)
        text=re.sub('jumping', 'jump',text)
        text=re.sub('shaking', 'shake',text)
        text=re.sub('approaching', 'approach',text)
        text=re.sub('reporting', 'report',text)
        text=re.sub('signing','sign',text)
        text=re.sub('dining','dine',text)
        text=re.sub('begging', 'beg',text)
        text=re.sub('ruling', 'rule',text)
        text=re.sub('failing', 'fail',text)
        text=re.sub('voting', 'vote',text)
        text=re.sub('fitting', 'fit',text)
        text=re.sub('starving', 'starve',text)
    #accounting->account
        text=re.sub('nursing','nurse',text)
        text=re.sub('manufacturing', 'manufacture',text)
        text=re.sub('gathering', 'gather',text)
        text=re.sub('blessing', 'bless',text)
        text=re.sub('supporting','support',text)
        text=re.sub('laying', 'lay',text)
        text=re.sub('climbing','climb',text)
        text=re.sub('packing', 'pack',text)
        text=re.sub('floating', 'float',text)
        text=re.sub('monitoring', 'monitor',text)
        text=re.sub('judging', 'judge',text)
        text=re.sub('freezing', 'freeze',text)
        text=re.sub('caring', 'care',text)
        text=re.sub('finishing', 'finish',text)
        text=re.sub('pressing', 'press',text)
        text=re.sub('gambling', 'gamble',text)
        text=re.sub('performing', 'perform',text)
        text=re.sub('dreaming', 'dream',text)
        text=re.sub('kidnapping', 'kidnap',text)
        text=re.sub('believing', 'believe',text)
        text=re.sub('collecting', 'collect',text)
        text=re.sub('traveling', 'travel',text)
        text=re.sub('healing', 'heal',text)
        text=re.sub('attending', 'attend',text)

    return text
def correction2(texted):
    ''' change wrong lemmatized words into correct one'''
    error=["wa","are","ha","am","comic_strip"]
    if texted in error:
        texted = re.sub("am","be",texted)
        texted = re.sub("wa","be",texted)
        texted = re.sub("are","be",texted)
        texted = re.sub("ha","have",texted)
        ''' couldn't figure out the reason but during the lemmatization process comic strip becomes comic_strip so this code correct this error'''
        texted = re.sub("comic_strip", 'comic strip',texted)
    return texted

lemmatized_sentences=[]
for i in lemmatize_sentences:
    lemmatized_sentence=[]
    for j in i:
        lemmatized_sentence.append(correction(j))
    lemmatized_sentences.append(lemmatized_sentence)

print('lemmatization finished')

lemma_sentences=[]
for i in lemmatized_sentences:
    lemma_sentence=[]
    for j in i:
        lemma_sentence.append(correction2(j))
    lemma_sentences.append(lemma_sentence)

print([j for i in lemma_sentences for j in i if j=='comic_strip'])
print(len([j for i in lemma_sentences for j in i if re.search('_',j)!=None]))
print([j for i in lemma_sentences for j in i if re.search('_',j)!=None])

'''find and bound phrases in whole corpus. this code bound longer phrases first because the number of longer phrases can be subsumed to the number of short phrases'''

print('detect MWE')
for i in range(len(lemma_sentences)):
    for j in range(len(lemma_sentences[i])-5):
        if lemma_sentences[i][j]+' '+lemma_sentences[i][j+1]+' '+lemma_sentences[i][j+2]+' '+lemma_sentences[i][j+3]+' '+lemma_sentences[i][j+4]+' '+lemma_sentences[i][j+5] in phrase:
            lemma_sentences[i][j]=lemma_sentences[i][j]+'_'+lemma_sentences[i][j+1]+'_'+lemma_sentences[i][j+2]+'_'+lemma_sentences[i][j+3]+'_'+lemma_sentences[i][j+4]+'_'+lemma_sentences[i][j+5]
            lemma_sentences[i][j+1] = ''
            lemma_sentences[i][j+2] = ''
            lemma_sentences[i][j+3] = ''
            lemma_sentences[i][j+4] = ''
            lemma_sentences[i][j+5] = ''
        if lemma_sentences[i][j]+' '+lemma_sentences[i][j+1]+' '+lemma_sentences[i][j+2]+' '+lemma_sentences[i][j+3]+' '+lemma_sentences[i][j+4] in phrase:
            lemma_sentences[i][j]=lemma_sentences[i][j]+'_'+lemma_sentences[i][j+1]+'_'+lemma_sentences[i][j+2]+'_'+lemma_sentences[i][j+3]+'_'+lemma_sentences[i][j+4]
            lemma_sentences[i][j+1] = ''
            lemma_sentences[i][j+2] = ''
            lemma_sentences[i][j+3] = ''
            lemma_sentences[i][j+4] = ''
        if lemma_sentences[i][j]+' '+lemma_sentences[i][j+1]+' '+lemma_sentences[i][j+2]+' '+lemma_sentences[i][j+3] in phrase:
            lemma_sentences[i][j]=lemma_sentences[i][j]+'_'+lemma_sentences[i][j+1]+'_'+lemma_sentences[i][j+2]+'_'+lemma_sentences[i][j+3]
            lemma_sentences[i][j+1] = ''
            lemma_sentences[i][j+2] = ''
            lemma_sentences[i][j+3] = ''
        if lemma_sentences[i][j]+' '+lemma_sentences[i][j+1]+' '+lemma_sentences[i][j+2] in phrase:
            lemma_sentences[i][j]=lemma_sentences[i][j]+'_'+lemma_sentences[i][j+1]+'_'+lemma_sentences[i][j+2]
            lemma_sentences[i][j+1] = ''
            lemma_sentences[i][j+2] = ''
        if lemma_sentences[i][j]+' '+lemma_sentences[i][j+1] in phrase:
            lemma_sentences[i][j] = lemma_sentences[i][j] + '_' + lemma_sentences[i][j + 1]
            lemma_sentences[i][j+1] = ''

    if len(lemma_sentences[i])>4 and lemma_sentences[i][-5]+' '+lemma_sentences[i][-4]+' '+lemma_sentences[i][-3]+' '+lemma_sentences[i][-2]+' '+lemma_sentences[i][-1] in phrase:
        lemma_sentences[i][-5] = lemma_sentences[i][-5]+'_'+lemma_sentences[i][-4]+'_'+lemma_sentences[i][-3]+'_'+lemma_sentences[i][-2] + '_' + lemma_sentences[i][-1]
        lemma_sentences[i][-4] = ''
        lemma_sentences[i][-3] = ''
        lemma_sentences[i][-2] = ''
        lemma_sentences[i][-1] = ''
    if len(lemma_sentences[i])>3 and lemma_sentences[i][-4]+' '+lemma_sentences[i][-3]+' '+lemma_sentences[i][-2]+' '+lemma_sentences[i][-1] in phrase:
        lemma_sentences[i][-4] = lemma_sentences[i][-4]+'_'+lemma_sentences[i][-3]+'_'+lemma_sentences[i][-2] + '_' + lemma_sentences[i][-1]
        lemma_sentences[i][-3] = ''
        lemma_sentences[i][-2] =''
        lemma_sentences[i][-1] = ''
    if len(lemma_sentences[i])>2 and lemma_sentences[i][-3]+' '+lemma_sentences[i][-2]+' '+lemma_sentences[i][-1] in phrase:
        lemma_sentences[i][-3] = lemma_sentences[i][-3]+'_'+lemma_sentences[i][-2] + '_' + lemma_sentences[i][-1]
        lemma_sentences[i][-2] =''
        lemma_sentences[i][-1] = ''
    if len(lemma_sentences[i])>1 and lemma_sentences[i][-2]+' '+lemma_sentences[i][-1] in phrase:
        lemma_sentences[i][-2] = lemma_sentences[i][-2] + '_' + lemma_sentences[i][-1]
        lemma_sentences[i][-1] = ''
    ''' remove every blanks('') in each sentences'''
    while True:
        if '' in lemma_sentences[i]:
            lemma_sentences[i].remove('')
        else:
            break
    if i%1000==0:
        print('{}/{}'.format(i,1248110))

''' make a sentence as a string'''
correct_lemmas = []
for lemma_sentence in lemma_sentences:
    correct_lemmas.append(' '.join(lemma_sentence))
correct_cleaned = []
for clean_sentence in clean_sentences:
    correct_cleaned.append(' '.join(clean_sentence))

''' find the location of phrases in lemmatized sentences and bound the words in equivalent position in original corpus'''
result=[]
for index1, sentence in enumerate(correct_lemmas):
    words = [i for i in sentence.split(' ')]
    new_sentence = correct_cleaned[index1].split(' ')
    for index2, i in enumerate(words):
        if '_' in i:
            new_sentence[index2]='_'.join(new_sentence[index2:index2+len(i.split('_'))])
            del new_sentence[index2+1:index2+len(i.split('_'))]

    result.append(' '.join(new_sentence))



os.chdir('C:/Users/gartl/Documents')
output_file = open("chatbot_training_data.txt", 'w',encoding='utf-8')
for sentences in result:
    output_file.write(sentences+'\n')
output_file.close()

spokenBNC_MWElist=[i for j in result for i in j.split() if re.search(r'_',i)!=None]
print('phrases_data:',len(spokenBNC_MWElist))
phrases_file=open("spokenBNC_MWElist.txt", 'w',encoding='utf-8')
for phrases in spokenBNC_MWElist:
    phrases_file.write(phrases+'\n')
phrases_file.close()

spokenBNC_lemma_MWElist=[i for j in lemma_sentences for i in j if re.search(r'_',i)!=None]
print('phrase_data:',len(spokenBNC_lemma_MWElist))
phrase_file=open("spokenBNC_lemma_MWElist.txt", 'w',encoding='utf-8')
for phrases in spokenBNC_lemma_MWElist:
    phrase_file.write(phrases+'\n')
phrase_file.close()

'''eliminate words that are not recognized as real word for accuracy of counting words'''
error_spoken=['--unclearword','--anonnamem','--anonnamef','--anonplace','unclearword','anonnamem','anonnamef','anonplace','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
spoken_bnc_word=[j for i in lemma_sentences for j in i if j not in error_spoken]
spoken_bnc_word=[i for i in spoken_bnc_word if i!='']
spoken_bnc_word=[i for i in spoken_bnc_word if i not in spokenBNC_lemma_MWElist]
spoken_bnc_word=[clean_text_word(i) for i in spoken_bnc_word]

print('spoken_bnc_n:',[i for i in spoken_bnc_word if i=='n'])
print('spoken_bnc_s:',[i for i in spoken_bnc_word if i=='s'])
print('bnc length:', len(spoken_bnc_word))

print(spoken_bnc_word[:20])

word_list_file=open('./BNC_spoken_count.txt','w',encoding='utf-8')
for i in spoken_bnc_word:
    word_list_file.write(i+'\n')
word_list_file.close()










