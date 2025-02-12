import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t')

# print(df.head())

df = pd.read_csv('https://raw.githubusercontent.com/ashokveda/books/main/nba.csv')

# print(df.head())
# print()

# print(df.groupby('Team').count())
# print()

# print(df.groupby('Team').Age.mean())

# print(df.groupby(['Team','Position']).first())

# print(df.sort_values('Age', ascending=False))


pf = pd.read_csv('https://raw.githubusercontent.com/ashokveda/books/main/titanic.csv')

print(pf.isnull().sum())





















