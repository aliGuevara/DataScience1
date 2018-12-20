import csv #lib to csv format
import numpy as np #lib numpy for math
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = [] #dates from document finance
prices = []  #prices for document finance

def get_data(filename):
    with open(filename,'r') as csvfile:
        csvFileReader =csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[2]))
            prices.append(float(row[1]))

    return

def predict_prices(dates,prices,x):
    dates = np.reshape(dates,(len(dates),1))

    svr_lin=SVR(kernel='linear',C=1e3)
    svr_poly=SVR(kernel='poly',C=1e3,degree=2)
    svr_rbf=SVR(kernel='rbf',C=1e3,gamma=0.1)
    svr_lin.fit(dates,prices)
    svr_poly.fit(dates,prices)
    svr_rbf.fit(dates,prices)

    plt.scatter(dates,prices,color='black',label='Data')
    plt.plot(dates,svr_rbf.predict(dates),color='red',label='RBF model')
    plt.plot(dates,svr_lin.predict(dates),color='green',label='Linear model')
    plt.plot(dates,svr_poly.predict(dates),color='blue',label='Poly model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Suport vector regresion')
    plt.legend()


    return svr_rbf.predict(x)[0],svr_lin.predict(x)[0],svr_poly.predict(x)[0]

get_data('AMZN1.csv')

predict_price=predict_prices(dates,prices,23)
plt.scatter(23,predict_price[0],color='black',label='Data')
plt.show()
print(predict_price)
