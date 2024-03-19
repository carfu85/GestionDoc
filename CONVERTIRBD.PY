import csv
import sqlite3

# Path to the CSV file
csv_file = '/path/to/your/report.csv'

# Path to the SQLite database file
db_file = '/path/to/your/database.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create a table in the database
cursor.execute('''CREATE TABLE IF NOT EXISTS report (
                    column1 TEXT,
                    column2 INTEGER,
                    column3 REAL
                )''')

# Read the CSV file and insert data into the database
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        cursor.execute('INSERT INTO report VALUES (?, ?, ?)', row)

# Commit the changes and close the connection
conn.commit()
conn.close()

print('CSV report converted to SQLite database successfully!')