import pandas as pd

def transform_data(df: pd.DataFrame):
    """
    Realiza a análise inicial dos dados, antes das transformações.

    :param df: DataFrame com os dados carregados e tratados
    :return: Tupla de DataFrames, separando as entradas dos valores previstos
    """
    try:
        # Verifica se df é um DataFrame válido
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Erro: O objeto fornecido não é um DataFrame válido.")
        
        # Verifica se as colunas necessárias existem no DataFrame
        required_columns = {'attrName', 'recvTime', 'attrValue'}
        if not required_columns.issubset(df.columns):
            raise KeyError(f"Erro: O DataFrame não contém todas as colunas obrigatórias: {required_columns}")

        # Processamento dos dados de previsão (lstm_forecast)
        df_lstm_pivot, df_other_pivot = None, None

        df_lstm = df[df['attrName'] == 'lstm_forecast']
        if not df_lstm.empty:
            df_lstm_pivot = df_lstm.pivot_table(index='recvTime', columns='attrName', values='attrValue', aggfunc='first')
            df_lstm_pivot = df_lstm_pivot.dropna(axis=1, how='all')
            df_lstm_pivot["lstm_forecast"] = pd.to_numeric(df_lstm_pivot["lstm_forecast"], errors="coerce")

        # Processamento dos demais dados
        df_other = df[df['attrName'] != 'lstm_forecast']
        if not df_other.empty:
            df_other_pivot = df_other.pivot_table(index='recvTime', columns='attrName', values='attrValue', aggfunc='first')
            df_other_pivot = df_other_pivot.dropna(axis=1, how='all')

            df_other_pivot = df_other_pivot.apply(pd.to_numeric, errors="coerce")

        return df_other_pivot, df_lstm_pivot

    except ValueError as ve:
        print(ve)
    except KeyError as ke:
        print(ke)
    except Exception as e:
        print(f"Erro inesperado ao transformar os dados: {e}")

    return None, None
