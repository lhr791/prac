#!/usr/bin/env python
# coding: utf-8

# # 取出字符串中数字、字母、大小写英文
# ## Take out the numbers, letters, uppercase and lowercase English in the string

# 
# * 方法1 for循环
# * .isdigit()=是否由数字构成
# * .islower()=是否由小写。。
# * .isupper()=。。。。

# In[ ]:


number=''


# In[ ]:


lower=''


# In[ ]:


upper=''


# In[ ]:


a='asd213SDAF123SADsdf'


# In[ ]:


for i in a :
    if i.isdigit():
        number=number+i
    elif i.islower():
        lower=lower+i
    elif i.isupper():
        upper=upper+i


# In[ ]:


print(number+'\n'+lower+'\n'+upper)


# * 方法2 正则表达式
# * \d=匹配任意数字，等价于[0-9]
# * \D=匹配任意非数字
# * [0-9]匹配任意数字
# * [a-z]匹配任意小写字母
# * [A-Z]。。。。。
# * [a-zA-Z0-9]匹配任意数字字母

# In[ ]:


import re


# In[ ]:


re.findall('[A-Za-z]', a)


# In[ ]:


print(''.join(re.findall('[A-Za-z]', a)))
print(''.join(re.findall('[A-Z]', a)))
print(''.join(re.findall('[a-z]', a)))
print(''.join(re.findall('[0-9]', a)))
print(''.join(re.findall('[2-9]', a)))


# * 对str格式 a里面的内容进行输出项替换（不替换原a）

# In[ ]:


print(re.sub('1', 'T', a))
print(re.sub('\D', '',a))

