import xml.etree.ElementTree as ET
from pprint import pprint
from sort_voc import sort_news

def pop_news(doc):        #Создание словаря key = слова, value = их количество в тексте
    values = {}
    for item in doc:
        for word in item.text.split():
            if len(word) > 6:
                if values.get(word.lower()):
                    values[word.lower()] += 1
                else:
                    values[word.lower()] = 1
    return values

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("documents/newsafr.xml", parser)
root = tree.getroot()
xml_items = root.findall('channel/item/description')
pprint(sort_news(pop_news(xml_items)))