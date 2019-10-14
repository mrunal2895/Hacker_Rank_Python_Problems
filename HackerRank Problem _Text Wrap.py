#!/usr/bin/env python
# coding: utf-8

# In[16]:


#PROBLEM STATEMENT!!!
'''
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Output Format

Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''


# In[ ]:


import textwrap


# In[17]:


#Solution fro Hacker Rank Problem

def wrap(string, max_width):
    return textwrap.fill(string,max_width)
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[13]:


#Practice code
s="I am mrunal limaye and study at georgia state universitydda"
textwrap.fill(s,4)
print(textwrap.fill(s,4))


# In[15]:


#Practice code
print(len(s))
for i in range(0,len(s)):
    if (i!=0 and i%4==0):
        print(s[i]+'\n')
    else:
        print(s[i],end='')


# In[ ]:





# In[ ]:




