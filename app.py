import os
import re
import string
import sqlite3
import csv
import random
import sqlite3
from datetime import datetime, timedelta
import pandas as pd

from helpers import generate_studentids, insert_students, generate_payments_data, insert_payments, get_students, generate_charges_data, insert_charges, generate_indicator_data, insert_indicators

# get number of students from the user
students = get_students()

# generate randomized ids for students
student_ids = generate_studentids(students)

# insert student ids into students table in stuaccts.db
insert_students(student_ids)

# generate randomized payment data for students
payments_data = generate_payments_data(student_ids, students)

# insert randomized payment data into payments table in stuaccts.db
insert_payments(payments_data)

# generate randomized charges data for students
charges_data = generate_charges_data(student_ids, students)

# insert randomized charges data into charges table in stuaccts.db
insert_charges(charges_data)

# generate randomized indicator data for students
indicator_data = generate_indicator_data(student_ids, students)

insert_indicators(indicator_data)

# connect to database
conn = sqlite3.connect('stuaccts.db')
cursor = conn.cursor()

# empty student data container
student_data = []

# get student data
for row in cursor.execute("""SELECT DISTINCT s.id,
SUM(c.amount) - SUM(p.amount) AS balance,

CASE
    WHEN SUM(c.amount) - SUM(p.amount) < 0  THEN 'refund due'
    WHEN SUM(c.amount) - SUM(p.amount) BETWEEN 0 AND 1500 THEN '0-1500'
	WHEN SUM(c.amount) - SUM(p.amount) BETWEEN 1500 AND 5000 THEN '1500-5000'
	WHEN SUM(c.amount) - SUM(p.amount) BETWEEN 5000 AND 10000 THEN '5000-10000'
	WHEN SUM(c.amount) - SUM(p.amount) > 10000 THEN 'greater than 10000'
END AS balance_bucket

FROM students s
LEFT JOIN payments p on p.student_id = s.id
LEFT JOIN charges c on c.student_id = s.id
GROUP BY s.id;"""):
	#append each row of query to empty container
	student_data.append(row)

# convert student_data container to pandas df for further manipulation
columns = ["id", "balance", "balance_bucket"]
df = pd.DataFrame(student_data,columns=columns)

# fill NaN values with average balance
average_balance = df["balance"].mean()
df["balance"].fillna(average_balance, inplace=True)

# round out the balance values
df["balance"] = df["balance"].round(2)


# function to assign 'balance_bucket' based on the 'balance' value
def assign_balance_bucket(balance):
    if balance < 0 :
         return 'refund due'
    elif 0 <= balance <= 1500:
        return '0-1500'
    elif 1500 <= balance <= 5000:
        return '1500-5000'
    elif 5000 <= balance <= 10000:
        return '5000-10000'
    else:
        return 'greater than 10000'

# call balance bucket function
df['balance_bucket'] = df['balance'].apply(assign_balance_bucket)

# create pivot table based on df
pivot1 = pd.pivot_table(df, values='id',index='balance_bucket',aggfunc='count', sort='True')

# print df
print(pivot1)

# delete all data from database
cursor.execute("delete from payments;")
cursor.execute("delete from charges;")
cursor.execute("delete from indicators;")
cursor.execute("delete from students;")
conn.commit()
conn.close()

