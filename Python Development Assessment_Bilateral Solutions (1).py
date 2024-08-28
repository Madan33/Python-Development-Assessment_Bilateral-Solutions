#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Write a Python function that takes a string as input and reverses it but with a twist: every vowel in the reversed string should be capitalized, and every consonant should be converted to lowercase. For example, if the input is "Hello, World!", the output should be "!dLrOw ,oLlE


# In[3]:


def reverse_and_transform(s):
    vowels = "aeiouAEIOU"
    reversed_s = s[::-1]
    transformed_s = []

    for char in reversed_s:
        if char in vowels:
            transformed_s.append(char.upper())
        elif char.isalpha():
            transformed_s.append(char.lower())
        else:
            transformed_s.append(char)

    return ''.join(transformed_s)

input_string = "Hello, World!"
result = reverse_and_transform(input_string)
print(result)  


# In[ ]:


#2. Design a Python function that takes a list of elements as input and returns the count of unique elements in the list. The function should not utilize any built-in Python libraries or functions related to counting or sets. 


# In[6]:


def count_unique_element(lst):
    unique_elements = []  
    for element in lst:
        is_unique = True
        for unique in unique_elements:
            if element == unique:
                is_unique = False
                break
        if is_unique:
            unique_elements.append(element)
    return len(unique_elements)

example_list = [1, 2, 2, 3, 4, 4, 5]
unique_count = count_unique_element(example_list)
print(unique_count)  


# In[ ]:


#3. Query Writing Challenge:
#Consider a table orders with columns order_id, customer_id, order_date, and total_amount. Write a SQL query to calculate the total revenue generated in the last quarter, grouped by month.


# In[ ]:


SELECT
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    SUM(total_amount) AS total_revenue
FROM
    orders
WHERE
    order_date >= DATE_TRUNC('quarter', CURRENT_DATE) - INTERVAL '1 quarter'
    AND order_date < DATE_TRUNC('quarter', CURRENT_DATE)
GROUP BY
    EXTRACT(YEAR FROM order_date),
    EXTRACT(MONTH FROM order_date)
ORDER BY
    year, month;

