import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
def train_and_predict():
    overall_df_aggr=pd.read_csv('data/overall_df_aggr.csv')
    price_data=pd.Series(list(overall_df_aggr['price']),overall_df_aggr['date'])
    invoice_data=pd.Series(list(overall_df_aggr['invoice']),overall_df_aggr['date'])
    times_viewed_data=pd.Series(list(overall_df_aggr['times_viewed']),overall_df_aggr['date'])
    X_invoice=invoice_data.values
    X_times=times_viewed_data.values
    X_price=price_data.values
    model_revenue=ARIMA(X_invoice,order=(30,1,1))
    model_times_viewed=ARIMA(X_times,order=(30,1,1))
    model_price=ARIMA(X_price,order=(30,1,1))
    model_revenue_fitted=model_revenue.fit()
    model_times_viewed_fitted=model_times_viewed.fit()
    model_price_fitted=model_price.fit()
    y_pred_revenue=model_revenue_fitted.forecast(30)
    y_pred_times_viewed=model_times_viewed_fitted.forecast(30)
    y_pred_price=model_price_fitted.forecast(30)
    fig,axs=plt.subplots(3)
    axs[0].plot(y_pred_revenue)
    axs[0].set_title("Revenue")
    axs[1].plot(y_pred_times_viewed,color='red')
    axs[1].set_title('Times Viewed')
    axs[2].plot(y_pred_price,color='green')
    axs[2].set_title("Price")
    plt.savefig('static/graph.png')
