from googletrans import Translator


def translate_bengali_to_english(bengali_words):
    """
        One day I will make this translator, till then use Google Translator - (Chapa)
    Params:
        - input one bengali word - translator er jodi common pore translate kore dibe.
        - don't keep any hope, it translates bal sal.
    Returns:
        - shit...
    """
    translator = Translator()
    translations = {}

    for word in bengali_words:
        translated = translator.translate(word, src='bn', dest='en')
        translations[word] = translated.text

    return translations

# Example Usage

# res = {
#     "custom_output": "This is a basic translator.",
#     "google_translator_message": "Using Google Translator",
#     "other_data": translate_bengali_to_english(["অই", "অক্ষিলোম", "অক্ষিপটল", "অংশ"])
# }
# response = json.dumps(res, ensure_ascii=False, indent=4)
# print(response)

