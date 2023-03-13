import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


df = pd.read_csv('assets/data.csv', index_col=0, encoding='latin')

print(df.to_string())

# sns.lmplot(x='Duration', y='Pulse', data=df)

