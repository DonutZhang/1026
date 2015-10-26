
# coding: utf-8

# In[11]:

news = "今年有十八位國考錄取者,未能通過實務訓練,撤銷錄取資格"
print(news)


# In[12]:

news.split(',')


# In[14]:

news_type = news.split(',')
type(news_type)


# In[22]:

news2 = "今年有十八位國考錄取者","未能通過實務訓練","撤銷錄取資格"
print(news2)


# In[23]:

','.join(news2)


# In[26]:

news.startswith('今年')


# In[27]:

news.startswith('明年')


# In[28]:

news.endswith('資格')


# In[29]:

word = "錄取"
news.find(word)


# In[30]:

news.rfind(word)


# In[31]:

news.count(word)


# In[36]:

import requests
response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/sdxl/001.htm")
response.encoding = "big5"
book1 = response.text


# In[38]:

word2 = "怪客"
book1.count(word2)


# In[50]:

text = 'aN apple A day ....'
print(text)


# In[51]:

text.strip('.')


# In[52]:

text.capitalize()


# In[53]:

text.title()


# In[54]:

text.upper()


# In[55]:

text.lower()


# In[56]:

text.swapcase()


# In[59]:

text.center(30)


# In[61]:

text.ljust(30)


# In[62]:

text.rjust(30)


# In[ ]:



