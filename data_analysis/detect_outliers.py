import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from data_analysis.utilities import save_plot

def detect_outliers(df: pd.DataFrame, save_imgs_path: str, quartis_percentile=0.25, multiplier=3, display_graphs=False, ignore_non_outliers=False):
    """
    Analisa os possíveis outliers dos dados e exibe estatísticas básicas, além de gerar gráficos.

    :param df: DataFrame com os dados carregados
    :param save_imgs_path: Diretório no qual as imagens dos outliers serão salvas
    :param quartis_percentile: Percentil usado para calcular Q1 e Q3 (default: 0.25)
    :param multiplier: Multiplicador do IQR para definir os limites dos outliers (default: 3)
    :param display_graphs: Determina se os gráficos gerados serão exibidos em tempo de execução ou apenas salvos (default: False)
    :param ignore_non_outliers: Ignora os dados que não são outliers, não criando seus gráficos (default: False)
    """
    for column in df.select_dtypes(include=[np.number]).columns:
      mean_val = df[column].mean()
      max_val = df[column].max()
      min_val = df[column].min()

      max_percentage = abs((max_val/mean_val - 1) * 100)
      min_percentage = abs((min_val/mean_val - 1) * 100)

      print(f"Estatísticas da coluna '{column}':")
      print(f"\t-> Média: {mean_val:.6f}")
      print(f"\t-> Máximo: {max_val:.6f} [{max_percentage:.2f}%]")
      print(f"\t-> Mínimo: {min_val:.6f} [{min_percentage:.2f}%]")

      # Detectar os outliers
      outliers = detect_outliers_iqr(df, column, quartis_percentile, multiplier)

      if not outliers.empty:
        print(f"\nOutliers encontrados na coluna '{column}':")
        # outliers_display = outliers.reset_index()[["recvTime", column]]
        # print(tabulate(outliers_display, headers="keys", tablefmt="plain", stralign="left", showindex=False))
        
      # Gerar o gráfico
      if not outliers.empty or not ignore_non_outliers :
        save_outlier_plot(df, outliers, column, save_imgs_path, display_graphs)

      print()

def detect_outliers_iqr(df: pd.DataFrame, column: str, quartis_percentile: float, multiplier: float):
  """
  Detecta outliers nos dados a partir da técnica IQR (Interquartile Range).

  :param df: DataFrame com os dados carregados
  :param column: Coluna que será analisada
  :param quartis_percentile: Percentil usado para calcular Q1 e Q3
  :param multiplier: Multiplicador do IQR para definir os limites dos outliers
  """
  Q1 = df[column].quantile(quartis_percentile)
  Q3 = df[column].quantile(1 - quartis_percentile)

  IQR = Q3 - Q1

  lim_inf = Q1 - multiplier * IQR
  lim_sup = Q3 + multiplier * IQR

  return df[(df[column] < lim_inf) | (df[column] > lim_sup)]

def save_outlier_plot(df: pd.DataFrame, outliers: pd.DataFrame, column: str, save_imgs_path: str, display_graphs: bool):
  """
  Plota os dados e destaca os outliers em um gráfico, salvando a imagem no diretório espeficiado, no formato png.
  
  :param df: DataFrame com os dados carregados
  :param outliers: DataFrame contendo os outliers
  :param column: Coluna que será analisada para outliers
  :param save_imgs_path: Diretório no qual as imagens dos outliers serão salvas
  :param display_graphs: Determina se os gráficos gerados serão exibidos em tempo de execução ou apenas salvos
  """
  # df_reset = df.reset_index()  # Resetando o índice para garantir que 'recvTime' seja uma coluna normal
  # outliers_reset = outliers.reset_index() # Resetando o índice para garantir que 'recvTime' seja uma coluna normal

  plt.figure(figsize=(10, 6))

  # Plotando todos os dados
  plt.plot(df.index, df[column], label='Todos os dados', color='blue', marker='o', markersize=3)
  # Plotando os outliers com uma cor diferente
  plt.scatter(outliers.index, outliers[column], color='red', label='Outliers', zorder=5)

  plt.xlabel('Tempo')
  plt.ylabel(column)
  plt.title(f'Outliers na coluna {column}')
  plt.xticks(rotation=45)
  plt.legend()

  save_plot(plt, save_imgs_path, f'{column}_outliers')
  if display_graphs:
    plt.show()
  
  plt.close()
