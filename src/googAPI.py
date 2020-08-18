import googletrans

# Функция перевода слова или списка слов при помощи googletrans
# Принимает на вход произвольную последовательность строк, а также языки с которого и на который переводить
# на выходе имеются в зависимости от входного количества строк соответствующие строки, переведенные
def translate_word(*word, from_lang="en", to_lang="ru"):
    # @TODO: придумать реализацию без списка чтобы не было костылей с освобождением
    # @TODO: протестировать функцию на множестве крайних случаев
    translator = googletrans.Translator()   # объявляем экземпляр переводчика
    word_in_lang = []                       # объявляем результрующий список строк
    for single_word in word:                # цикл по всем входным строкам
        # присваиваем вывод перевода при помощи функции translate
        word_translation = translator.translate(text=str(single_word), src=from_lang, dest=to_lang)
        word_in_lang.append(word_translation.text)      # встроенный парсинг вывода переводчика
    return word_in_lang[0]                  # освобождаемся от списка


#print(translate_word("today is your birthday"))
