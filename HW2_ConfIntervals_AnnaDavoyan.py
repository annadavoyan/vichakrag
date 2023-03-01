#!/usr/bin/env python
# coding: utf-8

# 1. Пусть $X∼F(x)$ — случайная величина с произвольным распределением, неизвестным математическим ожиданием EX и известной дисперсией DX. Как выглядит доверительный интервал для EX с приближённым уровнем доверия 100(1−α)%?
# 
# A.         $\bar{X}_{n}\pm z_{1-\frac{\alpha}{2}}\frac{DX}{\sqrt{n}}$ </br>
# </br>
# B.         $\bar{X}_{n}\pm t_{n-1, 1-\frac{\alpha}{2}}\sqrt{\frac{DX}{n}}$ </br>
# </br>
# C.         $\bar{X}_{n}\pm z_{1-\frac{\alpha}{2}}{\sqrt\frac{DX}{n}}$ </br>
# </br>
# D.         $\bar{X}_{n}\pm z_{1-\alpha}\sqrt{\frac{DX}{n}}$ </br>

# In[32]:


# 1. Your answer here
print("A")


# 2. Для 61 большого города в Англии и Уэльсе известны средняя годовая смертность на 100000 населения (по данным 1958–1964) и концентрация кальция в питьевой воде (в частях на миллион). Чем выше концентрация кальция, тем жёстче вода. Города дополнительно поделены на северные и южные.

# In[3]:


import pandas as pd
import numpy as np


# In[6]:


# Load water.txt file
water_data = pd.read_table("C:\\Users\\davoy\\water.txt")


# In[7]:


water_data.info()


# In[9]:


water_data.head()


# In[8]:


water_data.describe()


# Постройте 95% доверительный интервал для средней годовой смертности в больших городах. Чему равна его нижняя граница? Округлите ответ до 4 знаков после десятичной точки. </br>
#  </br>
#   </br>
#    </br>
# **Будьте осторожны при использовании метода std()!** Дело в том, что у объекта numpy он по умолчанию вычисляется как
# $\sqrt{\frac{1}{n}\sum_{i=1}^n(X_i-\bar{X})}$, а у объекта pandas — как $\sqrt{\frac{1}{n-1}\sum_{i=1}^n(X_i-\bar{X})}$. </br>
#  </br>
# Интересует только второй вариант, несмещённая оценка стандартного отклонения. </br>
#  </br>
# Чтобы не думать всё время о том, правильно ли вычисляется в вашем случае std(), можно всегда использовать std(ddof=1) (ddof — difference in degrees of freedom), тогда нормировка всегда будет на n-1.

# In[11]:


# 2. Your answer here
mort_mean = water_data['mortality'].mean()
mort_mean


# In[20]:


from statsmodels.stats.weightstats import _tconfint_generic


# In[21]:


mort_mean_std = water_data['mortality'].std() / np.sqrt(water_data['mortality'].shape[0])
print('Mortality 95%% interval: %s' %  str(_tconfint_generic(mort_mean, mort_mean_std, water_data['mortality'].shape[0] - 1,
                                                         0.05, 'two-sided')))


# 3. На данных из предыдущего вопроса постройте 95% доверительный интервал для средней годовой смертности по всем южным городам. Чему равна его верхняя граница? Округлите ответ до 4 знаков после десятичной точки.

# In[22]:


# 3. Your answer here
water_data_south = water_data[water_data.location == 'South']
mort_mean_south = water_data_south['mortality'].mean()
print('Mean south mortality: %f' % mort_mean_south)


# In[23]:


mort_mean_south_std = water_data_south['mortality'].std() / np.sqrt(water_data_south['mortality'].shape[0])
print('Mortality south 95%% interval: %s' %  str(_tconfint_generic(mort_mean_south, mort_mean_south_std,
                                                                   water_data_south['mortality'].shape[0] - 1,
                                                                   0.05, 'two-sided')))


# 4. На тех же данных постройте 95% доверительный интервал для средней годовой смертности по всем северным городам. Пересекается ли этот интервал с предыдущим? Как вы думаете, какой из этого можно сделать вывод? 

