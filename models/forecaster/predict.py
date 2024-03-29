from processing.data_manager import Extract
from processing.model import load_model
from processing.features import load_scalers
from forecaster import __version__ as _version
from sklearn.metrics import r2_score


def make_prediction(
        ticker_list,
) -> dict:
    """Make a prediction using a saved model pipeline."""
    
    extract = Extract(ticker_list, years_bf=12)
    stocks_hist = extract.run()

    lstm = load_model(f"forecaster_output_v{_version}.pkl")
    scaler = load_scalers(f"min_max_scaler{_version}.pkl")

    results={}

    label, predictions, risk = lstm.predict()

    r2={}

    for ticker in predictions.keys():
        r2[ticker] = r2_score(label[ticker], predictions[ticker])

    for ticker in ticker_list:
        data_s = scaler[ticker].transform(stocks_hist[ticker].tail(60).values.reshape(-1, 1))
        pred_s = lstm.lstm[ticker].predict(data_s.reshape(1,-1, 1))
        pred = scaler[ticker].inverse_transform(pred_s.reshape(-1, 1))
        results[ticker]["today"]=round(stocks_hist[ticker].iloc[-1])
        results[ticker]["tomorrow"]=round(pred[0][0])
        results[ticker]["price_change_perc"]=round(((pred[0][0]-stocks_hist[ticker].iloc[-1])/stocks_hist[ticker].iloc[-1])*100, 2)
        results[ticker]["risk"]=round(risk[ticker], 4)
        results[ticker]["r2"]=round(r2[ticker], 4)

    return results
