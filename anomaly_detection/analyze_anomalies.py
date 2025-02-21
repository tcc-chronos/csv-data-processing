import matplotlib.pyplot as plt

def analyze_anomalies(df_anomalies, column_name='mean_cpu_usage'):
    """
    Analisa as anomalias detectadas e gera gráficos para visualização.

    :param df_anomalies: DataFrame contendo as anomalias detectadas
    :param column_name: Nome da coluna a ser analisada
    :return: Nenhum, mas gera gráficos das anomalias
    """
    # Plotar as anomalias
    plt.figure(figsize=(10, 6))
    plt.plot(df_anomalies['recvTime'], df_anomalies[column_name], 'ro', label='Anomalias')
    plt.xlabel('Data')
    plt.ylabel(column_name)
    plt.title(f'Anomalias detectadas em {column_name}')
    plt.legend()
    plt.show()
