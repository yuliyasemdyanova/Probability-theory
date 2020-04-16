#!/usr/bin/env python
# coding: utf-8

# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

# In[7]:


s=np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])


# среднее арифметическое

# In[9]:


s_mean=s.sum()/s.size
s_mean


# среднее квадратичное отклонение

# In[11]:


s_std=np.sum(((s-s_mean)**2)/s.size)**0.5
s_std


# смещенная дисперсия

# In[14]:


s_var=np.sum(((s-s_mean)**2)/s.size)
s_var


# несмещенная дисперсия

# In[15]:


s_var2=np.sum(((s-s_mean)**2)/(s.size-1))
s_var2


# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?

# In[1]:


import numpy as np
import numpy as np
import math
from math import factorial
def combinations(k,n):
    return(factorial(n)/(factorial(k)*factorial(n-k)))
def bernulli(k,n,p):
    return(combinations(k,n)*p**k*(1-p)**(n-k))
def puasson (n,m,p):
    lambda_=n*p
    return(lambda_**m/factorial(m))*np.exp(-lambda_)


# In[2]:


p1=combinations(2,5)/combinations(2,8)*combinations(1,5)*combinations(3,7)/combinations(4,12)
p1


# In[4]:


p2=combinations(1,5)*combinations(1,3)/combinations(2,8)*combinations(2,5)*combinations(2,7)/combinations(4,12)
p2


# In[6]:


p3=combinations(2,3)/combinations(2,8)*combinations(3,5)*combinations(1,7)/combinations(4,12)
p3


# In[7]:


p=p1+p2+p3
p


# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.

# In[21]:


p=1/3*0.9+1/3*0.8+1/3*0.6
p


# In[17]:


p1=1/3*0.9/p
p1


# In[18]:


p2=1/3*0.8/p
p2


# In[19]:


p3=1/3*0.6/p
p3


# В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же, сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?

# In[32]:


p=1/4*0.8+1/4*0.7+2/4*0.9
p


# In[36]:


A=(1/4*0.8)/p
A


# In[37]:


B=1/4*0.7/p
B


# In[38]:


C=2/4*0.9/p
C


# Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя:   

# In[39]:


p=1/3*0.1+1/3*0.2+1/3*0.25
p


# а). все детали

# In[41]:


bernulli(3,3,p)


# б). только две детали

# In[42]:


bernulli(2,3,p)


# в). хотя бы одна деталь

# In[46]:


1-bernulli(0,3,p)


#  г). от одной до двух деталей?

# In[47]:


1-bernulli(1,3,p)


# In[ ]:





# In[ ]:



