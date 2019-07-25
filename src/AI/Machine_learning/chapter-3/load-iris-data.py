import pandas as pd

df = pd.read_csv('data.csv', header=None,
                               # A
                               names=['sepal length', 'sepal width', #B
                                      'petal length', 'petal width', 'class'])
print(df.head())