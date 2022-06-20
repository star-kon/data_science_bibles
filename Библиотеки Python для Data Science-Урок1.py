#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np

x1 = np.array([[1,2], [1,2], [1,2]])
x2 = np.array([[1,2], [3,4]])

z = np.dot(x1, x2)
print(z)


# ##### Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7. Будем считать, что каждый столбец - это признак, а строка - наблюдение. Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. Результат запишите в массив mean_a, в нем должно быть 2 элемента.

# In[167]:


a = np.array([[1, 2, 3, 3, 1], [6, 8, 11, 10, 7]])
print(a)
mean_a = a.mean(axis=0)
mean_a


# ##### Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков, содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.

# In[46]:


a_centered = a - mean_a
a_centered


# ##### Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1, где N - число наблюдений

# In[117]:


nabludenia, priznak = np.shape(a_centered)
a_centered_sp = (np.dot(a_centered[0], a_centered[1]))/(nabludenia-1)
a_centered_sp


# #### В этом задании проверьте получившееся число, вычислив ковариацию еще одним способом - с помощью функции np.cov. В качестве аргумента m функция np.cov должна принимать транспонированный массив “a”. В получившейся ковариационной матрице (массив Numpy размером 2x2) искомое значение ковариации будет равно элементу в строке с индексом 0 и столбце с индексом 1.

# In[168]:


print(a)
covariation = np.cov(a.T)
covariation


# ##### Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# ##### Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
# ##### [1, 1, 1, 2, 2, 3, 3],['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],[450, 300, 350, 500, 450, 370, 290].

# In[66]:


import pandas as pd

authors = {'author_id':[1, 2, 3], 'author_name':['Тургенев', 'Чехов', 'Островский']}
dtf1 = pd.DataFrame(authors)
print(dtf1)

book = {'author_id':[1, 1, 1, 2, 2, 3, 3], 
        'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 
        'price':[450, 300, 350, 500, 450, 370, 290]}
dtf2 = pd.DataFrame(book)
print(dtf2)


# ##### Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

# In[67]:


authors_price = pd.merge(dtf1, dtf2)
authors_price


# ##### Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

# In[78]:


top5 = authors_price.sort_values(by = 'price', ascending = False).head(5)
top5


# ##### Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# ##### author_name, min_price, max_price и mean_price,
# ##### в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.
# 

# In[164]:


authors_stat1 = authors_price.groupby('author_name', as_index = False).mean()
authors_stat1 = authors_stat1.drop(['author_id'], axis=1).rename(columns={'price':'mean_price'})
authors_stat2 = authors_price.groupby('author_name', as_index = False).max()
authors_stat2 = authors_stat2.drop(['author_id', 'book_title'], axis=1).rename(columns={'price':'max_price'})
authors_stat3 = authors_price.groupby('author_name', as_index = False).min()
authors_stat3 = authors_stat3.drop(['author_id', 'book_title'], axis=1).rename(columns={'price':'min_price'})
authors_stat = authors_stat1.merge(pd.merge(authors_stat2, authors_stat3, how='outer'), how='outer')
print(authors_stat)


# In[ ]:





# In[ ]:





# In[ ]:




