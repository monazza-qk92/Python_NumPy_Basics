#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Print data into Python List
data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
print(data)


# In[2]:


## Convert data list into NumPy array for numerical analysis
import numpy as np
grades = np.array(data)
print(grades)


# In[3]:


## Comparing list with numpy array
print (type(data),'x 2:', data * 2)
print('---')
print (type(grades),'x 2:', grades * 2)


# In[4]:


## shape of array
grades.shape


# In[5]:


## accessing first element of array
grades[0]


# In[6]:


## mean of array
grades.mean()


# In[7]:


## add another set of data or array
# Define an array of study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

# Create a 2D array (an array of arrays)
student_data = np.array([study_hours, grades])

# display the array
student_data


# In[8]:


# Show shape of 2D array
student_data.shape


# In[9]:


# Show the first element of the first element
student_data[0][0]


# In[10]:


# Get the mean value of each sub-array
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

print('Average study hours: {:.2f}\nAverage grade: {:.2f}'.format(avg_study, avg_grade))


# In[11]:


## DataFrame 
import pandas as pd

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

df_students 


# In[ ]:




