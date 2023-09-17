# Projeto ETL - Bootcamp de Ciência de Dados DIO
Este projeto foi desenvolvido como parte do Bootcamp de Ciência de Dados da Digital Innovation One (DIO), com o objetivo de concluir os requisitos estabelecidos pelo curso.

O projeto engloba um processo de ETL (Extração, Transformação e Carregamento) básico. Foram extraídos dados de violência interpessoal ocorridos no município de São Gonçalo-RJ no período de janeiro a junho de 2023, comparando-os com o mesmo período do ano de 2022. O sistema computou o quantitativo de ocorrências registradas, calculou uma média e determinou se houve aumento ou diminuição de casos. Em seguida, os dados acrescidos foram carregados em uma nova planilha.

# Etapas da ETL:
## Etapa 1 - Extração (E):
- Dado a ser tratado: Dados de violência contra mulheres negras do município de São Gonçalo-RJ
- Fonte dos dados: DATASUS
- Local de extração: Planilha baixada do site do TABNET.
- Formato do arquivo: CSV.
## Etapa 2 - Transformação (T):
- Alterações nos dados: Nesta etapa, foram aplicadas transformações para limpar os dados, remover duplicatas e adicionar o calculo da média de casos e retornar a informação se houve ou não aumento de registros entre os períodos. 
## Etapa 3 - Carregamento (L):
- Local de atualização dos dados transformados: Os dados transformados foram carregados em um arquivo CSV.
## Próximos Passos:
Melhorias Futuras: Este projeto pode ser expandido com funcionalidades avançadas de ETL, gráficos para visualização dos dados ou integração com outras fontes de dados.

## Autor:
*Jonas Salles*

## Linguagem de programação utilizada:
- Python 

## Agradecimentos:
Agradeço à Digital Innovation One pela oportunidade de aprendizado proporcionada pelo Bootcamp de Ciência de Dados.