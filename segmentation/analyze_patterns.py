import pandas as pd
import matplotlib.pyplot as plt

def analyze_patterns(df_segmented):
    """
    Analisa padrões e tendências nas segmentações por dia da semana e hora.

    :param df_segmented: DataFrame com os dados segmentados
    :return: Nenhum, mas gera gráficos de padrões identificados
    """
    # Exemplo de análise de tendência para a variável 'mean_cpu_usage' ao longo do tempo
    # Vamos supor que 'mean_cpu_usage' seja uma das colunas no DataFrame segmentado
    mean_cpu_usage = pd.DataFrame(df_segmented['mean_cpu_usage'].to_list())

    # Plotar as tendências de 'mean_cpu_usage' por dia da semana e hora do dia
    plt.figure(figsize=(10, 6))
    for i in range(7):  # Para cada dia da semana
        daily_data = mean_cpu_usage[mean_cpu_usage.index % 7 == i]
        plt.plot(daily_data.mean(axis=1), label=f'Dia {i}')
    
    plt.xlabel('Hora do dia')
    plt.ylabel('Média de uso de CPU')
    plt.legend()
    plt.title('Padrões de Uso de CPU por Dia da Semana')
    plt.show()
