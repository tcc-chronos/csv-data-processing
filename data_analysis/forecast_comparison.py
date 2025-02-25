import os
import pandas as pd
import matplotlib.pyplot as plt

def forecast_comparison(file_input: str, file_forecast: str, save_imgs_path: str):
    """
    Compara as previsões de dois modelos (EWMA e LSTM) em um gráfico de linha.

    :param file_input: Caminho do arquivo CSV contendo os dados de entrada.
    :param file_forecast: Caminho do arquivo CSV contendo os dados de previsão LSTM.
    :param save_imgs_path: Diretório onde os gráficos serão salvos.
    """
    # Carregar os dados corretamente
    df_input = pd.read_csv(file_input, delimiter=';', dtype=str)
    df_forecast = pd.read_csv(file_forecast, delimiter=';', dtype=str)

    # Converter a coluna de tempo `recvTime` corretamente
    df_input['recvTime'] = pd.to_datetime(df_input['recvTime'], errors='coerce', utc=True)
    df_forecast['recvTime'] = pd.to_datetime(df_forecast['recvTime'], errors='coerce', utc=True)

    os.makedirs(save_imgs_path, exist_ok=True)
  
    # Converter colunas numéricas corretamente
    df_input['ewma_forecast'] = pd.to_numeric(df_input['ewma_forecast'], errors='coerce')
    df_forecast['lstm_forecast'] = pd.to_numeric(df_forecast['lstm_forecast'], errors='coerce')

    # Mesclar os dois DataFrames pelo tempo (recvTime)
    df_merged = pd.merge(df_input[['recvTime', 'ewma_forecast']], df_forecast[['recvTime', 'lstm_forecast']], on='recvTime', how='inner')

    for day, df_day in df_merged.groupby(df_merged['recvTime'].dt.date):
        day_dir = os.path.join(save_imgs_path, str(day))
        os.makedirs(day_dir, exist_ok=True)
        
        for hour, df_hour in df_day.groupby(df_day['recvTime'].dt.hour):
            # Remover linhas onde ambas as previsões são NaN
            df_hour = df_hour.dropna(subset=['ewma_forecast', 'lstm_forecast'], how='all')
            if df_hour.empty:
                continue  # Pular se não houver dados válidos

            plt.figure(figsize=(10, 5))
            
            plt.plot(df_hour['recvTime'], df_hour['ewma_forecast'], label='EWMA Forecast', linestyle='dashed', color='blue')
            plt.plot(df_hour['recvTime'], df_hour['lstm_forecast'], label='LSTM Forecast', linestyle='solid', color='red')

            # Ajustar o eixo Y dinamicamente
            all_values = pd.concat([df_hour['ewma_forecast'], df_hour['lstm_forecast']])
            plt.ylim(all_values.min() - 0.1 * abs(all_values.min()), all_values.max() + 0.1 * abs(all_values.max()))

            plt.xlabel('Time')
            plt.ylabel('Forecast Value')
            plt.title(f'Forecast Comparison - {day} {hour}:00')
            plt.legend()
            
            file_name = f"forecast_{hour}.png"
            plt.savefig(os.path.join(day_dir, file_name))
            plt.close()
