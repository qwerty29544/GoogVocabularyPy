import googletrans


def translate_word(*word, from_lang="en", to_lang="ru"):
    translator = googletrans.Translator()
    word_in_lang = []
    for single_word in word:
        word_translation = translator.translate(text=str(single_word), src=from_lang, dest=to_lang)
        word_in_lang.append(word_translation.text)
    return word_in_lang[0]


print(translate_word("today is your birthday"))
