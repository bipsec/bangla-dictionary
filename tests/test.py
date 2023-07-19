import os
import pandas as pd


from bangla_dictionary.script.preprocess import rename_columns
from bangla_dictionary.script.write_pickle import write_to_pickle
from bangla_dictionary.script.read_pickle import get_dict
from bangla_dictionary import BanglaDictionary


# read the xlsx file and convert it to pickle data

def do():
    filename = os.path.join("../data/demo_data.xlsx")
    new_column_names = ["pageNo", "word", "spelling", "pronunciation", "meaning",
                    "pos", "IPA [B]", "language", "class", "sentence", "source"]

    dataframe = rename_columns(filename, new_column_names)

    df = pd.DataFrame(dataframe)

    # df.to_pickle("../data/dict_pkl")


def read_or_write_pickel():
    write_pickle = write_to_pickle()
    read_pickle = get_dict()
    print(read_pickle)


def testing():
    test = BanglaDictionary()
    meaning = test.get_multiple_root_lang("অই", "অক্ষিলোম", "অক্ষিপটল")
    print(meaning)

if __name__ == "__main__":
    do()
    # read_or_write_pickel()
    
    # for testing 
    # testing()