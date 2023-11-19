#!/usr/bin/env python
# coding: utf-8

# #                        Project Title:
# ##                          Analysis Of Students Exam Scores.
# #### Analytics questions:
# ##### What factors (features) affect test scores most?
# ##### Are there interacting features which affect test scores?
# 
# ##### Author : Shinde Pragati Satish.

# # Import Libraries

# In[15]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Load Dataset

# In[24]:


df=pd.read_csv("Student.csv")
pd.options.display.max_rows=350000
df


# In[17]:


df.head()


# ##  Exploratory Data Analysis

# In[18]:


df.info()


# In[19]:


df.describe()


# # Data Cleaning

# In[20]:


df.isnull().sum()


# # Drop unnamed column

# In[21]:


df=df.drop("Unnamed: 0",axis=1)
print(df.head())


# # Change weekly study hours column

# In[22]:


df["WklyStudyHours"]=df["WklyStudyHours"].str.replace("05-Oct","5-10")
df.head()


# # Gender Disribution

# In[34]:


gd=sns.countplot(data=df,x="Gender")
plt.title("Gender Disribution")
plt.figure(figsize=(3,3))
for i in gd.containers:
    gd.bar_label(i,)
plt.show()


# ## Conclusion:
# ### From the above chart we have analysed that the number of females in the data is more than the number of males.

# # Relationship between Parent's Education and Student's Score

# In[12]:


gb=df.groupby("ParentEduc").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb)


# In[13]:


sns.heatmap(gb,annot=True)
plt.title("Relationship between Parent's Education and Student's Score")
plt.figure(figsize=(10,8))
plt.show()


# ## Conclusion:
# ### From the above chart we have conclude that the education of the parent have a good impact on their scores.

# # Relationship between Parent's Marital Status and Student's Score

# In[14]:


gb1=df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
gb1


# In[15]:


sns.heatmap(gb1,annot=True)
plt.title("Relationship between Parent's Marital Status and Student's Score")
plt.show()


# ## Conclusion:
# ### From above chart we have conclude that there is no/negligible impact on the student's score due to their parent's marital status.

# # Detection of Outlier in Score:

# In[34]:


# Create a figure with 3 subplots:
fig, axes = plt.subplots(1, 3, figsize=(12, 5))

# Plot 1: MathScore Distribution:
sns.boxplot(data=df,x="MathScore",ax=axes[0])

# Plot 2: ReadingScore Distribution:
sns.boxplot(data=df,x="ReadingScore",ax=axes[1])

# Plot 2: WritingScore Distribution:
sns.boxplot(data=df,x="WritingScore",ax=axes[2])

# Adjust the spacing between subplots:
plt.tight_layout()

# Display the plots:
plt.show()


# # Conclusion:
# ### From above chart we have conclude that there is minimum value is very low in the  Math Score as compaire to Reading Score and Writing Score.

# # Analyze exam scores based on weekly study hours

# In[20]:


# Create a figure with 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(12, 5))

# Plot 1: MathScore Distribution
sns.boxplot(data=df, x='WklyStudyHours', y='MathScore', ax=axes[0])
axes[0].set_title('MathScore based on WklyStudyHours')

# Plot 2: ReadingScore Distribution
sns.boxplot(data=df, x='WklyStudyHours', y='WritingScore', ax=axes[1])
axes[1].set_title('WritingScore based on WklyStudyHours')

# Plot 2: WritingScore Distribution
sns.boxplot(data=df, x='WklyStudyHours', y='ReadingScore', ax=axes[2])
axes[2].set_title('ReadingScore based on WklyStudyHours')

# Adjust the spacing between subplots
plt.tight_layout()

# Display the plots
plt.show()


# # Conclusion:
# ### The student who spends more than 10 hours weekly studying seems to have a good performance in the math exam,but in writing and reading there's no significant differnce.

# # Analyze exam scores based on gender:

# In[40]:


# Create a figure with 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(12, 5))

# Plot 1: MathScore Distribution
sns.boxplot(data=df, x='Gender', y='MathScore', ax=axes[0])
axes[0].set_title('MathScore')

# Plot 2: ReadingScore Distribution
sns.boxplot(data=df, x='Gender', y='WritingScore', ax=axes[1])
axes[1].set_title('WritingScore')

# Plot 2: WritingScore Distribution
sns.boxplot(data=e, x='Gender', y='ReadingScore', ax=axes[2])
axes[2].set_title('ReadingScore')

# Adjust the spacing between subplots
plt.tight_layout()

# Display the plots
plt.show()


# ## Conclusion:
# ### Female student seems to have a good performance in writing and reading, while male student has a good performance in math.
# ### There’s no male student gets 0 score on all exams, while there are female students who get 0 score in math.

# # Distribution of Ethnic Group:

# In[5]:


print(df["EthnicGroup"].unique())


# In[37]:


groupA=df.loc[(df["EthnicGroup"]=="group A")].count()
groupB=df.loc[(df["EthnicGroup"]=="group B")].count()
groupC=df.loc[(df["EthnicGroup"]=="group C")].count()
groupD=df.loc[(df["EthnicGroup"]=="group D")].count()
groupE=df.loc[(df["EthnicGroup"]=="group E")].count()

mylist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
print(mylist)

l=["groupA","groupB","groupC","groupD","groupE"]

plt.title("Distribution of Ethnic Groups")
plt.pie(mylist,labels=l,autopct="%1.2f%%",shadow=True)

plt.legend(loc="center")
plt.show()


# ## Conclusion:
# ### Ethnic groupC are larger than other ethinic group .

# In[ ]:




