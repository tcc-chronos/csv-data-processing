from data_analysis.detect_correlation import detect_correlation
from data_analysis.detect_outliers import detect_outliers
from data_analysis.forecast_comparison import forecast_comparison
from data_export.export_to_csv import export_to_csv
from data_export.remove_empty_rows import remove_empty_rows
from data_preprocessing.load_data import load_data
from data_preprocessing.analyse_initial_data import analyze_initial_data
from data_preprocessing.transform_data import transform_data

def main():
    FILE_PATH = 'data_test.csv'
    FILE_PATH_INPUT_DATA = 'data_input.csv'
    FILE_PATH_FORECAST_DATA = 'data_forecast.csv'

    FILE_PATH_IMGS_OUTLIERS = 'imgs/outliers'
    FILE_PATH_IMGS_CORRELATION= 'imgs/correlations'
    FILE_PATH_IMGS_FORECASTS= 'imgs/forecasts'

    DISPLAY_GRAPHS = True

    # Carregar dados
    df_loaded = load_data(FILE_PATH)
    if df_loaded is None:
        return

    # Analisar dados inicias (exibir quais os nomes dos atributos e tipos de dados)
    # analyze_initial_data(df_loaded)

    # Realizar a transposição dos valores de acordo com o tempo, separando em dados de entrada e dados previstos
    df_input, df_forecast = transform_data(df_loaded)

    detect_outliers(df_input, FILE_PATH_IMGS_OUTLIERS, display_graphs=DISPLAY_GRAPHS)
    detect_correlation(df_input, FILE_PATH_IMGS_CORRELATION, display_graphs=DISPLAY_GRAPHS)
    
    df_input, linhas_removidas_input = remove_empty_rows(df_input)
    df_forecast, linhas_removidas_forecast = remove_empty_rows(df_forecast)

    export_to_csv(df_input, FILE_PATH_INPUT_DATA)
    export_to_csv(df_forecast, FILE_PATH_FORECAST_DATA)

    forecast_comparison(FILE_PATH_INPUT_DATA, FILE_PATH_FORECAST_DATA, FILE_PATH_IMGS_FORECASTS)

if __name__ == '__main__':
    main()
