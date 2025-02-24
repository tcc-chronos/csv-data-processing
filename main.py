from data_analysis.detect_correlation import detect_correlation
from data_analysis.detect_outliers import detect_outliers
from data_export.export_to_csv import export_to_csv
from data_preprocessing.load_data import load_data
from data_preprocessing.transform_data import transform_data
from data_segmentation.segment_data import TimeSegment, segment_data

def main():
    FILE_PATH = 'data_test.csv'
    FILE_PATH_INPUT_DATA = 'data_input.csv'
    FILE_PATH_FORECAST_DATA = 'data_forecast.csv'
    FILE_PATH_INPUT_SEGMENTED_DATA = 'data_input_segmented.csv'

    FILE_PATH_IMGS_OUTLIERS = 'imgs/outliers'
    FILE_PATH_IMGS_CORRELATION= 'imgs/correlations'

    DISPLAY_GRAPHS = False
    TIME_SEGMENT = TimeSegment.HOUR

    # Carregar dados
    df_loaded = load_data(FILE_PATH)
    if df_loaded is None:
        return

    # Analisar dados inicias (exibir quais os nomes dos atributos e tipos de dados)
    # analyze_initial_data(df_loaded)

    # Realizar a transposição dos valores de acordo com o tempo, separando em dados de entrada e dados previstos
    df_input, df_forecast = transform_data(df_loaded)

    # Detectar e salvar os outliers nos dados de entrada
    detect_outliers(df_input, FILE_PATH_IMGS_OUTLIERS, display_graphs=DISPLAY_GRAPHS)

    # Detectar e salvar as correlações entre os dados de entrada
    detect_correlation(df_input, FILE_PATH_IMGS_CORRELATION, display_graphs=DISPLAY_GRAPHS)
    
    # Segmentar os dados de entrada em segmentos de tempo (exibir as estatísticas dos dados de entrada)
    df_segmented_input = segment_data(df_input, TIME_SEGMENT)
    if df_segmented_input is None:
        return
    detect_outliers(df_segmented_input, FILE_PATH_IMGS_OUTLIERS + '/segmented', display_graphs=DISPLAY_GRAPHS, ignore_non_outliers=True)
    
    print('Exportando csv')
    export_to_csv(df_input, FILE_PATH_INPUT_DATA)
    export_to_csv(df_forecast, FILE_PATH_FORECAST_DATA)
    export_to_csv(df_segmented_input, FILE_PATH_INPUT_SEGMENTED_DATA)


if __name__ == '__main__':
    main()
