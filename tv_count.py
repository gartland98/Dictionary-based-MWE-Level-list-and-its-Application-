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
import xml.etree.ElementTree as elemTree
from nltk.corpus import wordnet as wn
import re

os.chdir('C:/')

tv_data_path=[]
tv_data=os.listdir('./TV_corpus')
for i in tv_data:
    tv_data_path.append(os.path.join(os.getcwd(),'TV_corpus',i))
print(tv_data)

tv_raw_word=[]
for i in tv_data_path[:1]:
    print(i)
    tv_raw_word.append(open(i,encoding='utf-8').read().lower())

def clean_text1(text):
    text=re.sub('du n no',"do n't know",text)
    text=re.sub('gon na', 'going to',text)
    return text

tv_raw_words=[clean_text1(i) for i in tv_raw_word]
tv_words=[re.findall('[a-z]+',j) for i in tv_raw_words for j in i.split()]

#tv_words=[]
#for i in tv_raw_word:
    #for j in i:
        #tv_words.append(re.findall('[a-z]+',j))

print(tv_words[:50])

def clean_text(text):
    '''Clean text by removing unnecessary characters and altering the format of words.'''

    text = re.sub(r"'m", "am", text)
    #text = re.sub(r"'s", "is", text)
    text = re.sub(r"\'ll", "will", text)
    text = re.sub(r"\'ve", "have", text)
    text = re.sub(r"\'re", "are", text)
    text = re.sub(r"n't", "not", text)
    text = re.sub(r"'bout", "about", text)
    text = re.sub(r"'till", "until", text)
    text = re.sub('du n no', "do not know", text)
    text = re.sub('gon na', 'going to', text)
    text = re.sub('wo', 'will', text)
    text = re.sub('ca', 'can', text)
    text = re.sub('cos', 'because', text)
    text = re.sub(r"[()\#/@;:<>{}`+=~|]", "", text)
    return text

print([re.findall("du n no",i) for i in tv_raw_words])
print([re.findall("gon na",i) for i in tv_raw_words])
print([re.findall("going to",i) for i in tv_raw_words])

telly_word=[]
for i in tv_words:
    if len(i)==1:
        for j in i:
            telly_word.append(j)

telly=[clean_text(i) for i in telly_word]

print(telly[:100])

print('sentence cleaned')

''' lemmatize the word'''
nltk.download('wordnet')
lemmatize_tv=[wn.morphy(i) for i in telly]

for i,x in enumerate(lemmatize_tv):
    if x==None:
        lemmatize_tv[i]=telly[i]

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
    error=["wa","are","ha","am"]
    if texted in error:
        texted = re.sub("wa","be",texted)
        texted = re.sub("are","be",texted)
        texted = re.sub("ha","have",texted)
        texted = re.sub("am","be",texted)

    return texted

lemma_telly=[correction(i) for i in lemmatize_tv]
lemmatized_telly=[correction(i) for i in lemma_telly]

print('lemmatised complete')

os.chdir('C:/Users/gartl/Downloads')
phrase_list_file=open('./newTVcount2.txt','w',encoding='utf-8')
for i in lemmatized_telly:
    phrase_list_file.write(i+'\n')
phrase_list_file.close()
