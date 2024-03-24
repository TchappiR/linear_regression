import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv("./prix_maisons.csv")

print(plt.figure(figsize=(15, 6)))
print(plt.plot(data_df["surface"], data_df["prix"], "bo"))
print(plt.show())


