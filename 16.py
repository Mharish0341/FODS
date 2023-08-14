import pandas as pd
cr=pd.read_csv("customer reviews.csv")
df=cr["customer reviews"].value_counts()
print(df)