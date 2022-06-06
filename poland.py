import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Lelikoth/Wizualizacja/main/poland.csv')
df['New Cases'] = df['new_cases'].fillna(0)
df['New Deaths'] = df['new_deaths'].fillna(0)
df['New Vaccinations'] = df['new_vaccinations'].fillna(0)
df.dropna()

df_long=pd.melt(df, id_vars=['date'], value_vars=['New Cases', 'New Deaths', 'New Vaccinations'])
fig = px.line(df_long, x='date', y='value', color='variable', labels={'date': 'Date', 'variable': 'Variable', 'value': 'Value','new_cases': 'New cases', 'new_deaths': 'New deaths', 'new_vaccinations': 'New vaccinations'})

fig.update_layout(
    title="Daily Poland statisctics",
    xaxis_title="Date",
    yaxis_title="Value",
    legend_title="Variable",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    template="ggplot2",
)

fig.show()