import pandas

# student_data_frame = pandas.DataFrame(student_dict)

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_df)

# Loop through rows of a data frame
for (index, row) in nato_df.iterrows():
    pass

nato_dict = {row.code[0]: row.code for (index, row) in nato_df.iterrows()}
desired_word = input("Please enter the word that you'd like to Nato phonetics of: ")
desired_word = desired_word.upper()


result = [nato_dict[letter] for letter in desired_word if letter in nato_dict]

print(result)
