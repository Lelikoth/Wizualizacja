import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv('https://raw.githubusercontent.com/Lelikoth/Wizualizacja/main/world_data.csv', sep=';' )
df['Total cases'] = df['total_cases'].fillna(0)
df['Total deaths'] = df['total_deaths'].fillna(0)
df['Total vaccinations'] = df['total_vaccinations']
df_long=pd.melt(df, id_vars=['date'], value_vars=['Total cases', 'Total deaths', 'Total vaccinations'])
fig = px.line(df_long, x='date', y='value', color='variable')
fig.update_layout(
    title="Covid-19 World Statistics",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    template="ggplot2",
)
fig.show()