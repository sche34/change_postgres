# this file is used to test the connection to the database. 
# It is not used in the main code, but it is useful to check if the connection to the database is working properly.

import psycopg2
import dotenv
import os
import time

dotenv.load_dotenv()

# Connect to the database 
connection = psycopg2.connect(database=os.getenv("POSTGRES_DB"),
                            user=os.getenv("POSTGRES_USER"),
                            password=os.getenv("POSTGRES_PASSWORD"),
                            host=os.getenv("POSTGRES_HOST"),
                            port=5432)

cursor = connection.cursor()

sql_query ="""
select 
    *
from 
    test_table2
"""

# Fetch all rows from database
start_time = time.time()
cursor.execute(sql_query)
record = cursor.fetchall()

# Close the connection
connection.close()
cursor.close()

# Print the last row if the total number of rows is greater than 100, otherwise print all rows
if len(record) > 100:
    print(f"Last row out of total {len(record)} rows:- {record[-1]}")
else:
    print(f'All {len(record)} row(s): {record}')
print(f'Executed query in {time.time()-start_time:.0f} seconds')