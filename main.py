import pandas

# student_data_frame = pandas.DataFrame(student_dict)

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_df)

# Loop through rows of a data frame
for (index, row) in nato_df.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass
    # print(row.code)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# TO DO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.code[0]: row.code for (index, row) in nato_df.iterrows()}
# print(nato_dict)
# TO DO 2. Create a list of the phonetic code words from a word that the user inputs.
desired_word = input("Please enter the word that you'd like to Nato phonetics of: ")
desired_word = desired_word.upper()
# print(desired_word)
# print(nato_dict)

result = [nato_dict[letter] for letter in desired_word if letter in nato_dict]

print(result)