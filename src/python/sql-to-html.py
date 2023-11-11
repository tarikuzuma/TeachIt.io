import os
import mysql.connector
import pandas as pd

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="8210909",
  port=3306,
  database="teachit"
)

# Create a cursor to interact with the database
mycursor = mydb.cursor()

# Execute the SQL query to select data from the "thread" table
mycursor.execute("SELECT * FROM thread")

# Fetch all the rows from the result set
result = mycursor.fetchall()

# BRUTE FORCEFULYL sorts the result by the highest number of Upvotes hence "Top Posts"
# Which is why we used to .sort of python since it is the most basic sorting method.
# Reversed in order to sort from highest to lowest
result.sort(key=lambda row: row[1], reverse=True)

# Prepare the data for HTML conversion
data = []

for row in result:
    
    # Convert the date to a formatted string so that it doesnt display datetime.date in the HTML
    formatted_date = row[4].strftime('%Y-%m-%d')

    # Convert the row to a dictionary
    row_data = {
        "rate": row[0],
        "upvote": row[1],
        "downvote": row[2],
        "author": row[3],
        "date_upload": formatted_date,
        "post_title": row[5]
    }

    # Append the row data to the list
    data.append(row_data)

    # Prints data in rows
    print(row[0], row[1], row[2], row[3], formatted_date, row[5])


# Create a Pandas DataFrame from the data list
df = pd.DataFrame(data)

# Generate HTML from the DataFrame
html = df.to_html()

html_with_title = "<h1>TEST</h1>\n" + html

# Save the HTML to a file named "test.html"
with open('src/python/test.html', 'w') as f:
  f.write(html_with_title)

# Close the cursor and connection
mycursor.close()
mydb.close()