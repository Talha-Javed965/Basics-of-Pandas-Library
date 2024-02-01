#!/usr/bin/env python
# coding: utf-8

# In[65]:


# importing python library
import pandas as pd


# In[66]:


# Creating Dataframe
Data_sheet = pd.DataFrame()


# In[67]:


Data_sheet['Name']=["Talha","Daniel","Mark"]
Data_sheet['Age']=[26,32,24]
Data_sheet['Student']=[False,True,False]


# In[68]:


print (Data_sheet)


# In[71]:


# Adding data into Dataframe
""" One important concept is that the “dataframe” object of Python, consists of rows which are “series” objects instead,
    stack together to form a table.
    Hence adding a new row means creating a new series object and appending it to the dataframe."""
new_row = pd.Series(["Ahmad",29,True], index = ["Name","Age","Student"])
Data_sheet = Data_sheet.append(new_row,ignore_index=True)
#pd.concat([Data_sheet,new_row])
print (Data_sheet) 


# In[83]:


# Support functions in Panda Library, helps to understand the shape of data we are working with

print(" Shape funtion gives the information about the shape of dataframe")
print(Data_sheet.shape,  " rows , columns")

print(" Info funtion gives the information about the data")
print(Data_sheet.info())

print(" Corr funtion gives the information about the relation between the columns")
print(Data_sheet.corr())


# In[84]:


""" Before processing and wrangling any data you need to get the total overview of it,
    which includes statistical conclusions like standard deviation(std),
    mean and it’s quartile distributions."""
# We have the function called Describe, which gives all of that statistical information
print(Data_sheet.describe())


# In[85]:


# In data analysis, sometimes we need to delete unnecessary information 
# for deleting a column from dataframe we will keep axis = 1 and use drop method
print(Data_sheet.drop(["Student"], axis = 1))


# In[86]:


# to drop rows, 2 represent that we want to drop row with index 2
print(Data_sheet.drop(2, axis = 0))


# In[87]:


# to view data without using print command
Data_sheet.head()


# In[ ]:




