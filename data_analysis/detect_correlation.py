import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from data_analysis.utilities import save_plot

def detect_correlation(df: pd.DataFrame, save_imgs_path: str, display_graphs: bool=False):
  """
  Identifica correlações entre as colunas de um dataFrame especificado

  :param df: DataFrame com os dados carregados
  :param save_imgs_path: Diretório no qual as imagens dos outliers serão salvas
  :param display_graphs: Determina se os gráficos gerados serão exibidos em tempo de execução ou apenas salvos (default: False)
  """
  print('Analisando correlações entre os dados')
  correlation_matrix = df.corr()
  plt.figure(figsize=(10, 6))
  sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
  plt.title('Matriz de Correlação das Variáveis')

  save_plot(plt, save_imgs_path, 'correlations')
  if display_graphs:
    plt.show()
    
  plt.close()

def detect_incoming_cpu_correlation(df: pd.DataFrame, save_imgs_path: str, display_graphs: bool = False):
  """
  Identifica a correlação entre o número de incoming (incoming_tx_mean) e o uso médio de CPU (mean_cpu_usage).
    
  :param df: DataFrame com os dados carregados
  :param save_imgs_path: Diretório no qual as imagens dos gráficos serão salvas
  :param display_graphs: Determina se os gráficos gerados serão exibidos em tempo de execução ou apenas salvos (default: False)
  """
  print('Analisando correlação entre incoming e uso de CPU')

  # Selecionar colunas de interesse
  cols_of_interest = ["incoming_tx_mean", "mean_cpu_usage"]
  df_corr = df[cols_of_interest].dropna()

  # Calcular a correlação
  correlation_matrix = df_corr.corr()
  correlation_value = correlation_matrix.loc["incoming_tx_mean", "mean_cpu_usage"]
  print(f"Correlação entre incoming_tx_mean e mean_cpu_usage: {correlation_value:.2f}")

  # Criar gráfico de dispersão
  plt.figure(figsize=(8, 6))
  sns.scatterplot(x=df_corr["incoming_tx_mean"], y=df_corr["mean_cpu_usage"], alpha=0.5)
  sns.regplot(x=df_corr["incoming_tx_mean"], y=df_corr["mean_cpu_usage"], scatter=False, color="red")

  plt.xlabel("incoming_tx_mean")
  plt.ylabel("mean_cpu_usage")
  plt.title(f"Correlação: {correlation_value:.2f}")
  plt.grid(True)

  # Criar diretório, se não existir
  os.makedirs(save_imgs_path, exist_ok=True)
  img_path = os.path.join(save_imgs_path, "incoming_cpu_correlation.png")

  # Salvar gráfico
  plt.savefig(img_path)
  if display_graphs:
      plt.show()

  plt.close()
  print(f"Gráfico de correlação entre incoming e uso de CPU salvo em: {img_path}")


def detect_incoming_service_time_correlation(df: pd.DataFrame, save_imgs_path: str, display_graphs: bool = False):
    """
    Identifica a correlação entre o número de incoming (incoming_tx_mean) e o tempo médio de serviço (service_time_mean).
    
    :param df: DataFrame com os dados carregados
    :param save_imgs_path: Diretório no qual as imagens dos gráficos serão salvas
    :param display_graphs: Determina se os gráficos gerados serão exibidos em tempo de execução ou apenas salvos (default: False)
    """
    print('Analisando correlação entre incoming_tx_mean e service_time_mean')

    # Selecionar colunas de interesse
    cols_of_interest = ["incoming_tx_mean", "service_time_mean"]
    df_corr = df[cols_of_interest].dropna()

    # Calcular a correlação
    correlation_matrix = df_corr.corr()
    correlation_value = correlation_matrix.loc["incoming_tx_mean", "service_time_mean"]
    print(f"Correlação entre incoming_tx_mean e service_time_mean: {correlation_value:.2f}")

    # Criar gráfico de dispersão
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df_corr["incoming_tx_mean"], y=df_corr["service_time_mean"], alpha=0.5)
    sns.regplot(x=df_corr["incoming_tx_mean"], y=df_corr["service_time_mean"], scatter=False, color="blue")

    plt.xlabel("incoming_tx_mean")
    plt.ylabel("service_time_mean")
    plt.title(f"Correlação: {correlation_value:.2f}")
    plt.grid(True)

    # Criar diretório, se não existir
    os.makedirs(save_imgs_path, exist_ok=True)
    img_path = os.path.join(save_imgs_path, "incoming_service_time_correlation.png")

    # Salvar gráfico
    plt.savefig(img_path)
    if display_graphs:
        plt.show()

    plt.close()
    print(f"Gráfico de correlação entre incoming_tx_mean e service_time_mean salvo em: {img_path}")


