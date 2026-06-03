import pandas as pd 
import numpy as np
import os 

os.system('cls')

try: 

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';',encoding='iso8859-1') #tipos de codificadores mais usados: iso8859-1 | utf-8 | latin1 | cp1252
    df_roubo_veiculo = df_ocorrencias[['munic','roubo_veiculo' ]]
    #método de agrupar as variáveis quantitativa
    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum()
    #método para ordenar 
    df_roubo_veiculo = df_roubo_veiculo.sort_values(by='roubo_veiculo', ascending=False)

except Exception as e:
    print(f'Falha: {e}') 
    exit()

#Obtendo Informações 
try: 
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    max_roubo_veiculo = np.amax(array_roubo_veiculo)
    min_roubo_veiculo = np.amin(array_roubo_veiculo)
    cidade_max_roubo_veiculo = df_roubo_veiculo.iloc[0]['munic']
    cidade_min_roubo_veiculo = df_roubo_veiculo.iloc[-1]['munic']
    distancia = abs(((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo) * 100)

    print(' Medidas de Posição '.center(100, '='))
    print(f'\nMédia: {media_roubo_veiculo:.2f}')
    print(f'Mediana: {mediana_roubo_veiculo:.2f}')
    print(f'Distância entre a média e mediana: {distancia:.2f}%')
    print(f'Maior quantidade de roubo: {max_roubo_veiculo} | Cidade: {cidade_max_roubo_veiculo}')
    print(f'Menor quantidade de roubo: {min_roubo_veiculo} | Cidade: {cidade_min_roubo_veiculo}\n')

    q1 = np.quantile(array_roubo_veiculo, 0.25)
    q2 = np.quantile(array_roubo_veiculo, 0.5)
    q3 = np.quantile(array_roubo_veiculo, 0.75)

    print(' Medidas de tendência Central '.center(100, '='))
    print(f'\nQ1: {q1}')
    print(f'Q2: {q2:.2f}')
    print(f'Q3: {q3}')


except Exception as e:
    print(f'Erro: {e}') 
    exit()
    