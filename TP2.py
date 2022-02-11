#!/usr/bin/env python
# coding: utf-8

# In[1]:


prenom = (input("Entrez votre prenom: "))
nom =(input("Entrez votre nom: "))
print(nom, prenom)


# In[1]:


n = input("Entrez la valeur: ")
nn= str(n)+str(n)
nnn = str(n)+str(n)+str(n)
print(int(n)+int(nn)+int(nnn))


# 

# In[22]:


n = input('Entrez une valeur: ')
n = int(n)
if n%2 !=0:
    print(n, "est impair")
else:
    print(n, "est pair")
        


# In[25]:


for i in range(2000,3201):
 if not i%5 ==0 and i//7:
    print(i)
    


# In[16]:


Num = 1
n = int(input("Entre la valeur de n: "))
for i in range(1,n+1):
    Num = Num * i
    print("Factorielle de", n, "est: ", Num)


# In[6]:


n = int(input("Entrez la valeur du n: "))
if n >= 500:
    prix = n*0.5
elif n in range(200,500):
        prix = n*0.3
elif n < 200:
        prix = n*0.1
        print("Le prix est: ", prix)
else:
        print("Le prix est: ", n)
    


# In[9]:





# In[ ]:




