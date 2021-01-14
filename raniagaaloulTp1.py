#!/usr/bin/env python
# coding: utf-8

# 
# # TP1 Probabilité et statistique
# <html>
#    <head>
#       <title>HTML Base Tag Example</title>
#       <base href = "https://github.com/nevermind78/Proba_stat_4_LM" />
#    </head>
#    <body>
#       <img src = "https://th.bing.com/th/id/OIP.Quijt6_GuJ-OzuMSNQ_S1gHaHa?pid=Api&rs=1" width="200" alt = "Logo Image"/>
#     </body>
# 
# </html>
# 

# In[1]:


from __future__ import print_function
import numpy as np
import pandas as pd
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


# ## Probabilités - approche fréquentiste
# ### Définition par la fréquence relative :
# * une expérience d’ensemble fondamental  est exécutée plusieurs fois sous les mêmes conditions.
# * Pour chaque événement E de , n(E) est le nombre de fois où l’événement E survient lors des n premières répétitions de l’expérience.
# * P(E), la probabilité de l’événement E est définie de la manière suivante :
# 
# $$P(E)=\lim_{n\to\infty}\dfrac{n(E)}{n} $$ 

# ## Simulation d'un dé parfait

# In[2]:


# seed the random number generator
np.random.seed(1)

# Example: sampling 
#
# do not forget that Python arrays are zero-indexed,
# and the 2nd argument to NumPy arange must be incremented by 1
# if you want to include that value
n = 6
k = 200000
T=np.random.choice(np.arange(1, n+1), k, replace=True)
unique, counts = np.unique(T, return_counts=True)
dic=dict(zip(unique, counts))
df=pd.DataFrame(list(dic.items()),columns=['i','Occurence'])
df.set_index(['i'], inplace=True)
df['Freq']=df['Occurence']/k
df['P({i})']='{}'.format(1/6)
df


# ## Ajouter de l'intéraction 

# In[3]:


def dice_sim(k=100):
    n = 6    
    T=np.random.choice(np.arange(1, n+1), k, replace=True)
    unique, counts = np.unique(T, return_counts=True)
    dic=dict(zip(unique, counts))
    df=pd.DataFrame(list(dic.items()),columns=['i','Occurence'])
    df.set_index(['i'], inplace=True)
    df['Freq']=df['Occurence']/k
    df['P({i})']='{0:.3f}'.format(1/6)
    return df
    


# In[4]:


dice_sim(100)


# In[5]:


interact(dice_sim,k=widgets.IntSlider(min=1000, max=50000, step=500, value=10));


# ## Cas d'un dé truqué

# In[6]:


p=[0.1, 0.1, 0.1, 0.1,0.1,0.5]
sum(p)


# In[7]:


def dice_sim(k=100,q=[[0.1, 0.1, 0.1, 0.1,0.1,0.5],[0.2, 0.1, 0.2, 0.1,0.1,0.3]]):
    n = 6
    qq=q
    T=np.random.choice(np.arange(1, n+1), k, replace=True,p=qq)
    unique, counts = np.unique(T, return_counts=True)
    dic=dict(zip(unique, counts))
    df=pd.DataFrame(list(dic.items()),columns=['i','Occurence'])
    df.set_index(['i'], inplace=True)
    df['Freq']=df['Occurence']/k
    df['P({i})']=['{0:.3f}'.format(j) for j in q]
    return df


# In[8]:


interact(dice_sim,k=widgets.IntSlider(min=1000, max=50000, step=500, value=10));


# ## Exercice 1: 
# 
# Tester l'intéraction précédente pour plusieurs valeurs de `p`
# Donner votre conclusion :

# In[9]:


# Conclusion 
la probabilité est equiprobable :10.6=0.6666666666666666666666666
    la frequence depend d'occurence et de nombre de simulations
    la fréquence donne une valeur plus précise en augmentant de la valeur d'occurence (l'augmentation de l'intervalle de simulations 
    engendre une augmentation du valeur d'occurences choisi)
    les valeurs de i sont :
        choisi aléatoirement
        unique(pas de répitition)
        arrangéesde 1 à n
        justification:random.choici(np.arrange(1,n+1))





# ## Permutation Aléatoire

# In[10]:


np.random.seed(2)

m = 1
n = 10

v = np.arange(m, n+1)
print('v =', v)

np.random.shuffle(v)
print('v, shuffled =', v)


# ## Exercice 2
# Vérifier que les permutation aléatoires sont uniforme , c'est à dire que la probabilité de générer une permutation d'élement de {1,2,3} est 1/6.
# En effet les permutations de {1,2,3} sont :
# * 1 2 3
# * 1 3 2
# * 2 1 3
# * 2 3 1
# * 3 1 2
# * 3 2 1
# 

# In[11]:


