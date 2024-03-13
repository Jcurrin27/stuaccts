# helpers.py

import os
import re
import sqlite3
import random
import string
import sqlite3
from datetime import datetime, timedelta

def get_students():
    while True:
        students = int(input("students:"))
        if students >= 0:
            break

    return students

# Function to generate random student data
def generate_studentids(students):
    student_ids = set()

    for _ in range(students):
        student_id = ''.join(random.choices(string.digits, k=8))
        student_ids.add(student_id)

    return list(student_ids)

# # Function to insert data into the database
def insert_students(student_ids):
    conn = sqlite3.connect('stuaccts.db')
    cursor = conn.cursor()

    # Insert data into the 'students' table
    for student_id in student_ids:
        cursor.execute('INSERT INTO students VALUES (?)', (student_id,))

    conn.commit()
    conn.close()

def generate_payments_data(student_ids, students):
    payment_types = ['Credit Card', 'Debit Card', 'Cash', 'Check', 'Financial Aid', 'Sponsored Payment', 'Waiver', 'Exemption']

    payments_data = []

    for _ in range(students):
        payment_id = None

        # Randomly select a student ID for the foreign key
        student_id = random.choice(student_ids)

        amount = round(random.uniform(10, 7000), 2)  # Random payment amount between 10 and 1000
        payment_type = random.choice(payment_types)

        # Generate a random timestamp within a range (e.g., last 365 days)
        timestamp = datetime.now() - timedelta(days=random.randint(1, 365))

        # Create a payment record as a tuple and append to the payments data list
        payment_record = (payment_id, student_id, amount, payment_type, timestamp)
        # payment_record = (student_id, amount, payment_type, timestamp)
        payments_data.append(payment_record)

    return payments_data

def insert_payments(payments_data):
    conn = sqlite3.connect('stuaccts.db')
    cursor = conn.cursor()

    # Insert data into the 'payments' table
    for i in payments_data:
        cursor.execute('INSERT INTO payments VALUES (?,?,?,?,?)', i)
    conn.commit()
    conn.close()

def generate_charges_data(student_ids, students):
    charge_types = ['Board Designated Tuition', 'Administrative Fee', 'State Tuition', 'Housing', 'Dining', 'Student Fee', 'Refund']

    charges_data = []

    for _ in range(students):

        charge_id = None

        # Randomly select a student ID for the foreign key
        student_id = random.choice(student_ids)

        amount = round(random.uniform(10, 10000), 2)  # Random payment amount between 10 and 1000
        charge_type = random.choice(charge_types)

        # Generate a random timestamp within a range (e.g., last 365 days)
        timestamp = datetime.now() - timedelta(days=random.randint(1, 365))

        # Create a payment record as a tuple and append to the payments data list
        charge_record = (charge_id, student_id, amount, charge_type, timestamp)
        charges_data.append(charge_record)

    return charges_data

def insert_charges(charges_data):
    conn = sqlite3.connect('stuaccts.db')
    cursor = conn.cursor()

    # Insert data into the 'payments' table
    for i in charges_data:
        cursor.execute('INSERT INTO charges VALUES (?,?,?,?,?)', i)
    conn.commit()
    conn.close()

def generate_indicator_data(student_ids, students):
    indicator_types = ['Financial Aid','Active Payment Plan','Active Collections','Course Cancellation','Applied to Graduate']

    indicator_data = []

    for _ in range(students):

        indicator_id = None

        # Randomly select a student ID for the foreign key
        student_id = random.choice(student_ids)

        # amount = round(random.uniform(10, 2000), 2)  # Random payment amount between 10 and 1000
        indicator_type = random.choice(indicator_types)

        # Generate a random timestamp within a range (e.g., last 365 days)
        date_placed = datetime.now() - timedelta(days=random.randint(1, 365))

        # Create a payment record as a tuple and append to the payments data list
        indicator_record = (indicator_id, student_id, indicator_type, date_placed)
        indicator_data.append(indicator_record)

    return indicator_data

def insert_indicators(indicator_data):
    conn = sqlite3.connect('stuaccts.db')
    cursor = conn.cursor()

    # Insert data into the 'indicator' table
    for i in indicator_data:
        cursor.execute('INSERT INTO indicators VALUES (?,?,?,?)', i)
    conn.commit()
    conn.close()
