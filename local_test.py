import psycopg2
import dotenv
import os
import time

dotenv.load_dotenv()

database=os.getenv("POSTGRES_DB")
user=os.getenv("POSTGRES_USER")
password=os.getenv("POSTGRES_PASSWORD")
host=os.getenv("POSTGRES_HOST")

connection = psycopg2.connect(database=database,
                            user=user,
                            password=password,
                            host=host,
                            port=5432)

cursor = connection.cursor()

sql_context ="""
select 
    *
from 
    test_table2
"""
start_time = time.time()
cursor.execute(sql_context)

# Fetch all rows from database
record = cursor.fetchall()

connection.close()
cursor.close()

if len(record) > 100:
    print(f"Last row out of total {len(record)} rows:- {record[-1]}")
else:
    print(f'All {len(record)} row(s): {record}')
print(f'Executed query in {time.time()-start_time:.0f} seconds')