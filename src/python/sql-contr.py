import os
import mysql.connector
import pandas as pd
from jinja2 import Environment, FileSystemLoader

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

# BRUTE FORCEFULLY sorts the result by the highest number of upvotes hence "Top"
result.sort(key=lambda row: row[2], reverse=True)

# Prepare the data for HTML conversion
data = []

for row in result:
    formatted_date = row[4].strftime('%Y-%m-%d')

    total_votes = row[1] - row[2]

    row_data = {
        "total_votes": total_votes,
        "author": row[3],
        "date_upload": formatted_date,
        "post_title": row[5]
    }
    data.append(row_data)
    print("Supposide Printables: ", row[0], row[1], row[2], total_votes, row[3], formatted_date, row[5])
    print("Actual Files: ", row_data)

# Create a Pandas DataFrame from the data list
df = pd.DataFrame(data)

# Generate HTML from the DataFrame
html = df.to_html()

# Create a Jinja environment and load the template
env = Environment(loader=FileSystemLoader(os.path.dirname(os.path.abspath(__file__))))
template = env.get_template('template.jinja')

# Render the template with the data
rendered_html = template.render(data=data)
#print (rendered_html)


# Create a new file 'template_new.html' and write the rendered_html to that file
with open('src/python/template.html', 'w') as new_file:
    new_file.write(rendered_html)

# Close the cursor and connection
mycursor.close()
mydb.close()