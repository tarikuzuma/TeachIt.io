from datetime import datetime

def epoch_seconds(date_string):
    date_format = "%Y-%m-%d"
    epoch = datetime.strptime("1970-01-01", date_format)
    given_date = datetime.strptime(date_string, date_format)
    delta = given_date - epoch
    return delta.days * 86400 + delta.seconds + (float(delta.microseconds) / 1000000)

date_string = "2024-06-04"
result = epoch_seconds(date_string)
print(result)
