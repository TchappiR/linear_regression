import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv("./prix_maisons.csv")
plt.figure(figsize=(15, 6))
plt.plot(df["surface"], df["prix"], "bo")
print(plt.show())


