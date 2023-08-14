import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
df=pd.read_csv("age fat.csv")
mean_value=df["age"].mean()
mean_value1=df["%fat"].mean()
median_value=df["age"].median()
median_value1=df["%fat"].median()
sd=df["age"].std()
sd1=df["%fat"].std()
print("mean of age",mean_value,"mean of %fat",mean_value1,"median of age",median_value,"median of %fat",median_value1,"standard deviation of age",sd,"standard deviation of %fat",sd1)
plt.boxplot(df["age"])
plt.show()
plt.boxplot(df["%fat"])
plt.show()
plt.scatter(df["age"],df["%fat"])
plt.show()
stats.probplot(df["age"],plot=plt)
plt.show()