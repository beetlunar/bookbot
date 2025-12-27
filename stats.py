def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_count_words(string):
    new_list = string.split()
    num_words = len(new_list)
    return num_words

def get_number_chac(string):
    lowercase = string.lower()
    dict = {}
    for chac in lowercase:
        if chac not in dict:
            dict[chac] = 1
        else:
            dict[chac] += 1
    return dict
    
def get_sorted_dict(dictionary):
    list_of_dict = []
    for key in dictionary:
        value = dictionary[key]
        list_of_dict.append({"char":key, "num": value})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

def sort_on(items):
    return items["num"]
