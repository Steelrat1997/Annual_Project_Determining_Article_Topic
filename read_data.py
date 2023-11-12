import pickle
import pandas as pd

with open('datasets/articles.pkl', 'rb') as file:
    data = pd.DataFrame(pickle.load(file))
print(data['time'])
print(data.dtypes)