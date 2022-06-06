import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Lelikoth/Wizualizacja/main/covid-cases.csv')
df['total_cases'] = df['total_cases'].fillna(0)
df['per100'] = (df['total_cases'] / df['population'] * 100000).round()

df_eu = df[df['location'] == 'European Union']
df_usa = df[df['location'] == 'United States']
df_merge = pd.concat([df_eu, df_usa])

fig = px.line(df_merge , x="date", y="per100",
              color="location", title="Cases in EU vs. USA",
              symbol="location",
              labels={"per100": "Cases per 100k", "date": "Quarter", "location": "Location", "total_cases": "Total cases", "population": "Population"},
              hover_data=['total_cases', 'location', 'per100', 'population'])

fig.update_layout(
    xaxis_title="Quarter",
    yaxis_title="Cases per 100k",
    legend_title="Location",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    template="ggplot2",
)

fig.show()
