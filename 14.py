import pandas as pd
data=pd.read_csv("price of sold product.csv")
df=data["age"].value_counts()
print(df)
