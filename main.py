import logging
import pickle

import pandas as pd

from article_parser import get_article

FIRST_ARTICLE_ID = 773234
ARTICLES_TO_COLLECT = 10000

BUCKET = "kekw"
PATH = "datasets/articles.pkl"
COLUMNS = ['id', 'title', 'text', 'time', 'hubs', 'tags']


_LOG = logging.getLogger()
_LOG.setLevel(logging.INFO)
_LOG.addHandler(logging.StreamHandler())



def save_results(df):
    with open(PATH, 'wb') as f:
        f.write(pickle.dumps(df))
    
    data = pickle.dumps(df)


def main():
    _LOG.info("Starting to collect data")

    data = pd.DataFrame(columns=COLUMNS)

    errors = 0
    successes = 0

    for i, article_id in enumerate(range(FIRST_ARTICLE_ID, FIRST_ARTICLE_ID - ARTICLES_TO_COLLECT, -1)):
        if i != 0 and i % 10 == 0:
            _LOG.info("Current stats: {} errors, {} successes".format(errors, successes))
            _LOG.info("Creating backup of results")
            save_results(data)
            _LOG.info("Results saved")

        cur_article = get_article(article_id)

        if cur_article:
            data.loc[data.shape[0]] = cur_article
            successes += 1
        else:
            errors += 1


if __name__ == "__main__":
    main()
