#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 21:38:50 2019

@author: venkat
"""
import requests
import re
str=requests.get('https://www.gutenberg.org/files/2638/2638-0.txt').text



#to remove between the given two parts
m=re.search('\*\*\* START OF THIS PROJECT GUTENBERG EBOOK THE IDIOT \*\*\*(.*)II\.',str,flags=re.S).group(0)
x=re.sub(m[0],'',str,flags=re.S)

#to remove end part only
n=re.search('\*\*\* END OF THIS PROJECT GUTENBERG EBOOK TITLE: THE IDIOT \*\*\*(.*)',str,flags=re.S).group(1)
x=re.sub(n[0],'',str,flags=re.S)

#to find word count
count=0
s=re.findall("this",str)#change to any word
for i in s:
    count=count+1
print('The count of the word is ',count)

#to print all section headings
u=[]
for i in (str.split('\n')):
    for j in i:
        if(j.isupper()==True):
            u.append(i)