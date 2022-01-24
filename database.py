import psycopg2
 
conn = psycopg2.connect(host="localhost",database="mydb", user="postgres", password="postgres")
 
if conn is not None:
    print('Connection established to PostgreSQL.')
else:
