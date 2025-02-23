import os

def save_plot(ptl, file_path: str, file_name: str):
    """
    Salva a imagem do gráfico gerado no formato png, aplicando tratamento de erro.

    :param ptl: Objeto do gráfico (matplotlib plot)
    :param file_path: Caminho para salvar o gráfico
    :param file_name: Nome do gráfico (será concatenado com .png internamente)
    """
    try:
      if not os.path.exists(file_path):
        os.makedirs(file_path)

      output_file = os.path.join(file_path, f'{file_name}.png')

      ptl.tight_layout()
      ptl.savefig(output_file)
      print(f'Gráfico salvo em: {file_path}')
    except Exception as e:
      print(f"Erro ao salvar o gráfico em {file_path}: {e}")
