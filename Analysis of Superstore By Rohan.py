#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv("Sample - Superstore.csv", encoding='cp1252')
df


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.columns


# In[7]:


df.describe()


# In[8]:


df.isna().sum()


# In[9]:


df.duplicated().sum()


# In[10]:


df_cat = df[[ 'Ship Mode', 'Customer ID', 'Customer Name',
             'Segment', 'Country', 'City', 'State', 'Region',
             'Product ID', 'Category', 'Sub-Category', 'Product Name']]


# In[11]:


df_cat.head()


# In[12]:


for feature in df_cat.columns:
    print(feature,':',df[feature].nunique())


# In[13]:


df['Order Date'].nunique()


# In[14]:


df['Ship Date'].nunique()


# In[15]:


df.head()


# In[16]:


df.tail()


# In[17]:


product_group = df.groupby(["Product Name"]).sum()["Sales"]
product_group.head()


# In[18]:


top_selling_products = product_group.sort_values(ascending=False)
top_5_selling_products = pd.DataFrame(top_selling_products.head())
top_5_selling_products


# In[19]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


top_5_selling_products.plot(kind="bar")

# Add a title to the plot
plt.title("Top 5 Selling Products in Superstore")

# Add labels to the x and y axes
plt.xlabel("Product Name")
plt.ylabel("Total Profit")

# Show the plot
plt.show()


# In[21]:


product_group = df.groupby(["Product Name"]).sum()["Profit"]

top_profit_products = product_group.sort_values(ascending=False)

top_5_profit_products =pd.DataFrame(top_profit_products[:5])
top_5_profit_products


# In[22]:


top_5_profit_products.plot(kind="bar")

plt.title("Top 5 Profit Products in Superstore")

plt.xlabel("Product Name")
plt.ylabel("Total Profit")

plt.show()


# In[23]:


top_5_profit_products.index == top_5_selling_products.index


# In[24]:


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,5))

# Plot the top 5 selling products in the first column
top_5_selling_products.plot(kind="bar", y="Sales", ax=ax1)

# Set the title for the first plot
ax1.set_title("Top 5 Selling Products")

# Plot the top 5 profit products in the second column
top_5_profit_products.plot(kind="bar", y="Profit", ax=ax2)

# Set the title for the second plot
ax2.set_title("Top 5 Profit Products")

# Show the plot
plt.show()


# In[25]:


list(top_5_profit_products.index)


# In[26]:


list(top_5_selling_products.index)


# In[27]:


df.Region.value_counts()


# In[28]:


product = df[df["Product Name"] == "Canon imageCLASS 2200 Advanced Copier"]

# Group the data by Region
region_group = product.groupby(["Region"]).mean()[["Sales", "Profit"]]

# Ploting
region_group.plot(kind="bar")

plt.show()


# In[29]:


product = df[df["Product Name"] == "Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind"]

# Group the data by Region
region_group = product.groupby(["Region"]).mean()[["Sales", "Profit"]]

# Plot the average sales and profit by region
region_group.plot(kind="bar")

# Show the plot
plt.show()


# In[30]:


product = df[(df["Product Name"] == "Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind") & (df["Region"] == "Central")]
product


# In[31]:


product = df[(df["Product Name"] == "Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind") & (df["Region"] == "Central")]

# Plot a histogram of the discounts offered for the product in the central region
product["Discount"].plot(kind="bar")

# Show the plot
plt.show()
product


# In[32]:


df['Order Date'] = pd.to_datetime(df['Order Date'])


# In[33]:


monthly_sales = df.groupby(['Order Date'], as_index=False).sum()

# Set the Order Date column as the index of the dataframe
monthly_sales = monthly_sales.set_index('Order Date')
# Resample the data into monthly intervals
monthly_sales = monthly_sales.resample('M').sum() # M for month

# Plot
plt.figure(figsize=(25,10))
plt.plot(monthly_sales['Sales'])
plt.xlabel("Order Date")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.show()


# In[34]:


yearly_sales = monthly_sales.resample('Y').sum()


plt.figure(figsize=(25,10))
plt.plot(yearly_sales['Sales'])
plt.xlabel("Order Date")
plt.ylabel("Sales")
plt.title("yearly Sales Trend")
plt.show()


# In[35]:


monthly_sales = df.groupby(['Order Date'], as_index=False).sum()

# Set the Order Date column as the index of the dataframe
monthly_sales = monthly_sales.set_index('Order Date')

# Resample the data into monthly intervals
monthly_sales = monthly_sales.resample('M').sum() # M for month

# Plot
plt.figure(figsize=(25,8))
plt.plot(monthly_sales['Profit'])
plt.xlabel("Order Date")
plt.ylabel("Profit")
plt.title("Monthly Profit Trend")
plt.show()


# In[36]:


yearly_sales = monthly_sales.resample('Y').sum()


