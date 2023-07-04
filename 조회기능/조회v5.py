import cx_Oracle

# Establish a connection to the database
connection = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')

# Create a cursor object
cursor = connection.cursor()

# Execute a query to find the specific value
query = "SELECT * FROM LIBBOOK WHERE BOOKNAME = :%S"
value_to_find = "BOOKNAME[4]"
cursor.execute(query, value=value_to_find)

# Fetch the results
result = cursor.fetchone()

# Close the cursor and connection
cursor.close()
connection.close()

# Print the result
print(result)
