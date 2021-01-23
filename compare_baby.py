#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:26:30 2019

@author: venkat
"""
from collections import Counter
import re
file=open('/home/venkat/Desktop/serious_python/day1/baby2000.html','r')
str=file.read()

#print("The list of boys names:")
groups=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',str)
strb1=''
strg1=''
#print('The list of boys:')
for i in groups:
    strb1=strb1+' '+(i[1])
for i in groups:
    strg1=strg1+' '+(i[2])
##############################################################  

file2=open('/home/venkat/Desktop/serious_python/day1/baby1996.html','r')
str=file2.read()

groups=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',str)
strb2=''
strg2=''
#print('The list of boys:')
for i in groups:
    strb2=strb2+' '+(i[1])
for i in groups:
    strg2=strg2+' '+(i[2])
########################################################################
file3=open('/home/venkat/Desktop/serious_python/day1/baby1990.html','r')
str=file3.read()

groups=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',str)
strb3=''
strg3=''
#print('The list of boys:')
for i in groups:
    strb3=strb3+' '+(i[1])
for i in groups:
    strg3=strg3+' '+(i[2])
###############################################################

file4=open('/home/venkat/Desktop/serious_python/day1/baby1992.html','r')
str=file4.read()

groups=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',str)
strb4=''
strg4=''
#print('The list of boys:')
for i in groups:
    strb4=strb4+' '+(i[1])
for i in groups:
    strg4=strg4+' '+(i[2])
###############################################################

file5=open('/home/venkat/Desktop/serious_python/day1/baby1994.html','r')
str=file5.read()

groups=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',str)
strb5=''
strg5=''
#print('The list of boys:')
for i in groups:
    strb5=strb5+' '+(i[1])
for i in groups:
    strg5=strg5+' '+(i[2])
###############################################################

file6=open('/home/venkat/Desktop/serious_python/day1/baby1998.html','r')
str=file6.read()
groups=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',str)
strb6=''
strg6=''
#print('The list of boys:')
for i in groups:
    strb6=strb6+' '+(i[1])
for i in groups:
    strg6=strg6+' '+(i[2])
###############################################################

file7=open('/home/venkat/Desktop/serious_python/day1/baby2002.html','r')
str=file7.read()
groups=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',str)
strb7=''
strg7=''
#print('The list of boys:')
for i in groups:
    strb7=strb7+' '+(i[1])
for i in groups:
    strg7=strg7+' '+(i[2])
###############################################################

file8=open('/home/venkat/Desktop/serious_python/day1/baby2004.html','r')
str=file8.read()
groups=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',str)
strb8=''
strg8=''
#print('The list of boys:')
for i in groups:
    strb8=strb8+' '+(i[1])
for i in groups:
    strg8=strg8+' '+(i[2])
###############################################################

file9=open('/home/venkat/Desktop/serious_python/day1/baby2006.html','r')
str=file9.read()
groups=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',str)
strb9=''
strg9=''
#print('The list of boys:')
for i in groups:
    strb9=strb9+' '+(i[1])
for i in groups:
    strg9=strg9+' '+(i[2])
###############################################################

file10=open('/home/venkat/Desktop/serious_python/day1/baby2008.html','r')
str=file10.read()
groups=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',str)
strb10=''
strg10=''
#print('The list of boys:')
for i in groups:
    strb10=strb10+' '+(i[1])
for i in groups:
    strg10=strg10+' '+(i[2])
###############################################################
strb=strb1+' '+strb2+' '+strb3+' '+strb4+' '+strb5+' '+strb6+' '+strb7+' '+strb8+' '+strb9+' '+strb10
strg=strg1+' '+strg2+' '+strg3+' '+strg4+' '+strg5+' '+strg6+' '+strg7+' '+strg8+' '+strg9+' '+strg10
split_boys=strb.split()
split_girls=strg.split()
def most_frequent(List): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0][0] 
print("The most common name among boy's is",(most_frequent(split_boys)))
print("The least common occuring boy's name is",(Counter(split_boys).most_common()[-1])[0])
print("The most common name among girl's is",(most_frequent(split_girls)))
print("The least common occuring girl's name is",(Counter(split_girls).most_common()[:-2:-1])[0])

