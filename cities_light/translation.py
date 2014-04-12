from modeltranslation.translator import translator, TranslationOptions
from cities_light.models import City

class NewsTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(City, NewsTranslationOptions)