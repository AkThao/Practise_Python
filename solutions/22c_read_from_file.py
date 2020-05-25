import re


def count_each_category(input_categories):
    count_dict = {}

    for category in input_categories:
        if category not in count_dict:
            count_dict[category] = 1
        else:
            count_dict[category] += 1

    return count_dict


with open("imageslist.txt", "r") as read_file:
    images = read_file.read()

image_list = images.split("\n")
del image_list[-1]

image_categories = []
for image in image_list:
    # Do the first bit with regex just for practice
    prefix = re.findall("/.{1}/", image)
    image = image.replace(prefix[0], "")
    # Then do the last bit with simple split() method
    image = image.split("/")
    del image[-1]
    image_categories.append("/".join(image))

number_of_categories = count_each_category(image_categories)

for k, v in number_of_categories.items():
    print(f"There are {v} occurrences of the category {k}.")




#### Example solution ####
"""counter_dict = {}
with open('imageslist.txt') as f:
	line = f.readline()
	while line:
		line = line[3:-26]
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

for k, v in counter_dict.items():
    print(f"There are {v} occurrences of the category {k}.")"""