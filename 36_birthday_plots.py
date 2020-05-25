from bokeh.plotting import figure, show, output_file
import json


def get_json_data(file):
    with open(file, "r") as read_file:
        data = json.load(read_file)

    return data


def make_plot(x, y):
    p = figure(x_range=x)
    p.vbar(x=x, top=y, width=0.25)
    p.xaxis.major_label_orientation = 1

    show(p)


bday_months = get_json_data("month_counter.json")

# Specify an HTML file where the output will go
output_file("birthday_months_plot.html")

# Load the x and y data
months = list(bday_months.keys())
counts = list(bday_months.values())
x_categories = months
x = x_categories
y = counts

make_plot(x, y)