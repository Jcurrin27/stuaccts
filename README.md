# Student Accounts
#### Introduction:
This program is designed primarily as a validation of fundamental skills in python, database management, and business intelligence solutions.
This program asks the user how many students the user would like to generate random student data for, it then generates data for this number of students, inserts the data into the stuaccts.db sqlite3 database, retrieves an aggregate dataset from the database, prints student data aggregation for the user, and then deletes all data from the database.

For context, the student data revolves around student accounts receivables as this is my background as a higher education administrator, and it was the catalyst for my studying computer programming and data analytics. The program simulates a dataset that is produced during the start of a new semester. As students register for classes, they generate charges, and administrators must ensure that they have sufficient funding to cover their charges before classes begin. If students still owe a balance by the payment deadline, administrators are often required by law to drop all of the student's classes for the term.

#### Randomized Data:
Much of the work put into this program is dedicated to the process of creating a randomized, student-centric dataset to use for aggregation. Specifically, there are four tables being populated by the generated data: students, charges, payments, and indicators. Each of these datasets are randomly generated in a very similar style. Though the datasets need to be randomized to some extent, the randomization could also be modified or improved with some deliberate tinkering to introduce patterns common to actual student receivables data found in a university.




