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

create_query ="""create table if not exists test_table2 (id serial primary key, name varchar(50), age int)"""
select_query ="""select * from test_table2"""
drop_query ="""drop table test_table2"""

# Create a table, insert some data, and then drop the table
start_time = time.time()
cursor.execute(create_query)
connection.commit()
cursor.execute(select_query)
record = cursor.fetchall()
if len(record) == 0:    
    cursor.execute(drop_query)
    connection.commit()	

# Close the connection
connection.close()
cursor.close()

# Print the last row if the total number of rows is greater than 100, otherwise print all rows
if len(record) > 100:
    print(f"Last row out of total {len(record)} rows:- {record[-1]}")
else:
    print(f'All {len(record)} row(s): {record}')
print(f'Executed query in {time.time()-start_time:.0f} seconds')