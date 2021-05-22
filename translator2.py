from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open('./kkk.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except :
    print("sorry my bad")
