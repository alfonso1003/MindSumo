import csv
import datetime

"""
https://www.mindsumo.com/contests/credit-card-transactions

Write a script:

Using the transactions data attached below, write a script in Java, Python, C/C++, or JavaScript
that outputs a list of subscription IDs, their subscription type (daily, monthly, yearly, one-off),
and the duration of their subscription.

Bonus Questions (not required):

1. Give annual revenue numbers for all years between 1966 and 2014. Which years had the highest revenue growth,
and highest revenue loss?

2. Predict annual revenue for year 2015 (based on historical retention and new subscribers)

Id,Subscription ID,Amount (USD),Transaction Date
1235,15447,1900,01/01/1966
"""


def main():
    with open('./Files/subscription_report.csv', 'rb') as subscription_file:
        data = list(csv.reader(subscription_file))

    # create a dictionary with subscription id as key and the whole data row as a value
    dict = {}
    firstline = True
    for row in data:
        # skip first line (need to find a more elegant way to do this)
        if firstline == True:
            firstline = False
            continue

        subscription_id = row[1]
        if subscription_id not in dict:
            dict[subscription_id] = [row]
        else:
            dict[subscription_id].append(row)

    # iterate through dictionary grabbing relevant info
    output = []
    for key in dict:
        subscription_type = ''

        first_date_l = map(int, dict[key][0][3].split('/'))
        first_date = datetime.datetime(first_date_l[2], first_date_l[0], first_date_l[1])

        second_date = None

        last_date_l = map(int, dict[key][-1][3].split('/'))
        last_date = datetime.datetime(last_date_l[2], last_date_l[0], last_date_l[1])
        duration = (last_date - first_date).days

        if len(dict[key]) > 1:
            second_date_l = map(int, dict[key][1][3].split('/'))
            second_date = datetime.datetime(second_date_l[2], second_date_l[0], second_date_l[1])
            delta = (second_date - first_date).days

        if second_date == None:
            subscription_type = 'one-off'
        elif 0 < delta < 3:
            subscription_type = 'daily'
        elif 25 < delta < 35:
            subscription_type = 'monthly'
        elif 360 < delta < 370:
            subscription_type = 'yearly'
        else:
            subscription_type = 'other'

        output.append([key, subscription_type, duration])

    with open('./Files/subscription_summary.csv', 'wb') as output_file:
        a = csv.writer(output_file)
        a.writerow(['Subscription ID', 'Subscription Type', 'Duration (Days)'])
        a.writerows(output)


if __name__ == '__main__':
    main()