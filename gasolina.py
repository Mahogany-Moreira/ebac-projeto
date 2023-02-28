# código de geração do gráfico
import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", color="red")
grafico.set(title='Gasolina: Preço por dia (BRL)', xlabel='Dia da semana', ylabel='Preço (BRL)')
