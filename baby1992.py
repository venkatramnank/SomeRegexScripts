"""
Created on Mon Jun 10 21:23:30 2019

@author: venkat
"""
import re

file=open('/home/venkat/Desktop/serious_python/day1/baby1992.html','r')
str=file.read()
#print(str)
boysnames=[]
girlsname=[]
#print("The list of boys names:")
groups=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',str)

#print('The list of boys:')
for i in groups:
    boysnames.append(i[1])
for i in groups:
    girlsname.append(i[2])

file2=open('/home/venkat/Desktop/serious_python/day1/names1992.txt','a+')
file2.write("The list of boys names:\n")
for j in boysnames:
    i=(boysnames.index(j))+1
    file2.write("%d) " % i)
    file2.write("%s\n" % j)
file2.write("\nThe list of girls names:\n")
for j in girlsname:
    i=(girlsname.index(j))+1
    file2.write("%d) " % i)
    file2.write("%s\n" % j)
