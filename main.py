from data_export.export_to_csv import export_to_csv
from data_preprocessing.load_data import load_data
from data_preprocessing.analyse_initial_data import analyze_initial_data
from data_preprocessing.transform_data import transform_data


def main():
    FILE_PATH = 'data_test.csv'
    FILE_PATH_INPUT_DATA = 'data_input.csv'
    FILE_PATH_FORECAST_DATA = 'data_forecast.csv'


    # Carregar dados
    df_loaded = load_data(FILE_PATH)
    if df_loaded is None:
        return

    # Analisar dados inicias (exibir quais os nomes dos atributos e tipos de dados)
    analyze_initial_data(df_loaded)

    # Realizar a transposição dos valores de acordo com o tempo, separando em dados de entrada e dados previstos
    df_input, df_forecast = transform_data(df_loaded)

    export_to_csv(df_input, FILE_PATH_INPUT_DATA)
    export_to_csv(df_forecast, FILE_PATH_FORECAST_DATA)

    
if __name__ == '__main__':
    main()
