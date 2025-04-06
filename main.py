# Imports
from stats import num_words, num_recurrances, sort_list
import sys

# Get the file path
def main():
        if len(sys.argv) != 2:
                print ("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
        else:
                path_to_book = sys.argv[1]
                text = get_book_text(path_to_book)
                word_count = num_words(text)
                recurrances = num_recurrances(text, word_count)
                sorted_list = sort_list(recurrances)

                print ("============ BOOKBOT ============")
                print ("Analyzing book found at", path_to_book)
                print ("----------- Word Count ----------")
                print ("Found", word_count, "total words")
                print ("--------- Character Count -------")
                for item in sorted_list:
                        print(f'{item["character"]}: {item["count"]}')
                print ("============= END ===============")

# Get text of book
def get_book_text(path_to_book):
        with open(path_to_book) as f:
                book_contents = f.read()
        return book_contents


# printing the output
main()
