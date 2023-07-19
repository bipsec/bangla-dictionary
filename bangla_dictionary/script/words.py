import pandas as pd


def extract_word_to_txt(input_file, output_file, column_name):
    # Read the CSV file
    df = pd.read_excel(input_file)

    # Extract the desired column
    column_values = df[column_name]

    # Remove NaN values
    column_values = column_values.dropna()

    column_values = column_values.str.strip()

    # Save the values to a text file
    with open(output_file, 'w') as file:
        for value in column_values:
            file.write(str(value) + '\n')


# testing

input_file = "../../data/demo_data.xlsx"
output_file = "../tools/words.txt"
column_name = "word"

extract_word_to_txt(input_file, output_file, column_name)