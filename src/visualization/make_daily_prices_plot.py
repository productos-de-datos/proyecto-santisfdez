def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    import pandas as pd
    import matplotlib.pyplot as plt

    daily_prices = pd.read_csv('data_lake/business/precios-diarios.csv', index_col=None, header=0)
    daily_prices.plot(kind='line')

    plt.plot(daily_prices['Fecha'], daily_prices['Precio'], 'b', label = 'daily average')
    plt.title('Daily average')
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.legend()
    plt.xticks(rotation = 'vertical')
    plt.savefig('data_lake/business/reports/figures/daily_prices.png')
    
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":

    make_daily_prices_plot()

    import doctest

    doctest.testmod()