def detect_incoming_pod_cpu_correlation(file_input: str, save_imgs_path: str, display_graphs: bool = False):
    print('Analisando correlação entre incoming_tx_mean * pods_now e uso de CPU')

    # Carregar os dados do CSV
    df_input = pd.read_csv(file_input, delimiter=';', dtype=str)

    # Verificar se 'recvTime' está presente ou renomear caso esteja sem nome
    if 'recvTime' not in df_input.columns:
        df_input.rename(columns={df_input.columns[0]: 'recvTime'}, inplace=True)

    # Converter a coluna de tempo `recvTime` corretamente
    df_input['recvTime'] = pd.to_datetime(df_input['recvTime'], errors='coerce', utc=True)

    # Converter colunas numéricas corretamente
    numeric_columns = ['incoming_tx_mean', 'mean_cpu_usage', 'pods_now']
    for col in numeric_columns:
        df_input[col] = pd.to_numeric(df_input[col], errors='coerce')

    # Filtrar dados a partir das 6:00
    df_filtered = df_input[df_input['recvTime'].dt.hour >= 6]

    # Encontrar o momento em que 'pods_now' é 3 pela primeira vez
    pod_3_mask = df_filtered['pods_now'] == 3
    if pod_3_mask.any():
        # Identificar o primeiro índice de 3 pods
        first_pod_3_index = df_filtered[pod_3_mask].index[0]
        
        # Encontrar o último índice onde 'pods_now' é 3, antes de mudar
        df_filtered = df_filtered.loc[first_pod_3_index:]  # Filtra a partir do primeiro 3
        last_pod_3_index = df_filtered[df_filtered['pods_now'] != 3].index[0]  # Pega a mudança para outro valor de pods
        
        # Identificar os horários de início e fim do intervalo
        pod_3_start_time = df_filtered.loc[first_pod_3_index, 'recvTime']
        pod_3_end_time = df_filtered.loc[last_pod_3_index - 1, 'recvTime']  # Antes da mudança para outro número de pods
        
        # Formatar o intervalo de tempo
        time_range = f"Das {pod_3_start_time.strftime('%H:%M')} até {pod_3_end_time.strftime('%H:%M')}"
        
        # Filtrar os dados até o último momento onde pods_now foi 3
        df_filtered = df_filtered.loc[:last_pod_3_index - 1]
    else:
        time_range = "Sem intervalo com 3 pods"

    # Criando novo gráfico considerando incoming_tx_mean * pods_now
    df_filtered = df_filtered.dropna(subset=['incoming_tx_mean', 'mean_cpu_usage', 'pods_now'])
    df_filtered['incoming_pod_product'] = df_filtered['incoming_tx_mean'] * df_filtered['pods_now']

    # Calcular a correlação entre incoming_pod_product e mean_cpu_usage
    correlation = df_filtered['incoming_pod_product'].corr(df_filtered['mean_cpu_usage'])

    # Exibir informações no terminal
    print("\nResumo dos Dados Filtrados:")
    print("Horas disponíveis:", df_filtered['recvTime'].dt.hour.unique())
    print("Número de Pods Ativos:", df_filtered['pods_now'].unique())
    print(f"Correlação entre incoming_tx_mean * pods_now e mean_cpu_usage: {correlation:.4f}")
    print(f"Intervalo de tempo com 3 pods: {time_range}")

    # Criar o gráfico
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df_filtered['incoming_pod_product'], y=df_filtered['mean_cpu_usage'], alpha=0.5)
    sns.regplot(x=df_filtered['incoming_pod_product'], y=df_filtered['mean_cpu_usage'], scatter=False, color='blue')
    plt.xlabel('incoming_tx_mean * pods_now')
    plt.ylabel('mean_cpu_usage')
    plt.title(f'Correlação entre Incoming Transactions * Pods e Uso de CPU\nCorrelação: {correlation:.4f}\n{time_range}')
    plt.grid(True)

    # Criar diretório se não existir e salvar o gráfico
    os.makedirs(save_imgs_path, exist_ok=True)
    save_plot(plt, save_imgs_path, 'incoming_pod_cpu_correlation')

    if display_graphs:
        plt.show()
    plt.close()

    print('Análise concluída e gráfico salvo.')


