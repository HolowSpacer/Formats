import json
from pprint import pprint
from sort_voc import sort_news

def pop_news(doc):       #Создание словаря key = слова, value = их количество в тексте
    values = {}
    for descriptions in (doc['rss']['channel']['items']):
        for word in descriptions['description'].split():
            if len(word) > 6:
                if values.get(word.lower()):
                    values[word.lower()] += 1
                else:
                    values[word.lower()] = 1
    return values

with open("documents/newsafr.json", encoding= "utf-8") as f:
    data = json.load(f)
    pprint(sort_news(pop_news(data)))
