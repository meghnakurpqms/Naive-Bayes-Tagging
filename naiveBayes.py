# coding=utf-8
from collections import Counter
import sys

currentTags = []
correctTags = []
Tags = set()
bitags = []
bitagscount = {}
countWordTag = {}
PrevCurrTagCount = {}
CountTags = {}

corpusfile = sys.argv[1]

cfile = open(corpusfile, 'r')
data = cfile.read()
word_tags = data.split()
prev_Tag = None
wrongTags = 0

for word_tag in word_tags:
    word = word_tag.split("_")[0]
    tag = word_tag.split("_")[1]
    if len(Tags) < 50:
        Tags.add(tag)
    if word in countWordTag:
        countWordTag[word][tag] = countWordTag[word].get(tag, 0) + 1
    else:
        countWordTag[word] = {}
        countWordTag[word][tag] = 1
    if prev_Tag != None:
        PrevCurrTagCount[(prev_Tag, tag)] = PrevCurrTagCount.get((prev_Tag, tag), 0) + 1
    prev_Tag = tag
    CountTags[tag] = CountTags.get(tag, 0) + 1



prob = {}

Tags = list(Tags)
tags = {}

for i in Tags:
	if i not in tags.keys():
		tags[i] = 1
	else:
		tags[i] += 1

for k,v in countWordTag.items():
	for i,j in v.items():
	    tag = i
	    c = j
	    count = tags[tag]
	    weight = float(count)/float(c)

	    prob[i] = weight


f1 = open("Prob_Word_Tag.txt", 'w+')
for k,v in prob.items():
    f1.write("P("+ k+ ") = " +str(v)+"\n")
f1.close()



fileInput= sys.argv[1]

with open(fileInput,'r') as file:
    data = file.read().split()
file.close()

words = {}
for word in data:
    if word not in words.keys():
        words[word] = 1
    else:
        words[word]+=1

for i in range(0,len(data)-2):
    w1 = data[i].split('_')
    w2 = data[i+1].split('_')
    tag = (w1[1], w2[1])
    bitags.append(tag)

for j in bitags:
    if j not in bitagscount.keys():
        bitagscount[j] = 1
    else:
        bitagscount[j]+=1

tokentags = {}
tags = {}

for token in data:
    s = token.split('_')
    a = (s[0], s[1])
    if a not in tokentags.keys():
        tokentags[a] = 1
    else:
        tokentags[a]+=1

    if s[1] not in tags.keys():
        tags[s[1]] = 1
    else:
        tags[s[1]]+=1




tagsprob = {}

for t in bitagscount.items():
    t1 = t[0][0]
    t2 = t[0][1]
    c = t[1]
    tc = tags[t1]
    p = float(c)/float(tc)
    tagsprob[t[0]] = p

f2 = open("Prob_Next_Prev.txt", 'w+')
for k,v in tagsprob.items():
    f2.write("P(" +str(k[0])+" | " +str(k[1])+ ") = "+str(v)+"\n")
f2.close()


    


        














