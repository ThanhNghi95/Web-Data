import re

# re.search(): return true or false depending on whether the string matches then RegEx
# re.findall(): extract the matching strings

# x= 'My 2 fAvourite numbers are 19 and 42'
# y= re.findall('[0-9]+',x)
# print(y)
# z= re.findall('[AEIOU]+',x)
# print(z)

# x= 'From: using the: character'
# y=re.findall('^F.+:',x)
# print(y)

# x= 'From: using the: character'
# y=re.findall('^F.+?:',x)
# print(y)

# x= 'From nghilt@st.uel.edu.vn sat asd 31:2:3123'
# y=re.findall('\S+@\S+',x)
# print(y)
# z=re.findall('^From (\S+@\S+)',x)
# print(z)

# x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y=re.findall('[0-9]+',x)
# print(y)

# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
# print(y)


file=open("D:/BaiTap/Python/Scraping Web Data/RegEx/regex_sum_1411158.txt")
k=0
for line in file:
    stuff=re.findall('[0-9]+',line)
    if len(stuff)!=0:
        for i in stuff:
            k+=int(i)
print(k)

    
    
