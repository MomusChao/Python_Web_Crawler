
# coding: utf-8

# In[1]:

#import module
import requests


# In[2]:

#define function
def get_content(url):
    resp = requests.get(url) # get & post
    return resp.text


# In[3]:

if __name__ == '__main__':
    url="http://www.phei.com.cn/"
    content=get_content(url)
    print("Top 50 Char:",content[0:50])
    
    # content len
    content_len = len(content)
    print("len content:",content_len)

    # len content is bigger than 40KB?
    if content_len >=40*1024:
        print("Yes, it is")
    else:
        print("No, it is not")


# In[ ]:

# save as MoCrawler2.py

