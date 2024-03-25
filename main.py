import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def show_data(dataframe):
    print(plt.figure(figsize=(15, 6)))
    print(plt.plot(dataframe["surface"], dataframe["prix"], "bo"))
    print(plt.show())

def prepare_data(dataframe):
	split_index = int(len(dataframe) * 0.75)
	train_dataframe = dataframe.iloc[ : split_index]
	test_dataframe = dataframe.iloc[split_index : ]

	x_train = train_dataframe[ ["surface"] ]
	y_train = train_dataframe[ ["prix"] ]

	x_test = test_dataframe[ ["surface"] ]
	y_test = test_dataframe[ ["prix"] ]

	return x_train, y_train, x_test, y_test

def regression(x_train, y_train):
    model = LinearRegression()
    model.fit(x_train, y_train)
    return model

def test_model(model, x_test, y_test):
    y_test_predicted = model.predict(x_test)
     
    rmse = np.sqrt(1/len(x_test) * sum((y_test.values - y_test_predicted)**2))
    print(rmse)

    plt.figure(figsize=(15, 6))
    plt.plot(x_test, y_test, "bo")
    plt.plot(x_test, y_test_predicted, "ro")
    plt.show()

data_df = pd.read_csv("./prix_maisons.csv")
#show_data(dataframe=data_df)
x_train, y_train, x_test, y_test = prepare_data(dataframe=data_df)
model = regression(x_train, y_train)
test_model(model, x_test, y_test)