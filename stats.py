def get_num_words(p):
    with open(p) as b:
        string = b.read()
    string = len(string.split())
    print(f"Found {string} total words")

def get_num_chars(p):
    with open(p) as b:
        string = b.read()
    lowercase = string.lower()
    character_dictionary = {}
    for char in lowercase:
        if char not in character_dictionary:
            character_dictionary[char] = 0
            character_dictionary[char] += 1
        else:
            character_dictionary[char] += 1
    return character_dictionary 

def sorter(dict):
    the_list = []
    for letter, count in dict.items():    
        if letter.isalpha() == True:
            row = {"char": letter, "num": count}
            the_list.append(row)
        else:
            pass
    the_list.sort(reverse=True, key=sort_on)
    return the_list

def sort_on(items):
    return items["num"]
