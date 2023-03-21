#!/usr/bin/env python
# coding: utf-8

# In[83]:


import os
import shutil


# In[84]:


#1
def createfolder(name):
    if not os.path.exists(source+name):
        os.mkdir(source+name)
    else:
        return 'Файла нет'


# In[85]:


#2
def delfolder(name):
    if os.path.exists(source+name):
        os.rmdir(source+name)
    else:
        return 'Файла нет'


# In[86]:


#3
def down(temp):
    global source
    l=[]
    for i in range(len(temp)):
        if temp[i]=='/':
            l.append(i)
            
    ind=l[-2]
    source = temp[:ind]+'/'

def move():
    global source
    while True:
        print('Зайти или подняться (STOP если уже всё)')
        do=input()
        if do=='зайти':
            name=input('Введите имя папки ')
            if os.path.exists(source+name+'/'):
                source=source+name+'/'
            else:
                print('Папки нет')
        elif do == 'подняться':
            down(source)
            print('Вы сейчас в ', source)
        elif do=='STOP':
            print('Вы сейчас в', source)
            break


# In[87]:


#4
def createfile(name):
    fullname=source+name+'.txt'
    open(fullname, 'tw').close()


# In[88]:


#5
def writetext(name):
    text=input('Содержимое: ')
    with open(source+name+'.txt', 'w') as f:
        f.write(text)


# In[89]:


#6
def check(name):
    with open(source+name+'.txt', 'r') as f:
        a=f.read()
    print(a)


# In[90]:


#7
def delfile(name):
    if os.path.exists(source+name+'.txt'):
        os.remove(source+name+'.txt')
    else:
        return 'Файла нет'


# In[91]:


#8
def copyfile(name):
    if os.path.exists(source+name+'.txt'):
        source2=input('Введите путь, куда копировать файл ')
        shutil.copyfile(source+name+'.txt', source2+name+' - copy.txt')
    else:
        return 'Файла нет'


# In[92]:


#9
def movefile(name):
    if os.path.exists(source+name+'.txt'):
        source2=input('Введите путь, куда переместить файл файл ')
        shutil.copyfile(source+name+'.txt', source2+name+'.txt')
        os.remove(source+name+'.txt')
    else:
        return 'Файла нет'


# In[93]:


#10
def renamefile(name):
    if os.path.exists(source+name+'.txt'):
        namenew=input('Введите новое имя файла ')
        os.rename(source+name+'.txt',source+namenew+'.txt')
    else:
        print('Файла нет')


# In[82]:


source='C:/python/manager/'
while True:
    n = input(('1. Создать папку \n 2. Удалить папку \n 3. Переместить папку \n 4. Создать пустой файл \n 5. Запись текста в файл \n 6. Просмотреть содержимое текстового файла \n 7. Удалить файл \n 8. Копировать файл \n 9. Переместить файл\n 10. Переименовать файл. \n 11. Настройки. \n'))
    n=int(n)
    if n == 11:
        print('Можете поменять корневую папку. Сейчас она - ', source)
        k=input('Y / N ')
        if k=='Y':
            source=input('Введите корневую папку ')
            source+='/'
    
    elif n == 1:
        name=input('Введите имя папки ')
        createfolder(name)
        
    elif n == 2:
        name=input('Введите имя папки ')
        delfolder(name)
        
    elif n == 3:
        move()
        
    elif n == 4:
        name=(input('Введите имя файла '))
        createfile(name)
        
    elif n == 5:
        name=input('Введите имя файла ')
        writetext(name)
        
    elif n == 6:
        name=input('Введите имя файла ')
        check(name)
        
    elif n == 7:
        name=input('Введите имя файла ')
        delfile(name)
        
    elif n == 8:
        name=input('Введите имя файла ')
        copyfile(name)
        
    elif n == 9:
        name=input('Введите имя файла ')
        movefile(name)
        
    elif n == 10:
        name=input('Введите имя файла ')
        renamefile(name)

