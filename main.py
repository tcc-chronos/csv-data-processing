from data_preprocessing.clean_data import clean_data
from data_preprocessing.handle_missing_values import handle_missing_values
from data_preprocessing.handle_outliers import handle_outliers
from data_preprocessing.load_data import load_data
from segmentation.segment_by_day import segment_by_day
from lstm_training.prepare_training_data import prepare_training_data
# from lstm_training.train_lstm import train_lstm
# from lstm_training.evaluate_model import evaluate_model

def main():
    # Carregar os dados
    df = load_data('data_test.csv')
    
    # Pré-processamento
    df_cleaned = clean_data(df)
    
    # Segmentação
    df_segmented = segment_by_day(df_cleaned)

    df_handled = handle_missing_values(df_segmented, "drop")
    print(len(df_handled))

    df_handled_outliers = handle_outliers(df_handled, 1)
    print(len(df_handled_outliers))
    
    # Preparar dados para LSTM
    # X_train, y_train = prepare_training_data(df_segmented, ['mean_cpu_usage'])
    
#     # Treinamento do modelo LSTM
#     model = train_lstm(X_train, y_train)
    
#     # Avaliação do modelo
#     mse, mae = evaluate_model(model, X_train, y_train)
    
#     print(f'Modelo avaliado com MSE: {mse} e MAE: {mae}')

    df_handled.to_csv("vitaoSemFreio3.csv", sep=";", index=False)
    
if __name__ == '__main__':
    main()
