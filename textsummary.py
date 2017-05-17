#!/usr/bin/env python
import re
import sys
with open(sys.argv[1], "r") as infile:
	lines = infile.readlines()

#print(lines)
infile.close()
with open("bad_words.txt", "r") as infile:
	lines2 = infile.readlines()
stops = [word.strip() + ' ' for word in lines]
bads = [word.strip() for word in lines2]
stops = ''.join(stops)
sentences = re.split('(?<=[.!?]) +',stops)
count = len(sentences)
score = {}
for s in sentences:
	words = s.split(" ")
	j = len(words)*0.4
	for w in words:
		w = str.lower(w)
		if (w.isupper() and len(w) > 1):
			j+=2.5  
		elif (w in bads[0:40] or w in bads[55:79]):
			j-=2.5
		elif (w in bads[41:54] or w in bads[80:107]):
			j-=1
		elif (w in bads[106:173]):
			j-=0.5
		elif (len(w) > 7):
			j+=0.5
	score[j] = s
m = list(score.keys())
for i in m:
	i = float(i)
m = sorted(m, key = float)
m.reverse()
#print(m)
count = count * 0.25
count = int(count)
if(count < 1):
	count = 1
for i in range(count):
	print(score[m[i]])	
#print(score[max(score.keys())])
