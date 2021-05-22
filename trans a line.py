from googletrans import Translator, LANGUAGES

sample_text = 'I love you.'

for language in LANGUAGES:
    t = Translator().translate(sample_text, dest = 'ja')
    print(t)

 
