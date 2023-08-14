import pandas as pd
import numpy as np
arr=pd.read_csv("house_data.csv")
arr1=arr["sale price"]
price=np.array(arr1)
arr2=arr["bedrooms"]
bedrooms=np.array(arr2)
bhkmorethanfour=bedrooms>4
filteredsalesprice=price[bhkmorethanfour]
avg_sales_price=np.mean(filteredsalesprice)
print("the average sales price more than 4bhk",avg_sales_price)
