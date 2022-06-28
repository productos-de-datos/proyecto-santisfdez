def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
import pandas as pd
import glob
import os
#final_path = 'data_lake/cleansed'
os.chdir('data_lake/raw')
file_extension = '.csv'
file_names = [ i for i in glob.glob(f"*{file_extension}")]
correct_file_names = file_names[2:]
concatenate_files = pd.concat([pd.read_csv(file) for file in correct_file_names])
os.chdir('../cleansed')
concatenate_files.to_csv('precios-horarios.csv')


#raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":

    clean_data()
    import doctest

    doctest.testmod()
