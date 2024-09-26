import psycopg2
import dotenv
import os

dotenv.load_dotenv()

database=os.getenv("POSTGRES_DB")
user=os.getenv("POSTGRES_USER")
password=os.getenv("POSTGRES_PASSWORD")
host=os.getenv("POSTGRES_HOST")

connection = psycopg2.connect(database=os.getenv("POSTGRES_DB"),
                            user=os.getenv("POSTGRES_USER"),
                            password=os.getenv("POSTGRES_PASSWORD"),
                            host=os.getenv("POSTGRES_HOST"),
                            port=5432)



cursor = connection.cursor()

sql_context ="""
select 
    *
from 
    test_table2
"""


cursor.execute(sql_context)

# Fetch all rows from database
record = cursor.fetchall()

connection.close()
cursor.close()

print("Last row from Database:- ", record[-1])