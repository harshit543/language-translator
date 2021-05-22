from deep_translator import (GoogleTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             DeepL,
                             QCRI,
                             single_detection,
                             batch_detection)
import pyperclip

with open('./pass.txt', mode='r') as my_file:
    text = my_file.read()
    translated = GoogleTranslator(source ='auto', target='de').translate(text)
    print(translated)
    pyperclip.copy(translated)
    with open('./kirei.txt', mode='w') as my_file2:
        t = pyperclip.paste()
        my_file2.write(t)
