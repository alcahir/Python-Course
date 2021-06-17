
#### Task 6.1
"""
Create 3 Dataframes for csv files __'sales.csv'__, __'houses.csv'__, __'employees.csv'__
"""

# code ...

#### Task 6.2

"""
Extract employee first name/last name from 3 to 10 rows (including) from Employees
"""



#### Task 6.3
"""
Get amount of men/women among all employees (Please use function value_counts())
"""

# code ...


#### Task 6.4
"""
Fill empty cells by 0 in column "square" in houses dataframe
"""

# code ...

#### Task 6.5
"""
Create new column "unit_price" for price/1m2 
(Please use the following formula: price/square) + round the result to 2 digits after point.
"""

# code ...

#### Task 6.6
"""
Sort houses dataframe by price descending and put the result to json file.
"""

# code ...

#### Task 6.7
"""
Please filter employees dataframe and find how much women with name 'Vera' we have
"""

# code ...

#### Task 6.8
"""
Please count how many houses do we have with square >= 100 m2, group by category and subcategory.
"""

# code ...

#### Task 6.9
"""
Put the result from task 7 to file .avro
"""

# code ...

#### Task 6.10
"""
Please update "sales_amount" column according to the following rule "sale_amount" = "sale_amount" + avg("sale_amount")*0.02 (Please try to use apply and lambda for it)
"""

# code ...

#### Task 6.11
"""
Please find all houses that are unsold yet (exists in houses but does not exist in sales, join by house_id). Put house names to .json
"""

# code ...

#### Task 6.12 __OPTIONAL__
"""
Please find sum of sales_amount by each employee, 
put the result to excel (emp_id, emp_first_name, emp_last_name, sum(sales_amount)) 
and mark employees who have less than average sales_amount with red.
"""

# code ...


## DATASETS

# _sales.csv_ - contain houses sales transactions
# _houses.csv_ - list of houses (sold and unsold ones) with their attributes
# _employees_ - list of employees who commit sales