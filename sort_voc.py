def sort_news(news):      #Сортировка словаря и создание списка топ-10
    list_dict_words = list(news.items())
    sort_dict_list_words = sorted(list_dict_words, key=lambda i: i[1], reverse=True)
    top_words = []
    for i in range(10):
        top_words.append(sort_dict_list_words[i])
    return top_words