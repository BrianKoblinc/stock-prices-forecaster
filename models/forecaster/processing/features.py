import numpy as np
from sklearn.preprocessing import MinMaxScaler

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

    return self.X_train, self.y_train, self.X_test, self.y_test, self.scaler