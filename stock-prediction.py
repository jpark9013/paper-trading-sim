import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import torch
import torch.nn as nn
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler


class GRU(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers, output_dim):
        super(GRU, self).__init__()
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
                
        self.gru = nn.GRU(input_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).requires_grad_()
        out, (hn) = self.gru(x, (h0.detach()))
        out = self.fc(out[:, -1, :]) 
        return out


class ModelAccessor:
    
    def runPredictions(filepath, length, lookback):
        scaler = MinMaxScaler(feature_range=(-1, 1))
        input_dim = 1
        hidden_dim = 32
        num_layers = 2
        output_dim = 1
    
        def readData(filePath):
            data = pd.read_csv(filePath)
            data = data.sort_values('Date')
            price = data[['Close']]
            scaler = MinMaxScaler(feature_range=(-1, 1))
            price['Close'] = scaler.fit_transform(price['Close'].values.reshape(-1,1))

            return price
    
        def make_prediction(x_test, model, size):
            X=x_test[-1:,...,...]
            with torch.no_grad():
                predictions = []
                model.eval()
                for _ in range(size):
                    yhat = model(X)
                    X=torch.roll(X, shifts=-1, dims=1)
                    X[0,-1,0]=yhat
                    predictions.append(yhat.item())
            return torch.tensor(predictions).reshape(-1, 1)
        
        def split_data(stock, lookback): # will need to be modified to fit project
            data_raw = stock.to_numpy() # convert to numpy array
            data = []
        
            #  create all possible sequences of length seq_len
            for index in range(len(data_raw) - lookback): 
                data.append(data_raw[index: index + lookback])

            data = np.array(data)
            test_set_size = data.shape[0]
            x_test = data[:test_set_size,:-1]
            y_test = data[:test_set_size,-1,:]

            return [x_test, y_test]
        
        price = readData(filepath)
        x_test, y_test = split_data(price, lookback)
        print('x_test.shape = ',x_test.shape)
        print('y_test.shape = ',y_test.shape)

        x_test = torch.from_numpy(x_test).type(torch.Tensor)

        model = GRU(input_dim=input_dim, hidden_dim=hidden_dim, output_dim=output_dim, num_layers=num_layers)

        # THE MODEL HAS BEEN LOADED
        model = torch.load('sussy.model')
        model.eval()

        # make predictions
        y_test_pred = make_prediction(x_test,model,length)

        # invert predictions
        y_test_pred = scaler.inverse_transform(y_test_pred.detach().numpy())

        return y_test_pred
