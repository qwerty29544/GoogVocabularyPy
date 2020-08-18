import googletrans

translator = googletrans.Translator()
textesr= ["geography", "Plain", "text", "groggy main tank"]
for i in textesr:
    print(translator.translate(text=i, src='en', dest='ru'))
print(translator.detect("%@#!@#@$!@$!@$!@$"))