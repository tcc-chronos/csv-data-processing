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

  plt.xlabel("Incoming Transactions Mean")
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

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def detect_cpu_incoming_correlation_matrix(df: pd.DataFrame, save_imgs_path: str, display_graphs: bool = False):
  """
  Gera uma matriz de correlação apenas entre o uso médio de CPU e o número de transações incoming.

  :param df: DataFrame com os dados carregados.
  :param save_imgs_path: Diretório no qual a imagem do gráfico será salva.
  :param display_graphs: Determina se o gráfico será exibido em tempo de execução ou apenas salvo (default: False).
  """
  selected_columns = ['mean_cpu_usage', 'incoming_tx_mean']
  df_selected = df[selected_columns].dropna()
    
  correlation_matrix = df_selected.corr()
    
  plt.figure(figsize=(6, 4))
  sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
  plt.title('Correlação entre Uso de CPU e Incoming Transactions')
    
  save_path = f"{save_imgs_path}/cpu_incoming_correlation_matrix.png"
  plt.savefig(save_path)
    
  if display_graphs:
      plt.show()
    
  plt.close()
  print(f"Matriz de correlação de Requisições e Processamento salva em: {save_path}")

