import pickle
import pandas as pd
from lemmatize import lemmatize

with open('datasets/articles.pkl', 'rb') as file:
    data = pd.DataFrame(pickle.load(file))

try:
    with open('datasets/number_of_last_article_counted.txt', 'r') as file:
        CURRENT_ARTICLE_ID = int(file.read())
except:
    CURRENT_ARTICLE_ID = 1

try:
    with open('datasets/counts_of_words.txt', 'rb') as file:
            words = dict(pickle.load(file))
except:
    words = dict()
    

ID = CURRENT_ARTICLE_ID
for i, text in enumerate(data['text'][ID:]):
    if lemmatize(text):
        for word in lemmatize(text):
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        CURRENT_ARTICLE_ID += 1

    if i%1000 == 0:
        with open('datasets/number_of_last_article_counted.txt', 'w') as file:
            file.write(str(CURRENT_ARTICLE_ID))
        with open('datasets/counts_of_words.txt', 'wb') as file:
            file.write(pickle.dumps(words))
        print(words)
        input()