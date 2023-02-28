# código de geração do gráfico 
import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", palette="pastel")
grafico.set(title='Preço da gasolina por dia (BRL)', xlabel='Dia da semana', ylabel='Preço (BRL)');
