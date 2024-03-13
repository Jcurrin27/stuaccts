# Student Accounts
#### Introduction:
This program is designed primarily as a validation of fundamental skills in python, database management, and business intelligence solutions.
However, the program also serves as a conceptual backbone from which there is opportunity to branch off into more sophisticated developments
that could be implemented across different higher education institutions. At its most basic, this program asks the user how many students
the user would like to generate random student data for, it then generates data for this number of students, inserts the data into the stuaccts.db
sqlite3 database, retrieves an aggregate dataset from the database, prints a refined version of the student data aggregation for the user, and then deletes all data from the database.

For context, the student data revolves around student accounts receivables as this is my background as a higher education administrator, and it was the catalyst for my studying computer programming and data analytics. The program simulates a dataset that is produced by universities across the nation during the start of a new semester. As students register for classes, they generate charges, and administrators must ensure that they have sufficient funding to cover their charges before classes begin. If students still owe a balance by the payment deadline, administrators are often required by law to drop all of the student's classes for the term.

#### Randomized Data:
Much of the work put into this program is dedicated to the process of creating a randomized, student-centric dataset to use for aggregation. Specifically, there are four tables being populated by the generated data: students, charges, payments, and indicators. Each of these datasets are randomly generated in a very similar style. Though the datasets need to be randomized to some extent, the randomization could also be modified or improved with some deliberate tinkering to introduce patterns common to actual student receivables data found in a university.

#### Higher Education Implications:
I mentioned earlier that I was motivated to study computer programming and data analytics as a result of my time as an adminstrator in student accounts receivables. My motivation was spurred by the lack of infrastructure dedicated to sifting through out student data in pursuit of student success. While we had mountains of valuable student data, we had essentially zero structure to creating insights to predict student attrition, or identify students who we could position for success if we identified them two months before the payment deadline rather than two days before the payment deadline.

For example, students with an indicator that they have available financial aid, yet still owe a large balance are opportunities to connect with staff members early to work through whatever obstacles they have in actually applying financial aid towards their balance.

My hope is that this program demonstrates, at a basic level, the type of data analytics infrastructure possible for working with student data. Again, this program was built within the scope of this course and not designed to represent the most sophisticated product, but more as a pointer to the posibilities for administrators who are empowered with more advanced tools for working with student data.


