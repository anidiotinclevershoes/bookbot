def main():
    book_path = "books/frankenstein.txt"
    text = count_every_letter(book_path)
    sort_and_display(book_path, count_every_letter(book_path))
    


def get_book_text(path):
    with open(path) as f:
        #reads the entire content of the file and returns it as a string
        return f.read()
    
def word_count(path):
    word_count = 0
    text = get_book_text(path)
    textlower = text.lower()
    words = textlower.split()
    for word in words:
        word_count += 1

    return word_count

def make_all_lower(string):
    return string.lower()

def sort_and_display(path, count):

    list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print("This is a report on all the letters within Frankenstein")
    print("-------------------------------------------------------")
    wrd_count = word_count(path)
    print(str(wrd_count) + " is the total word count")

    result = []
    for key, value in count.items():
        result.append({key:value})

    result.sort(reverse=True, key=lambda x: list(x.values())[0])
    
    for letter_dict in result:

            for key, value in letter_dict.items():
                if key not in list_of_letters:
                    pass
                else:
                    print(f"The {key} character was found {value} times")
    


def count_every_letter(path):

    book_as_string_upper = get_book_text(path)
    book_as_string = book_as_string_upper.lower()

    letter_counts = {}

    for letter in book_as_string:
        if letter == "":
            pass
        elif letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
        
    return letter_counts        



main()