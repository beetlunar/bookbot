import sys
from stats import get_book_text, get_count_words, get_number_chac, sort_on, get_sorted_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    count = get_count_words(get_book_text(sys.argv[1]))
    chac_count = get_number_chac(get_book_text(sys.argv[1]))
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    new_dict = get_sorted_dict(get_number_chac(get_book_text(sys.argv[1])))
    for key in new_dict:
        value = key["num"]
        k = key["char"]
        if not k.isalpha():
            continue
        print(f"{k}: {value}")
    print("============= END ===============")
    print(sys.argv)
main()