def detect_incoming_pod_service_time_correlation(file_input: str, save_imgs_path: str, display_graphs: bool = False):
    print('Analisando correlação entre incoming_tx_mean * pods_now e Service Time')

    # Carregar os dados do CSV
    df_input = pd.read_csv(file_input, delimiter=';', dtype=str)

    # Verificar se 'recvTime' está presente ou renomear caso esteja sem nome
    if 'recvTime' not in df_input.columns:
        df_input.rename(columns={df_input.columns[0]: 'recvTime'}, inplace=True)

    # Converter a coluna de tempo `recvTime` corretamente
    df_input['recvTime'] = pd.to_datetime(df_input['recvTime'], errors='coerce', utc=True)

    # Converter colunas numéricas corretamente
    numeric_columns = ['incoming_tx_mean', 'service_time_mean', 'pods_now']
    for col in numeric_columns:
        df_input[col] = pd.to_numeric(df_input[col], errors='coerce')

    # Filtrar dados a partir das 6:00
    df_filtered = df_input[df_input['recvTime'].dt.hour >= 6]

    # Encontrar o momento em que 'pods_now' é 3 pela primeira vez
    pod_3_mask = df_filtered['pods_now'] == 3
    if pod_3_mask.any():
        # Identificar o primeiro índice de 3 pods
        first_pod_3_index = df_filtered[pod_3_mask].index[0]
        
        # Encontrar o último índice onde 'pods_now' é 3, antes de mudar
        df_filtered = df_filtered.loc[first_pod_3_index:]  # Filtra a partir do primeiro 3
        last_pod_3_index = df_filtered[df_filtered['pods_now'] != 3].index[0]  # Pega a mudança para outro valor de pods
        
        # Identificar os horários de início e fim do intervalo
        pod_3_start_time = df_filtered.loc[first_pod_3_index, 'recvTime']
        pod_3_end_time = df_filtered.loc[last_pod_3_index - 1, 'recvTime']  # Antes da mudança para outro número de pods
        
        # Formatar o intervalo de tempo
        time_range = f"Das {pod_3_start_time.strftime('%H:%M')} até {pod_3_end_time.strftime('%H:%M')}"
        
        # Filtrar os dados até o último momento onde pods_now foi 3
        df_filtered = df_filtered.loc[:last_pod_3_index - 1]
    else:
        time_range = "Sem intervalo com 3 pods"

    # Criando novo gráfico considerando incoming_tx_mean * pods_now
    df_filtered = df_filtered.dropna(subset=['incoming_tx_mean', 'service_time_mean', 'pods_now'])
    df_filtered['incoming_pod_product'] = df_filtered['incoming_tx_mean'] * df_filtered['pods_now']

    # Calcular a correlação entre incoming_pod_product e service_time_mean
    correlation = df_filtered['incoming_pod_product'].corr(df_filtered['service_time_mean'])

    # Exibir informações no terminal
    print("\nResumo dos Dados Filtrados:")
    print("Horas disponíveis:", df_filtered['recvTime'].dt.hour.unique())
    print("Número de Pods Ativos:", df_filtered['pods_now'].unique())
    print(f"Correlação entre incoming_tx_mean * pods_now e service_time_mean: {correlation:.4f}")
    print(f"Intervalo de tempo com 3 pods: {time_range}")

    # Criar o gráfico
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df_filtered['incoming_pod_product'], y=df_filtered['service_time_mean'], alpha=0.5)
    sns.regplot(x=df_filtered['incoming_pod_product'], y=df_filtered['service_time_mean'], scatter=False, color='blue')
    plt.xlabel('incoming_tx_mean * pods_now')
    plt.ylabel('service_time_mean')
    plt.title(f'Correlação entre Incoming Transactions * Pods e Service Time\nCorrelação: {correlation:.4f}\n{time_range}')
    plt.grid(True)

    # Criar diretório se não existir e salvar o gráfico
    os.makedirs(save_imgs_path, exist_ok=True)
    save_plot(plt, save_imgs_path, 'incoming_pod_service_time_correlation')

    if display_graphs:
        plt.show()
    plt.close()

    print('Análise concluída e gráfico salvo.')