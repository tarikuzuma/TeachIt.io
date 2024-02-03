import os
import mysql.connector
import flask

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="teachit"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM thread")

result = mycursor.fetchall()

result.sort(key=lambda row: row[2], reverse=True)

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

# Redner Flask

app = flask.Flask(__name__)

@app.route("/")

def home():
    return flask.render_template("template_origin.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)