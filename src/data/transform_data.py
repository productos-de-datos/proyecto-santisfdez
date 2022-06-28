def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """

import pandas as pd
import xlwt

start = 1995
end = 2022
repo_path = 'data_lake/landing'
final_path = 'data_lake/raw/'

for year_to_download in range (start, end):
    try: 
        files = pd.read_excel(repo_path + '/' + str(year_to_download) + '.xlsx')
        files.to_csv(final_path + str(year_to_download) + '.csv', index=None, header=True)
    except:
        files = pd.read_excel(repo_path + '/' + str(year_to_download) + '.xls')
        files.to_csv(final_path + str(year_to_download) + '.csv', index=None, header=True)



#raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    transform_data()

    doctest.testmod()
