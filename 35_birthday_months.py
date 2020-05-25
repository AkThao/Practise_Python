import json
import re
from collections import Counter


def get_json_data(file):
    with open(file, "r") as read_file:
        data = json.load(read_file)

    return data


def extract_months():
    bdays = get_json_data("birthdays.json")
    dates = list(bdays.values())
    months = []
    for date in dates:
        month = re.split("/", date)[1]
        months.append(month)

    return months


def convert_nums_to_months(months):
    month_names = ["January", "February", "March", "April",
                   "May", "June", "July", "August",
                   "September", "October", "November", "December"]
    for i in range(len(months)):
        months[i] = month_names[int(months[i]) - 1]

    return months


def write_counter_to_json(counter):
    with open("month_counter.json", "w") as write_file:
        json.dump(counter, write_file)


months = extract_months()
months = convert_nums_to_months(months)
c = Counter(months)
print(c)
write_counter_to_json(c)