import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}  # iterating over rows of the DataFrame


def generate_phonetic():
    try:
        user_name = input("Enter your name: ").upper()
        words_list = [nato_dict[letter] for letter in user_name]  # using list comprehension
        print("Your name's spelling: ")
        print(words_list)
    except KeyError:  # handling the exception when user inputs anything except the letters
        print("Sorry, but you must use letters only.")
        generate_phonetic()


generate_phonetic()