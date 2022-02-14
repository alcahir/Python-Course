
## Tasks

#### Task 6.1
Create 3 Dataframes for csv files __'sales.csv'__, __'houses.csv'__, __'employees.csv'__

#### Task 6.2
Extract employee first name / last name from 3 to 10 rows (including) from Employees

#### Task 6.3
Get amount of men / women among all employees (Please use function value_counts())

#### Task 6.4
Fill empty cells by 0 in column __"square"__ in __houses__ dataframe

#### Task 6.5
Create new column __"unit_price"__ for __price^1m2__ (Please use the following formula: _price / square_) + round the result to 2 digits after point.

#### Task 6.6
Sort __houses__ dataframe by __price__ descending and put the result to json file.

#### Task 6.7
Please filter __employees__ dataframe and find how much women with name __'Vera'__ we have

#### Task 6.8
Please count how many houses do we have with square >= 100 m2, group by category and subcategory.

#### Task 6.9
Put the result from task 7 to file __'.avro'__

#### Task 6.10
Please update __"sales_amount""__ column according to the following rule __"sale_amount"__ = __"sale_amount"__ + __avg(sale_amount)__ * 0.02 (Please try to use apply and lambda for it)

#### Task 6.11
Please find all houses that are unsold yet (exists in houses but does not exist in sales, join by house_id).  
Put house ids to __.json__ ('output_files/task_11.json'). Put result list of unique house names into `house_ids_available` list.

#### Task 6.12 __(OPTIONAL)__
Please find sum of __sales_amount__ by each employee, put the result to excel (__emp_id__, __emp_first_name__, __emp_last_name__, sum(__sales_amount__)) and mark employees who have less than average __sales_amount__ with red.

## DATASETS

* _sales.csv_ - contain houses sales transactions
* _houses.csv_ - list of houses (sold and unsold ones) with their attributes
* _employees_ - list of employees who commit sales