from keras.models import Sequential
from keras.layers import Dense, LSTM

from forecaster import __version__ as _version
from forecaster.config.core import TRAINED_MODEL_DIR

import typing as t
import joblib

class Model():
  def __init__(self, X_train, y_train, X_test, y_test, scaler):
    self.X_train, self.y_train, self.X_test, self.y_test = X_train, y_train, X_test, y_test
    self.scaler = scaler

  def fit(self):
    self.lstm={}
    for ticker in self.X_train.keys():
      self.lstm[ticker] = Sequential()
      self.lstm[ticker].add(LSTM(128, return_sequences=True, input_shape= (self.X_train[ticker].shape[1], 1)))
      self.lstm[ticker].add(LSTM(64, return_sequences=False))
      self.lstm[ticker].add(Dense(25))
      self.lstm[ticker].add(Dense(1))

      # Compile the model
      self.lstm[ticker].compile(optimizer='adam', loss='mean_squared_error')

      # Train the model
      self.lstm[ticker].fit(self.X_train[ticker], self.y_train[ticker], batch_size=1, epochs=1)

  def _risk(self):
    self.risk={}
    for ticker in self.X_test.keys():
      self.risk[ticker]=np.std((np.diff(self.X_test[ticker][:,:,0])/self.X_test[ticker][:,0:-1,0]), axis=1).mean()

  def predict(self):
    self.predictions={}
    self.label={}

    for ticker in self.X_test.keys():
      self.predictions[ticker] = self.lstm[ticker].predict(self.X_test[ticker])
      self.predictions[ticker] = self.scaler[ticker].inverse_transform(self.predictions[ticker])

    for ticker in self.y_test.keys():
      self.label[ticker] = self.scaler[ticker].inverse_transform(self.y_test[ticker].reshape(-1, 1))

    self._risk()

    return self.label, self.predictions, self.risk
  
def save_model(*, model_to_persist: Model) -> None:
    """Persist the model.
    Saves the versioned model, and overwrites any previous
    saved models. This ensures that when the package is
    published, there is only one trained model that can be
    called, and we know exactly how it was built.
    """

    # Prepare versioned save file name
    save_file_name = f"forecaster_output_v{_version}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    remove_old_models(files_to_keep=[save_file_name])
    joblib.dump(model_to_persist, save_path)

def load_model(*, file_name: str) -> Model:
    """Load a persisted pipeline."""

    file_path = TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model

def remove_old_models(*, files_to_keep: t.List[str]) -> None:
    """
    Remove old model.
    This is to ensure there is a simple one-to-one
    mapping between the package version and the model
    version to be imported and used by other applications.
    """
    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()