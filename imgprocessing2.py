
# coding: utf-8

# In[1]:

import cv2
import matplotlib.pyplot as plt


# In[2]:

img = cv2.imread("insta.jpg")


# In[3]:

img.shape


# In[4]:

img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()


# In[5]:

img


# In[6]:

test=img.copy()
import numpy as np
lower_green=np.array([10,30,10])
upper_green=np.array([200,250,200])
mask=cv2.inRange(test,lower_green,upper_green,cv2.THRESH_BINARY)
plt.imshow(mask,cmap="gray")
plt.show()


# In[7]:

_,thesh=cv2.threshold(mask,50,255,cv2.THRESH_BINARY)
plt.imshow(thesh,cmap="gray")
plt.show()


# In[8]:

img[mask==0]=0


# In[9]:

plt.imshow(img)
plt.show()


# In[11]:

bg=cv2.imread("space.jpg")
bg=cv2.cvtColor(bg,cv2.COLOR_BGR2RGB)
bg=cv2.resize(bg,(300,168))


# In[12]:

plt.imshow(bg)
plt.show()


# In[14]:

bg[mask!=0]=0
plt.imshow(bg)
plt.show()


# In[15]:

plt.imshow(bg+img)
plt.show()


# In[ ]:



