from googletrans import Translator
from googletrans import LANGUAGES
translator = Translator()


titile = "Music’s Impact and Influence on Everyday Life"
text = "As a person who loves music and even got into playing an instrument myself, it does have an influence on my everyday life. I’m constantly listening to music whether it be while working during class, in the car on my way home, or just while practicing playing the guitar. Music is all around the world and one of the most popular forms of entertainment and escape. It consists of many different styles and opinions, whether it be just personal opinion or even a part of your culture."
author = "Bryleigh Conley, Reporter"
date = "April 12, 2023"

article = f"""
{titile}
{author}
{date}
{text}
"""


print(LANGUAGES)
language = input("Выберите язык на который хотите перевести статью: ")

translated_article = translator.translate(src='en', dest=language, text=article)

print(translated_article.text)