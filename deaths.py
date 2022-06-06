
import pandas as pd
import plotly.express as px


path = 'https://raw.githubusercontent.com/Lelikoth/Wizualizacja/main/covid-cases.csv'
df = pd.read_csv(path)

df['total_cases'] = df['total_cases'].fillna(0)
df['total_deaths'] = df['total_deaths'].fillna(0)
df['total_vaccinations'] = df['total_vaccinations'].fillna(0)
df = df.dropna()

df['death_rate'] = round((df['total_deaths'] / df['population']) * 100, 2)

fig = px.choropleth(df, locations='location', locationmode='country names', color='death_rate', scope='world',
                    hover_data=['population', 'total_deaths', 'date'],
                    animation_frame='date', animation_group='location', color_continuous_scale='reds',
                    range_color=[0, df['death_rate'].max()], labels={'location': 'Location', 'total_deaths': 'Deaths',
                                                                     'date': 'Quarter', 'death_rate': 'Rate'})

fig.update_layout(
    title="Deaths in the World",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    geo=dict(
        scope='world',
        projection_type='natural earth'
    ),
    template="ggplot2",
)


fig.show()
