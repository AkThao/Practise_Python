with open("nameslist.txt", "r") as read_file:
    names = read_file.read()

name_list = names.split("\n")

def count_each_name(input_names):
    count_dict = {}

    for name in input_names:
        if name not in count_dict:
            count_dict[name] = 1
        else:
            count_dict[name] += 1

    return count_dict


number_of_names = count_each_name(name_list)

for k, v in number_of_names.items():
    print(f"There are {v} occurrences of the name {k}.")