plt.figure(figsize=(25,10))
plt.plot(yearly_sales['Profit'])
plt.xlabel("Order Date")
plt.ylabel("Profit")
plt.title("yearly Sales Trend")
plt.show()


# In[37]:


df_places = df[['Country','City','State','Region']]
df_places.head()


# In[38]:


for place in df_places.columns:
    print(place,':',df_places[place].nunique())


# In[39]:


df_places = df[['City','State','Region','Sales','Profit']]
df_places.head()


# In[40]:


region_sales = df_places.groupby(['Region'], as_index=False).sum()
region_sales.sort_values(by='Sales', ascending=False, inplace=True)

# Plot the total sales geProfitnerated by each region and city
plt.figure(figsize=(10,5))
plt.bar(region_sales['Region'], region_sales['Sales'], align='center',)
plt.xlabel("Region")
plt.ylabel("Sales")
plt.title("Sales Generated by Region")
plt.xticks(rotation=90)
plt.show()
region_sales


# In[41]:


region_profit = df_places.groupby(['Region'], as_index=False).sum()
region_profit.sort_values(by='Profit', ascending=False, inplace=True)

# Plot the total sales generated by each region and city
plt.figure(figsize=(10,5))
plt.bar(region_profit['Region'], region_profit['Profit'], align='center',)
plt.xlabel("Region")
plt.ylabel("Profit")
plt.title("Profit Generated by Region")
plt.xticks(rotation=90)
plt.show()
region_profit


# In[42]:


state_sales = df_places.groupby(['State'], as_index=False).sum()
state_sales.sort_values(by='Sales', ascending=False, inplace=True)


plt.figure(figsize=(22,10))
plt.bar(state_sales['State'], state_sales['Sales'], align='center',)
plt.xlabel("State")
plt.ylabel("Sales")
plt.title("Sales Generated by State")
plt.xticks(rotation=90)

plt.show()
state_sales


# In[43]:


state_profit = df_places.groupby(['State'], as_index=False).sum()
state_profit.sort_values(by='Profit', ascending=False, inplace=True)


plt.figure(figsize=(22,10))
plt.bar(state_profit['State'], state_profit['Profit'], align='center',)
plt.xlabel("State")
plt.ylabel("Profit")
plt.title("Sales Generated by State")
plt.xticks(rotation=90)

plt.show()
state_profit


# In[44]:


city_sales = df_places.groupby('City', as_index=False).sum()

# Sort the data by Sales in descending order
city_sales.sort_values(by='Sales', ascending=False, inplace=True)

# Select the top 5 cities
top_5_cities_sales = city_sales.head()

plt.bar(top_5_cities_sales['City'], top_5_cities_sales['Sales'], align='center')
plt.xlabel("City")
plt.ylabel("Sales")
plt.title("Top 5 Cities by Sales")
plt.xticks(rotation=90)
plt.show()
top_5_cities_sales


# In[45]:


city_profit = df_places.groupby('City', as_index=False).sum()

# Sort the data by Sales in descending order
city_profit.sort_values(by='Profit', ascending=False, inplace=True)

# Select the top 5 cities
top_5_cities_profit =city_profit.head()

plt.bar(top_5_cities_profit['City'], top_5_cities_profit['Profit'], align='center')
plt.xlabel("City")
plt.ylabel("Profit")
plt.title("Top 5 Cities by Profit")
plt.xticks(rotation=90)

plt.show()
top_5_cities_profit


# In[46]:


df.head()


# In[47]:


df.Discount.value_counts()


# In[48]:


discount_group = df.groupby(["Discount"]).mean()[["Sales"]]

ax = discount_group.plot(kind="bar")

ax.set_ylabel("Sales")

plt.show()


# In[49]:


discount_group = df.groupby(["Discount"]).mean()[["Sales"]]

ax = discount_group.plot(kind="bar")

ax.set_ylabel("Sales")

plt.show()


# In[50]:


discount_group = df.groupby(["Discount"]).mean()[["Sales"]]

ax = discount_group.plot(kind="bar")

ax.set_ylabel("Sales")

plt.show()


# In[51]:


discount_group = df.groupby(["Discount"]).sum()[["Profit"]]

ax = discount_group.plot(kind="bar")

ax.set_ylabel("Profit")

plt.show()


# In[52]:


avg_profit_margin_by_category = df.groupby('Category')['Profit'].sum()

print(avg_profit_margin_by_category)


# In[53]:


df['Profit Margin'] = df['Profit'] / df['Sales']

# Group the data by product category and calculate the average profit margin for each category
avg_profit_margin_by_category = df.groupby('Category')['Profit Margin'].mean()

# Plot the average profit margin for each category as a bar chart
avg_profit_margin_by_category.plot(kind='bar')

# Add a title and labels to the chart
plt.title("Average Profit Margin by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Average Profit Margin")

plt.show()


# In[54]:


df.head()


# In[55]:


df.Segment.value_counts()


# In[56]:


df['Ship Mode'].value_counts()


# In[ ]:




