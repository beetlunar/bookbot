import sys
from stats import get_num_words 
from stats import get_num_chars
from stats import sorter
from stats import sort_on
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
num_chars = get_num_chars(sys.argv[1])
print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
get_num_words(sys.argv[1])
the_last = sorter(num_chars)
print("--------- Character Count -------")
for item in the_last:
    ch = item["char"]
    print(F"{ch}: {item['num']}")
print("============= END ===============")
