import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv("./prix_maisons.csv")

def show_data(dataframe):
    print(plt.figure(figsize=(15, 6)))
    print(plt.plot(dataframe["surface"], dataframe["prix"], "bo"))
    print(plt.show())


