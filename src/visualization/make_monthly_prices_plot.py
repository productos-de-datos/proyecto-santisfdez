def make_monthly_prices_plot():

    """ Función que crea una gráfica de los precios de electricidad promedio mensuales

    El archivo se guarda en la ruta data_lake/business/reports/figures/monthly_prices.png
    """

    import pandas as pd
    import matplotlib.pyplot as plt

    monthly_prices = pd.read_csv('data_lake/business/precios-mensuales.csv', index_col=None, header=0)
    monthly_prices.plot(kind='line')

    plt.plot(monthly_prices['Firstday'], monthly_prices['Precio'], 'b', label = 'monthly average')
    plt.title('Monthly average')
    plt.xlabel('Month')
    plt.ylabel('Price')
    plt.legend()
    plt.xticks(rotation = 'vertical')
    plt.savefig('data_lake/business/reports/figures/monthly_prices.png')
    
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":

    make_monthly_prices_plot()

    import doctest

    doctest.testmod()
