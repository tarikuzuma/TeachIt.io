from datetime import datetime, timedelta
from math import log
from math import sqrt

# Standard Epoch time
epoch = datetime(1970, 1, 1)
'''
    Function to calculate the number of seconds since the epoch
    Multiplied by 1000000 to convert to microseconds
'''
def epoch_seconds(date):
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)

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

def _confidence(upvotes, downvotes):
    n = upvotes + downvotes

    if n == 0:
        return 0

    z = 1.281551565545
    p = float(upvotes) / n

    left = p + 1/(2*n)*z*z
    right = z*sqrt(p*(1-p)/n + z*z/(4*n*n))
    under = 1+1/n*z*z

    return (left - right) / under

def confidence(upvotes, downvotes):
    if upvotes + downvotes == 0:
        return 0
    else:
        return _confidence(upvotes, downvotes)

# Example usage
upvotes = 100
downvotes = 20
post_date = datetime(2021, 1, 1)  # Replace this with the actual posting date
print(f"Confidence Score: {confidence(upvotes, downvotes)}")

# Calculate hotness score using the provided function
hotness_score = hot(upvotes, downvotes, post_date)

# Display the result
print(f"Hotness Score: {hotness_score}")