# In[24]:


# 4. Your answer here
water_data_north = water_data[water_data.location == 'North']
mort_mean_north = water_data_north['mortality'].mean()
print('Mean north mortality: %f' % mort_mean_north)


# In[25]:


mort_mean_north_std = water_data_north['mortality'].std() / np.sqrt(water_data_north['mortality'].shape[0])
print('Mortality north 95%% interval: %s' %  str(_tconfint_generic(mort_mean_north, mort_mean_north_std,
                                                                   water_data_north['mortality'].shape[0] - 1,
                                                                   0.05, 'two-sided')))


# 5. Пересекаются ли 95% доверительные интервалы для средней жёсткости воды в северных и южных городах?
# 
# A. Пересекаются </br>
# B. Не пересекаются 

# In[26]:


# 5. Your answer here
hardness_mean_south = water_data_south['hardness'].mean()
print('Mean south hardness: %f' % hardness_mean_south)

hardness_mean_north = water_data_north['hardness'].mean()
print('Mean north hardness: %f' % hardness_mean_north)


# In[27]:


hardness_mean_south_std = water_data_south['hardness'].std() / np.sqrt(water_data_south['hardness'].shape[0])
print('Hardness south 95%% interval: %s' %  str(_tconfint_generic(hardness_mean_south, hardness_mean_south_std,
                                                                   water_data_south['hardness'].shape[0] - 1,
                                                                   0.05, 'two-sided')))

hardness_mean_north_std = water_data_north['hardness'].std() / np.sqrt(water_data_north['hardness'].shape[0])
print('Hardness north 95%% interval: %s' %  str(_tconfint_generic(hardness_mean_north, hardness_mean_north_std,
                                                                   water_data_north['hardness'].shape[0] - 1,
                                                                   0.05, 'two-sided')))


# 6. Вспомним формулу доверительного интервала для среднего нормально распределённой случайной величины с дисперсией $\sigma^2$: </br>
# $\bar{X}_{n}\pm z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}$ </br>
# При $\sigma = 1$ какой нужен объём выборки, чтобы на уровне доверия 95% оценить среднее с точностью $\pm0.1$?

# In[28]:


# 6. Your answer here
from scipy import stats
np.ceil((stats.norm.ppf(1-0.05/2) / 0.1)**2)


# 7. Объём выборки, необходимый для построения доверительного интервала заданной ширины: </br>
# A. увеличивается с уменьшением требуемой ширины, </br>
# B. уменьшается с ростом дисперсии выборки, </br>
# C. увеличивается с увеличением требуемой ширины, </br>
# D. увеличивается с ростом дисперсии выборки, </br>
# E. увеличивается с ростом $\alpha$, </br>
# F. уменьшается с ростом $\alpha$. </br>

# In[33]:


# 7. Your answer here
print("B,C,F")


# 8. Давайте уточним правило трёх сигм. Утверждение: 99.7% вероятностной массы случайной величины $X∼N(\mu,\sigma^2)$ лежит в интервале $\mu±c⋅\sigma$. Чему равно точное значение константы c? Округлите ответ до четырёх знаков после десятичной точки.

# In[29]:


# 8. Your answer here
from scipy import stats
print('Answer: %.4f' % stats.norm.ppf(1-0.003/2))


# 9. Пусть $X∼N(\mu,\sigma^2)$. Какое распределение имеет величина $\frac{\bar{X}_n - \mu}{S_n/\sqrt{n}}$? </br>
# A. $St(n-1)$ </br>
# </br>
# B. $N(0, 1)$ </br>
# </br>
# C. $\chi_{n-1}^2$ </br>

# In[31]:


# 9. Your answer here
print("B")


# 10. Выберите все распределения с несимметричной функцией плотности: </br>
# 
# A. Фишера, </br>
# B. Стьюдента, </br>
# C. хи-квадрат, </br>
# D. Гаусса

# In[30]:


# 10. Your answer here
print("B and D")

