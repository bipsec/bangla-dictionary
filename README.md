# BanglaDictionary

BanglaDictionary is a Python package that provides a dictionary for the Bengali (Bangla) language. It allows you to retrieve meanings, pronunciations, examples, parts of speech, types, and sources of words in the Bengali language.

## Installation

You can install the BanglaDictionary package using pip:

```python

```

- [File Structure](#file-structure)
  - [bangla_dictionary](#bangla_dictionary)
    - [script](#script)
      - [__init__.py](#__init__.py)
      - [bangla_dictionary.py](#bangla_dictionary.py)
      - [preprocess.py](#preprocess.py)
      - [read_pickle](#read_pickle)
      - [write_pickle](#write_pickle)
      - [words.py](#words.py)
    - [tools](#tools)
      - [words.txt](#words.txt)
    - [data](#data)
      - [demo_data.xlsx](#demo_data.xlsx)
      - [dict_pkl](#dict_pkl)
  - [tests](#tests)
    - [test.py](#test.py)
  - [README.md](#README.md)
  - [.gitignore](#gitignore)
  - [LICENSE](#LICENSE)
  - [setup.py](#setup.py)
  - 
## Usage

Here's an example of how to use the BanglaDictionary package:

```python
# Create an instance of the BanglaDictionary
from BanglaDictionary import BanglaDictionary
bd = BanglaDictionary()

# Get the meaning of a word
meaning = bd.get_meaning("অই")
print(meaning)  # Output: "পদ্যে ছন্দের নির্দেশক স্বরবর্ণ"

# Get the pronunciation of a word
pronunciation = bd.get_pronunciation("অংগুষ্ঠানা")
print(pronunciation)  # Output: "ওঙ্গুশঠানা"

# Get an example sentence for a word
example = bd.get_example("অকাজ")
print(example)  # Output: "সে হলো অকাজের কাজী।"

# Get the part of speech (POS) of a word
pos = bd.get_pos("অকাট্য")
print(pos)  # Output: "বিণ"

# Get the type of word
word_type = bd.get_type("অঋণ") 
print(word_type)  # Output: "অর্থ [অর্থনৈতিক]"

# Get the source of a word
source = bd.get_source("অকাণ্ড")
print(source)  # Output: "ব্যবহারিক বাংলা অভিধান" 

```



```python
# Get multiple meanings
meanings = bd.get_multiple_meanings("অংশভাগী", "অংশল", "অংশহারী")
print(meanings)  # Output: {"অংশভাগী": "অংশ পাওয়ার যোগ্য", "অংশল": "বলবান", "অংশহারী": "অংশলোপ"}

# Get multiple pronunciations
pronunciations = bd.get_multiple_pronunciations("অংশহারী", "অংশাংশ", "অংশানো")
print(pronunciations)  # Output: {"অংশহারী": "অঙ্‌শোহর", "অংশাংশ": "অঙ্‌শাঙ্‌শো", "অংশানো": "অঙ্‌শানো"}

# Get multiple examples
examples = bd.get_multiple_examples("অকল্যান", "অকষ্টবদ্ধ", "অকস্মাৎ")
print(examples)  # Output: {"অকল্যান": "অকল্যান এই সুর।", "অকষ্টবদ্ধ": "সাধু বাংলার বাক্য গঠন পদ্ধতি অকষ্টবদ্ধ।", "অকস্মাৎ": "ছেড়েছি সব অকস্মাতের আশা।"}

# Get multiple parts of speech (POS)
pos_list = bd.get_multiple_pos("অকল্যাণকর", "অকল্মষ", "অকস্মাৎ")
print(pos_list)  # Output: {"অকল্যাণকর": "বিণ", "অকল্মষ": "বিণ", "অকস্মাৎ": "ক্রিবিন"}

# Get multiple types
types = bd.get_multiple_types("অকরোটি ", "অঋণী", "অইরান")
print(types)  # Output: {"অকরোটি ": "প্রাণি [প্রাণিবিজ্ঞান]", "অঋণী": "অর্থ [অর্থনৈতিক]", "অইরান": "ফা. [ফারসি]"}

# Get multiple sources
sources = bd.get_multiple_sources("অকরোটি", "অঋণী", "অইরান")
print(sources)  # Output: {"অকরোটি": "ব্যবহারিক বাংলা অভিধান", "অঋণী": "ব্যবহারিক বাংলা অভিধান", "অইরান": "ব্যবহারিক বাংলা অভিধান"}
```


## Data Source

The data used by the BanglaDictionary package is sourced from Bangla Dictionary: Bangla Academy- ব্যবহারিক বাংলা অভিধান . The dictionary provides meanings, pronunciations, examples, parts of speech, types, and sources for a wide range of Bengali words.

## Contributing
If you find any issues or would like to contribute to the BanglaDictionary package, please feel free to open an issue or submit a pull request on the GitHub repository. You can contact via email: [bip.sec22@gmail.com](#bip.sec22@gmail.com) , [afrarjahin@gmail.com](#afrarjahin@gmail.com)


## License
The BanglaDictionary package is released under the MIT License. You are free to use, modify, and distribute this package in your own projects.
