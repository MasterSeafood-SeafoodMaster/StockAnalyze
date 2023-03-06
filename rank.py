import pandas as pd
data = pd.read_csv('df.txt', sep=",", header=None)


data = data.sort_values(by=[5])
print(data)
data.to_csv("./ranked_df.txt", header=None, index=None, sep=',', mode='w')