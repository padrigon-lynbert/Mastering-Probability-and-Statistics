import pandas as pd
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris.head())
print(iris.species.unique())