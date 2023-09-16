##### Ínicio da etapa de extração de dados ######

import pandas as pd

# Primeiro vamos carregar os dados dos arquivos CSV
df_2022 = pd.read_csv('Violencia_2022.csv', sep=';')
df_2023 = pd.read_csv('Violencia_2023.csv', sep=';')

# Iremos exibir os resultados para verificar
print('Dados de 2022: ')
print(df_2022)

print('Dados de 2023: ')
print(df_2023)

#### fim da etapa de extração #### 

####Ínicio da etapa de transformação ####

#primeiro iremos calcular a média dos casos

media_2022 = df_2022.loc[0, 'Total'] / 6
media_2023 = df_2023.loc[0, 'Total'] / 6

# Agora irei adicionar uma nova coluna com a média para cada ano

df_2022['Media_Casos'] = media_2022
df_2023['Media_Casos'] = media_2023

# Calcular o aumento em porcentagem
aumento_percentual = ((media_2023 - media_2022) / media_2022) * 100

# Agora irei compara as colunas para saber se houve aumento ou diminuição de casos

aumento_diminuicao = "aumento" if media_2023 > media_2022 else "diminuição"

# Irei exibir as medias para análisar os dados

print('\nMédia de casos em 2022: ', media_2022) 
print('Média de casos em 2023: ', media_2023)
print(f'Análise: Houve {aumento_diminuicao} nos casos de 2023 em comparação com 2022.')
print(f'No ano de 2023 o aumento percentual foi de: {aumento_percentual:.2f}%')

# fim da etapa de transformação 

# inicio da etapa de carregamento 
df_2022.to_csv('Violencia_2022_transformado.csv', index=False)
df_2023.to_csv('Violencia_2023_transformado.csv', index=False)

print('Dados transformados com sucesso. Uma nova coluna "Media_Casos" foi adicionada a planilha.')