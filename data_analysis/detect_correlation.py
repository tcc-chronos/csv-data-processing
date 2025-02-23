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
