#!/usr/bin/python3
''' Task 0 '''
import sys
import MySQLdb

# take args from the promp
arg = sys.argv
DB_HOST = 'localhost'
DB_USER = arg[1]
DB_PASS = arg[2]
DB_NAME = arg[3]
data = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

# connect to db
conn = MySQLdb.connect(*data)

#create cursor
cursor = conn.cursor()

# exe query
query = 'SELECT * FROM states ORDER BY id ASC'
cursor.execute(query)

# Fetch the results of a select
res = cursor.fetchall() 

# print response
for i in res:
    print(i)




