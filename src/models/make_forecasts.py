def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


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
    for t in range(P - 1, 9417 - 1):
        X.append([data_scaled[t - n] for n in range(P)])

    observed_scaled = data_scaled[P:]

    pickle_model = pickle.load(open('src/models/precios-diarios.pkl', 'rb'))
    y_scaled_m1 = pickle_model.predict(X)

    y_m1 = scaler.inverse_transform([[u] for u in y_scaled_m1])
    y_m1 = [u[0] for u in y_m1]

    lista = []
    for i in range(0, 13):
        t = 0
        lista.append(t)

    forecasting = lista + y_m1
    data['pronóstico'] = forecasting
    
    data.to_csv('data_lake/business/forecasts/precios-diarios.csv', index=False)
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    make_forecasts()
    import doctest

    doctest.testmod()