k =10
m = 1
n = 3
v = np.arange(m, n+1)
T=[]
for i in range(k):
    np.random.shuffle(v)
    w=np.copy(v)
    T.append(w)


# In[12]:


TT=[str(i) for i in  T]
TT


# In[13]:


k =1000
m = 1
n = 3
v = np.arange(m, n+1)
T=[]
for i in range(k):
    np.random.shuffle(v)
    w=np.copy(v)
    T.append(w)

TT=[str(i) for i in  T]
unique, counts = np.unique(TT, return_counts=True)
dic=dict(zip(unique, counts))
df=pd.DataFrame(list(dic.items()),columns=['i','Occurence'])
df.set_index(['i'], inplace=True)
df['Freq']=df['Occurence']/k
df['P({i,j,k})']='{0:.3f}'.format(1/6)
df


# ### Donner  votre conclusion en expliquant le script 

# In[14]:


## Explication 

la probabilité n'est pas equipropable et on a deux cas de probabilité 
 np.random.shuffle(v):
Cette fonction mélange uniquement le tableau le long du premier axe d'un tableau multidimensionnel.
L'ordre des sous-tableaux est modifié mais leur contenu reste le même
w=np.copy(v)
Renvoie une copie de tableau de l'objet donné
T.append(w):
The append() method adds an item to the end of the list.
la fréquence donne une valeur plus précise  en augmentant de la valeur d'occurence (l'augmentation de l'intervalle de simulations 
    engendre une augmentation du valeur d'occurences choisi)
    ==> la fréquence dépend d'occurence et de nombre de simulations









# ## Probabilité conditionnelle 

# Rappelons que l'interprétation fréquentiste de la probabilité conditionnelle basée sur un grand nombre `n` de répétitions d'une expérience est $ P (A | B) ≈ n_ {AB} / n_ {B} $, où $ n_ {AB} $ est le nombre de fois où $ A \cap B $ se produit et $ n_ {B} $ est le nombre de fois où $ B $ se produit. Essayons cela par simulation et vérifions les résultats de l'exemple 2.2.5. Utilisons donc [`numpy.random.choice`] (https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.choice.html) pour simuler les familles` n`, chacun avec deux enfants.
# 

# In[15]:


np.random.seed(34)

n = 10**5
child1 = np.random.choice([1,2], n, replace=True) 
child2 = np.random.choice([1,2], n, replace=True) 

print('child1:\n{}\n'.format(child1))

print('child2:\n{}\n'.format(child2))


# Ici, «child1» est un «tableau NumPy» de longueur «n», où chaque élément est un 1 ou un 2. En laissant 1 pour «fille» et 2 pour «garçon», ce «tableau» représente le sexe du enfant aîné dans chacune des familles «n». De même, «enfant2» représente le sexe du plus jeune enfant de chaque famille.
# 

# In[16]:


np.random.choice(["girl", "boy"], n, replace=True)


# mais il est plus pratique de travailler avec des valeurs numériques.
# 
# Soit $ A $ l'événement où les deux enfants sont des filles et $ B $ l'événement où l'aîné est une fille. Suivant l'interprétation fréquentiste, nous comptons le nombre de répétitions où $ B $ s'est produit et le nommons `n_b`, et nous comptons également le nombre de répétitions où $ A \cap B $ s'est produit et le nommons` n_ab`. Enfin, nous divisons `n_ab` par` n_b` pour approximer $ P (A | B) $.

# In[17]:


n_b = np.sum(child1==1)
n_ab = np.sum((child1==1) & (child2==1))

print('P(both girls | elder is girl) = {:0.2F}'.format(n_ab / n_b))


# L'esperluette `&` est un élément par élément $ AND $, donc `n_ab` est le nombre de familles où le premier et le deuxième enfant sont des filles. Lorsque nous avons exécuté ce code, nous avons obtenu 0,50, confirmant notre réponse $ P (\text {les deux filles | l'aîné est une fille}) = 1/2 $.
# 
# Soit maintenant $ A $ l'événement où les deux enfants sont des filles et $ B $ l'événement selon lequel au moins l'un des enfants est une fille. Alors $ A \cap B $ est le même, mais `n_b` doit compter le nombre de familles où au moins un enfant est une fille. Ceci est accompli avec l'opérateur élémentaire $ OR $ `|` (ce n'est pas une barre de conditionnement; c'est un $ OR $ inclusif, retournant `True` si au moins un élément est` True`).

# In[18]:


n_b = np.sum((child1==1) | (child2==2))
n_ab = np.sum((child1==1) & (child2==1))

print('P(both girls | at least one girl) = {:0.2F}'.format(n_ab / n_b))


# Pour nous, le résultat était de 0,33, confirmant que $ P (\text {les deux filles | au moins une fille}) = 1/3 $.
