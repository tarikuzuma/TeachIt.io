import os
import mysql.connector
import pandas as pd
from datetime import datetime, timedelta
from math import log
from math import sqrt
from jinja2 import Environment, FileSystemLoader


# Connect to the MySQL data_hot_tempbase
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8210909",
    port=3306,
    database="teachit"
)

# Create a cursor to interact with the data_hot_tempbase
mycursor = mydb.cursor()

# Execute the SQL query to select data_hot_temp from the "thread" table
mycursor.execute("SELECT * FROM thread")

# Fetch all the rows from the result set
result = mycursor.fetchall()


# Prepare the data_hot_temp for HTML conversion
data_hot_temp_printables= []
data_hot_temp = []

for row in result:
    formatted_date = row[4].strftime('%Y-%m-%d')
    formatted_year = row[4].strftime('%Y')

    total_votes = row[1] - row[2]

    # data_hot_temp to gather for printables
    row_data_hot_temp = {
        "sort_id": result.index(row) + 1,
        "total_votes": total_votes,
        "author": row[3],
        "date_upload": formatted_date,
        "post_title": row[5]
    }

    # data_hot_temp to gather for Hot algorithm
    row_data_hot_temp_hot = {
        "sort_id": result.index(row) + 1,
        "upvotes": row[1],
        "downvotes": row[2],
        "date_upload": formatted_date
    }

    data_hot_temp_printables.append(row_data_hot_temp)
    data_hot_temp.append(row_data_hot_temp_hot)


# Standard Epoch time is 1970-01-01 00:00:00
'''
    Function to calculate the number of seconds since the epoch
    Multiplied by 1000000 to convert to microseconds
'''
def epoch_seconds(date_string):
    date_format = "%Y-%m-%d"
    epoch = datetime.strptime("1970-01-01", date_format)
    given_date = datetime.strptime(date_string, date_format)
    delta = given_date - epoch
    return delta.days * 86400 + delta.seconds + delta.microseconds / 1e6

# Function to calcualte the score of a post
def score(upvotes, downvotes):
    return upvotes - downvotes

'''
    Function to calculate the Hotness Score of a post
'''
def hot(upvotes, downvotes, date):
    s = score(upvotes, downvotes)
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(sign * order + seconds / 45000, 7)

# Loop through the data_hot_temp and calculate the hotness score for each row
for data_hot_temp_item in data_hot_temp:
    print(data_hot_temp_item)
    # Check if "year" key exists and is a string
    data_hot_temp_item["hotness_score"] = hot(data_hot_temp_item["upvotes"], data_hot_temp_item["downvotes"], data_hot_temp_item["date_upload"])
    print(data_hot_temp_item["hotness_score"])


# Sort the data_hot_temp by the hotness score
hot_sorted = []
hot_sorted = sorted(data_hot_temp, key=lambda k: k['hotness_score'], reverse=True)
print (hot_sorted)

# data_hot_temp in row_data_hot_temp will be used for printables
data_hot_final_printables =[]

# Checks if both sort_ids are the same and if so, append the row of original printables.
for row in hot_sorted:
    for row2 in data_hot_temp_printables:
        if row["sort_id"] == row2["sort_id"]:
            print ("SAME ID FOR: ", row["sort_id"], row2["sort_id"])
            data_hot_final_printables.append(row2)

print ("Final data_hot_temp for data_hot_temp_final",data_hot_final_printables)

# Create a Pandas DataFrame from the data list
df = pd.DataFrame(data_hot_final_printables)

# Generate HTML from the DataFrame
html = df.to_html()

# Create a Jinja environment and load the template
env = Environment(loader=FileSystemLoader(os.path.dirname(os.path.abspath(__file__))))
template = env.get_template('template.jinja')

# Render the template with the data
rendered_html = template.render(data=data_hot_final_printables)
#print (rendered_html)


# Create a new file 'template_new.html' and write the rendered_html to that file
with open('src/python/template.html', 'w') as new_file:
    new_file.write(rendered_html)

# Close the cursor and connection
mycursor.close()
mydb.close()