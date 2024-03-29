import numpy as np
from sklearn.preprocessing import MinMaxScaler

<<<<<<< HEAD
from forecaster.config.core import FITTED_SCALERS_DIR
#from forecaster import __version__ as _version

import typing as t
import joblib

with open('/Users/bkoblinc/Desktop/Otros proyectos/stock-prices/stock-prices-forecaster/models/forecaster/VERSION', 'r') as archivo:
    _version = archivo.read().strip() 

=======
>>>>>>> ee7abfd (feat: data transformation)
class Transform():
  def __init__(self, data, test_size, X_days):
    self.data = data
    self.test_size = test_size
    self.X_days = X_days

  def _split_train_test(self):
    self.train={}
    self.test={}

    for ticker in self.data.keys():
      dataset = self.data[ticker].values
      training_data_len = int(np.ceil( len(dataset) * (1-self.test_size)))
      self.train[ticker] = dataset[:int(training_data_len)]
      self.test[ticker] = dataset[int(training_data_len):]

  def _scaler(self):
    self.scaler={}

    for ticker in self.data.keys():
      self.scaler[ticker] = MinMaxScaler(feature_range=(0,1))
      self.train[ticker] = self.scaler[ticker].fit_transform(self.train[ticker].reshape(-1, 1))
      self.test[ticker] = self.scaler[ticker].transform(self.test[ticker].reshape(-1, 1))

  def _split_X_y(self):

    self.X_train={}
    self.y_train={}
    self.X_test={}
    self.y_test={}

    for ticker in self.data.keys():
      self.X_train[ticker]=[]
      self.y_train[ticker]=[]

      for i in range(self.X_days, len(list(self.train.values())[0])):

        self.X_train[ticker].append(self.train[ticker][i-self.X_days:i, 0])
        self.y_train[ticker].append(self.train[ticker][i, 0])

      self.X_train[ticker], self.y_train[ticker] = np.array(self.X_train[ticker]), np.array(self.y_train[ticker])
      self.X_train[ticker] = np.reshape(self.X_train[ticker], (self.X_train[ticker].shape[0], self.X_train[ticker].shape[1], 1))

      self.X_test[ticker]=[]
      self.y_test[ticker]=[]

      for i in range(self.X_days, len(list(self.test.values())[0])):

        self.X_test[ticker].append(self.test[ticker][i-self.X_days:i, 0])
        self.y_test[ticker].append(self.test[ticker][i, 0])

      self.X_test[ticker], self.y_test[ticker] = np.array(self.X_test[ticker]), np.array(self.y_test[ticker])
      self.X_test[ticker] = np.reshape(self.X_test[ticker], (self.X_test[ticker].shape[0], self.X_test[ticker].shape[1], 1))

  def run(self):
    self._split_train_test()
    self._scaler()
    self._split_X_y()

<<<<<<< HEAD
    return self.X_train, self.y_train, self.X_test, self.y_test, self.scaler
  
def save_scalers(*, scalers_to_persist: dict) -> None:
    """Persist the scalers.
    Saves the versioned scalers, and overwrites any previous
    saved scalers. This ensures that when the package is
    published, there is only one fitted scaler that can be
    called, and we know exactly how it was built.
    """

    # Prepare versioned save file name
    save_file_name = f"min_max_scaler{_version}.pkl"
    save_path = FITTED_SCALERS_DIR / save_file_name

    remove_old_scalers(files_to_keep=[save_file_name])
    joblib.dump(scalers_to_persist, save_path)

def load_scalers(*, file_name: str) -> dict:
    """Load a persisted pipeline."""

    file_path = FITTED_SCALERS_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model

def remove_old_scalers(*, files_to_keep: t.List[str]) -> None:
    """
    Remove old model pipelines.
    This is to ensure there is a simple one-to-one
    mapping between the package version and the model
    version to be imported and used by other applications.
    """
    do_not_delete = files_to_keep + ["__init__.py"]
    for scalers_file in FITTED_SCALERS_DIR.iterdir():
        if scalers_file.name not in do_not_delete:
            scalers_file.unlink()
=======
    return self.X_train, self.y_train, self.X_test, self.y_test, self.scaler
>>>>>>> ee7abfd (feat: data transformation)
