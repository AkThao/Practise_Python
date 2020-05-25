import requests
from bs4 import BeautifulSoup
import json


def download_bday_data():
    """Create a cache of the online birthday data, to avoid making many requests to website"""
    url = "http://www.bonestamp.com/sgt/famous_bdays.htm"
    r = requests.get(url)
    html = r.text

    with open("birthdays.txt", "w") as write_file:
        write_file.write(html)


def format_names(names_list):
    for i in range(len(names_list)):
        # Clean up text
        names_list[i] = names_list[i].strip().replace(",", "").split()

    # Flatten the list, so all names and dates are contiguous
    names_list_flat = [element for sublist in names_list for element in sublist]

    individual_names_list = []
    temp_list = []

    # Loop through all tokens and separate people by year
    for i in range(len(names_list_flat)):
        try:
            names_list_flat[i] = int(names_list_flat[i])
            temp_list.append(str(names_list_flat[i]))
            individual_names_list.append(temp_list)
            temp_list = []
        except ValueError:
            temp_list.append(names_list_flat[i])

    return individual_names_list


def get_birthyears():
    with open("birthdays.txt", "r") as read_file:
        html = read_file.read()

    soup = BeautifulSoup(html, "html.parser")
    birthdays = soup.findAll(class_="MsoNormal")
    for i in range(len(birthdays)):
        birthdays[i] = birthdays[i].text

    # We are only interested in years, so remove the text blocks with days and months
    birthdays = [bd for bd in birthdays if len(bd) > 2 and bd != "January"]

    # First two text blocks contain stuff from the webpage's headers, so we don't need them
    birthdays = birthdays[2:]

    # Convert the pile of name and year data into a list of lists containing the person's name and birthyear
    individual_birthdays = format_names(birthdays)

    for i in range(len(individual_birthdays)):
        # Join the names and years together into a nice readable string
        individual_birthdays[i] = " ".join(individual_birthdays[i][:-1]) + " – " + individual_birthdays[i][-1]

    return individual_birthdays


def get_full_birthdays():
    with open("birthdays.txt", "r") as read_file:
        html = read_file.read()

    soup = BeautifulSoup(html, "html.parser")
    months = soup.findAll("table")
    months = months[4:16] # The extra elements are nonsense

    bdays_by_mon = [] # Each element will contain all the people and their DOBs in the respective month
    for i in range(len(months)):
        temp_list = [] # This list will temporarily hold each month's data and will be used 12 times
        current_month = months[i].find_all("tr") # All the rows of birthday data in the month
        # Now separate current_month into the data for each day
        for i in range(len(current_month)): # Loop through the rows
            day = current_month[i].find_all("td") # Data in each row
            temp_list.append([day[0].text.strip().replace(",", ""), day[1].text.strip().replace(",", "")])
        bdays_by_mon.append(temp_list)

    # Now process the data for each day in each month and separate the names that are grouped by day
    for i in range(len(bdays_by_mon)):
        for j in range(len(bdays_by_mon[i])):
            formatted_names = format_names([bdays_by_mon[i][j][1]])
            bdays_by_mon[i][j][1] = formatted_names

    # A bit more formatting and tidying up
    all_bdays = []
    for i in range(len(bdays_by_mon)):
        for j in range(len(bdays_by_mon[i])):
            for k in range(len(bdays_by_mon[i][j][1])):
                bday = f"{' '.join(bdays_by_mon[i][j][1][k][:-1])} – "\
                f"{bdays_by_mon[i][j][0]}/{str(i+1)}/{bdays_by_mon[i][j][1][k][-1]}" # SO MUCH NESTING!!!!!!!!
                all_bdays.append(bday)

    return all_bdays


def convert_bday_list_to_dict(bday_list):
    bday_dict = {}
    for bday in bday_list:
        name_and_date = bday.split(" – ")
        bday_dict[name_and_date[0]] = name_and_date[1]

    return bday_dict


def save_bdays_to_json(birthdays):
    with open("birthdays.json", "w") as write_file:
        json.dump(birthdays, write_file)


#download_bday_data()
scientist_birthyears = get_birthyears()
scientist_birthdays = get_full_birthdays()
birthday_dict = convert_bday_list_to_dict(scientist_birthdays)
save_bdays_to_json(birthday_dict)