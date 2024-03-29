from processing.data_manager import Extract
from processing.features import Transform, save_scalers
from processing.model import Model, save_model
from config.core import ticker_list

def run_training() -> None:
    """Train the model."""

    # read training data
    print("a")
    extract = Extract(ticker_list, years_bf=12)
    stocks_hist = extract.run()

    # divide X_train, y_train, X_test and y_test
    transform = Transform(stocks_hist, test_size=.05, X_days=60)
    X_train, y_train, X_test, y_test, scaler = transform.run()
    save_scalers(scaler)

    # fit model
    lstm = Model(X_train, y_train, X_test, y_test, scaler)
    lstm.fit()

    # persist trained model
    save_model(pipeline_to_persist=lstm)


if __name__ == "__main__":
    run_training()