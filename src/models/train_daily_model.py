def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import pickle
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.neural_network import MLPRegressor

    
    data = pd.read_csv('data_lake/business/features/precios_diarios.csv', index_col=None, header=0)



    df = data.copy()
    prices_history = df['Precio']
    


    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(np.array(prices_history).reshape(-1,1))
    data_scaled = [u[0] for u in data_scaled]


    P = 13
    X = []
    for t in range(P - 1, 9416 - 1):
        X.append([data_scaled[t - n] for n in range(P)])

    observed_scaled = data_scaled[P:]

    np.random.seed(123456)
    H = 10 

    mlp = MLPRegressor(
        hidden_layer_sizes=(H,),
        activation="logistic",
        learning_rate="adaptive",
        momentum=0.0,
        learning_rate_init=0.1,
        max_iter=10000,
    )

    mlp.fit(X[0:9043], observed_scaled[0:9043]) 

    pickle.dump(mlp, open('src/models/precios-diarios.pkl', 'wb'))

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    train_daily_model()
    import doctest

    doctest.testmod()
