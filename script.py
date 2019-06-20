# -*- coding: cp1251 -*-
from collections import Counter
import re
from math import log

alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя "

def clear_text():
    file = open('text.txt')
    string = file.read()
    string = string.lower()
    string = string.replace('ё','е')
    string = string.replace('ъ','ь')
    for i in string:
        if not(i in alphabet):
            string = string.replace(i, ' ')
    while "  " in string:
        string = string.replace('  ',' ')
    clear_file = open('clear_text.txt', 'w')
    clear_file.write(string)
    clear_file.close()
    string = string.replace(' ', '')
    clear_file = open('clear_text_nospaces.txt', 'w')
    clear_file.write(string)
    clear_file.close()
    file.close()
    print('Text cleaned and saved successfully.')

#clear_text()
hmas=[]
def entropy(bigrams):
    c = Counter()
    for word in bigrams:
        c[word] += 1
    H=0
    sum1=sum(c.values())
    print 'Всього біграм', sum1
    print alphabet
    for i in alphabet:
        mas = []
        for j in alphabet:
            if i+j in c.keys():
                mas.append(c[i+j] / float(sum1))
                H -= (c[i+j] / float(sum1)) * log(c[i+j] / float(sum1), 2)
            else:
                mas.append(0)
        print i, mas
    hmas.append(H/2)

def entropyword(string):
    H=0
    print 'Всього символів', len(string)
    print 'Частоти символів:'
    c = Counter(string).most_common()
    for i in range(len(c)):
        print c[i][0], ":", c[i][1]/float(len(string))
        H -= (c[i][1]/float(len(string))) * log(c[i][1]/float(len(string)), 2)
    hmas.append(H)   
        
def count(filename):
    file = open(filename)
    string = file.read()
    entropyword(string)
    print 'Частоти біграм, які перетинаються:'
    bigrams = []
    for j in range(len(string)-1):
        bigrams.append(string[j]+string[j+1])
    #entropy(re.findall(r'..', string))
    entropy(bigrams)
    print 'Частоти біграм, які не перетинаються:'
    bigrams = []
    for j in range(0, len(string)-1, 2):
        bigrams.append(string[j]+string[j+1])
    #bigrams = re.findall(r'([а-я+\s]{2})', string)
    entropy(bigrams)
    file.close()

print "ТЕКСТ З ПРОБІЛАМИ"
count('clear_text.txt')
print "ТЕКСТ БЕЗ ПРОБІЛІВ"
count('clear_text_nospaces.txt')
print 'H letter with spaces:', hmas[0]
print 'R letter with spaces:', 1-hmas[0]/log(len(alphabet), 2)
print 'H cross bigrams with spaces:', hmas[1]
print 'R cross bigrams with spaces:', 1-hmas[1]/log(len(alphabet), 2)
print 'H non-cross  bigrams with spaces:', hmas[2]
print 'R non-cross  bigrams with spaces:', 1-hmas[2]/log(len(alphabet), 2)
print 'H letter', hmas[3]
print 'R letter', 1-hmas[3]/log(len(alphabet), 2)
print 'H cross bigrams:', hmas[4]
print 'R cross bigrams:', 1-hmas[4]/log(len(alphabet), 2)
print 'H non-cross  bigrams', hmas[5]
print 'R non-cross  bigrams', 1-hmas[5]/log(len(alphabet), 2)
